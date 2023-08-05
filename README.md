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


### Windows Startup Folder Method
To automatically run the script when your computer starts, you can use the Windows Startup folder method. Here's how to do it:

1. Press `Windows + R` to open the Run dialog box.
2. Type `shell:startup` and click OK. This will open the Startup folder.
3. Create a shortcut for the `downloadorganizer.py` script:
   - Right-click on the `downloadorganizer.py` script.
   - Select "Create shortcut."

4. Move the created shortcut into the Startup folder:
   - Press `Windows + R` to open the Run dialog box again.
   - Type `shell:startup` and click OK. This will open the Startup folder.
   - Move the shortcut you created for the `downloadorganizer.py` script into this folder.

5. Now, right-click on the shortcut in the Startup folder and select "Properties."

6. In the properties window, go to the "Shortcut" tab.

7. In the "Target" field, make sure the path to the Python executable and your `downloadorganizer.py` script is correct. It should look something like this:

```
"C:\path\to\python.exe" "C:\path\to\downloadorganizer.py"
```

Note: Replace `C:\path\to` with the actual path to your Python executable and script.

8. In the same properties window, find the "Run" option and choose "Minimized" from the drop-down menu. This will run the script without popping-up the command prompt window.

9. Click Apply then OK to save the changes.

10. Reboot your computer.

Now, the `downloadorganizer.py` script will be automatically executed every time you start your computer and log in to your user account. It will work silently in the background, organizing your files in the download folder according to their file extensions.


### Note
Please note that this setup guide is specifically for Windows operating systems. For macOS and Linux, you may need to follow a different approach to automatically run the script on startup.

If you encounter any issues or have specific feature requests, please feel free to open an issue on this repository.

## License

This project is licensed under the MIT License 
