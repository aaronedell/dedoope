import dropbox
import sys
import time
from tqdm import tqdm  # For progress bar, install using 'pip install tqdm'

def main(mode):
    dbx = dropbox.Dropbox('YOUR_ACCESS_TOKEN')
    file_info = {}
    processed_files_count = 0
    limit_per_call = 1000  # Adjust the number of files processed per API call
    progress_bar = tqdm(total=limit_per_call, desc="Scanning files")

    try:
        response = dbx.files_list_folder('', recursive=True, limit=limit_per_call)
        while True:
            for entry in response.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    file_info[entry.path_lower] = entry.content_hash
                    processed_files_count += 1
                    progress_bar.update(1)

            if processed_files_count >= limit_per_call or not response.has_more:
                break

            response = dbx.files_list_folder_continue(response.cursor)

    except dropbox.exceptions.ApiError as err:
        print(f'API error: {err}')
    finally:
        progress_bar.close()

    # Process duplicates
    duplicates = {}
    for path, hash in file_info.items():
        if hash in duplicates:
            duplicates[hash].append(path)
        else:
            duplicates[hash] = [path]

    if mode == 'scan':
        with open('duplicate_report.txt', 'w') as file:
            for hash, paths in duplicates.items():
                if len(paths) > 1:
                    file.write(f'Duplicate files with hash {hash}:\n')
                    for path in paths:
                        file.write(f'  {path}\n')
        print("Scan complete. Report saved to 'duplicate_report.txt'.")

    elif mode == 'delete':
        for hash, paths in duplicates.items():
            if len(paths) > 1:
                print(f'Duplicate files with hash {hash}:')
                for path in paths:
                    print(f'  {path}')
                user_input = input("Delete all but one of these files? (y/n/q): ")
                if user_input.lower() == 'y':
                    for path in paths[:-1]:  # Keep one file, delete the rest
                        try:
                            dbx.files_delete_v2(path)
                            print(f'Deleted {path}')
                        except dropbox.exceptions.ApiError as err:
                            print(f'Error deleting {path}: {err}')
                elif user_input.lower() == 'q':
                    print("Quitting...")
                    break
                print("Moving to next group...")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['scan', 'delete']:
        print("Usage: python script.py [scan|delete]")
    else:
        main(sys.argv[1])
