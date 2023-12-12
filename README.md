# dedoope

## Introduction

Welcome to dedoope - the Dropbox Deduplicator! This tool is designed to help you efficiently deduplicate files in your Dropbox account. By identifying and managing duplicate files, you can save valuable time and reduce unnecessary storage costs. This Python-based utility is user-friendly and can be a great addition to your file management toolkit.

## Getting Started

### Setting Up Dropbox API Access

To use Dropbox Deduplicator, you'll first need to set up Dropbox API access:

1. **Create a Dropbox App**:
   - Go to the [Dropbox Developers App Console](https://www.dropbox.com/developers/apps).
   - Click "Create App", choose the "Scoped Access".
   - Select "Full Dropbox" or "App Folder" access, depending on your preference.
   - Name your app and create it.

2. **Configure Permissions**:
   - In the App Console, under the "Permissions" tab of your app, enable the following scopes:
     - `files.content.write`
     - `files.metadata.read`
   - Save your changes.

3. **Generate Access Token**:
   - In the settings of your app, locate the "OAuth 2" section.
   - Click on the "Generate" button to create an access token. This token will be used in the Dropbox Deduplicator script.

### Installation

#### Prerequisites

Make sure you have Python installed on your system (Python 3.6 or later is recommended). You'll also need the Dropbox SDK and tqdm library for Python. Install them using pip:

```bash
pip install dropbox tqdm
```

#### Downloading and Running the Script

1. **Download the Script**:
   - Clone or download this repository to your local machine.

2. **Set Up**:
   - Open the script in a text editor.
   - Replace `'YOUR_ACCESS_TOKEN'` with the access token you generated earlier.

3. **Running the Program**:
   - Open a terminal and navigate to the directory containing the script.
   - Run the script using Python:
     ```bash
     python deduplicator.py [scan|delete]
     ```
   - Use `scan` to generate a report of duplicates or `delete` to remove duplicates interactively.

## Contributing

Your contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/yourusername/dropbox-deduplicator](https://github.com/yourusername/dropbox-deduplicator)
