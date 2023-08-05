# Download Organizer

## Description

Download Organizer is a Python script that automatically organizes files in your Downloads folder into specific destination folders based on their file extensions. It helps keep your Downloads folder clean and organized, making it easier to find and manage your files.

The script continuously monitors the Downloads folder and moves files to the appropriate destination folder according to their file extensions. If a file's extension is not listed, it will be moved to the "Other" folder.

## Features

- Automatically organizes files based on their file extensions
- Customizable destination folders for different file types
- Moves files to the "Other" folder if the extension is not listed
- Periodically runs every 5 seconds to check for new files

## How to Use

### Setup

1. Clone this repository to your local machine.
2. Make sure you have Python installed (at least Python 3.6).

### Configuration

1. Open the `downloadorganizer.py` script in a text editor.
2. Customize the `destination_folders` dictionary with your preferred folder paths for different file types.
3. Customize the `file_extensions` dictionary with the corresponding destination folder names for each file extension.
4. Set the `destination_path` variable to the root folder where the destination folders will be created.

### Running the Script

To run the script, simply execute the `downloadorganizer.py` script on your prompt using Python:

```
python downloadorganizer.py
```

The script will continuously monitor the Downloads folder and organize new files as they are added.

### Automatic Startup (Windows)

To automatically run the script when your computer starts, you can use the Windows Startup folder method. Here's how to do it:

1. Open File Explorer and navigate to:

```
C:\Users<your_username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

2. Copy the `download_organizer.py` script into the Startup folder.
3. Reboot your computer.

The script will now run every time you start your computer and log in to your user account.

### Note

This script should also work on macOS and Linux, but I haven't tested on those yet.

If you encounter any issues or have specific feature requests, please feel free to open an issue on this repository.

## License

This project is licensed under the MIT License 
