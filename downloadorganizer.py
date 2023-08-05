import os
import shutil
import time

def get_unique_filename(dest_folder, filename):
    base_name, extension = os.path.splitext(filename)
    index = 1
    while True:
        new_filename = f"{base_name} ({index}){extension}"
        new_path = os.path.join(dest_folder, new_filename)
        if not os.path.exists(new_path):
            return new_filename
        index += 1

def create_destination_folders(destination_folders):
    for folder in destination_folders.values():
        if not os.path.exists(folder):
            os.makedirs(folder)

def organize_files(download_folder, destination_folders):
    file_extensions = {
        'exe': 'Applications',
        'msi': 'Applications',
        'zip': 'Zip',
        'rar': 'Zip',
        'pdf': 'PDFs',
        'doc': 'WordDocs',
        'docx': 'WordDocs',
        'txt': 'WordDocs',
        'rtf': 'WordDocs',
        'xls': 'SpreadSheets',
        'xlsx': 'SpreadSheets',
        'ods': 'SpreadSheets',
        'ppt': 'PowerPoints',
        'pptx': 'PowerPoints',
        'png': 'Images',
        'jpg': 'Images',
        'jpeg': 'Images',
        'svg': 'Images',
        'gif': 'Images',
        'avif': 'Images',
        'mp4': 'Videos',
        'mov': 'Videos',
        'wmv': 'Videos',
        'avi': 'Videos',
        'avchd': 'Videos',
        'flv': 'Videos',
        'f4v': 'Videos',
        'swf': 'Videos',
        'mkv': 'Videos',
        'mp3': 'Sounds',
        'wav': 'Sounds',
        'ogg': 'Sounds',
        'flac': 'Sounds',
        'aif': 'Sounds',
        'aiff': 'Sounds',
        'wma': 'Sounds',
        'mid': 'Sounds',
        'midi': 'Sounds',
        'eps': 'Vectors',
        'ai': 'Vectors',
        'svg': 'Vectors',
        'cdr': 'Vectors',
        'emf': 'Vectors',
        'wmf': 'Vectors',
        'fig': 'Vectors',
        'ico': 'Icons',
        'css': 'Programming',
        'html': 'Programming',
        'py': 'Programming',
        'js': 'Programming',
        'ts': 'Programming',
        'json': 'Programming',
        'jsx': 'Programming',
        'java': 'Programming',
        'cs': 'Programming',
        'cpp': 'Programming',
        'php': 'Programming',
        'webp': 'Programming',
        'sqlite': 'Databases',
        'db': 'Databases',
        'db3': 'Databases',
        'mysql': 'Databases',
        'sql': 'Databases',
        'pgsql': 'Databases',
        'mdf': 'Databases',
        'ndf': 'Databases',
        'ldf': 'Databases',
        'bak': 'Databases',
        'dbf': 'Databases',
        'dmp': 'Databases',
        'log': 'Databases',
        'ctl': 'Databases',
        'bson': 'Databases',
        'mariadb': 'Databases',
        'db2': 'Databases',
        'db2f': 'Databases',
        'db2g': 'Databases',

    }

    create_destination_folders(destination_folders)

    while True:
        for filename in os.listdir(download_folder):
            src_path = os.path.join(download_folder, filename)

            if os.path.isfile(src_path):
                _, file_extension = os.path.splitext(filename)
                file_extension = file_extension[1:].lower()  

                if file_extension in file_extensions:
                    folder_name = file_extensions[file_extension]
                else:
                    base_name, _ = os.path.splitext(filename)
                    _, base_extension = os.path.splitext(base_name)
                    base_extension = base_extension[1:].lower()
                    if base_extension in file_extensions:
                        folder_name = file_extensions[base_extension]
                    else:
                        folder_name = 'Other'

                if folder_name in destination_folders:
                    dest_folder = destination_folders[folder_name]
                else:
                    print(f"Unknown destination folder for extension: {file_extension}")
                    continue

                dest_path = os.path.join(dest_folder, filename)
                if os.path.exists(dest_path):
                    new_filename = get_unique_filename(dest_folder, filename)
                    dest_path = os.path.join(dest_folder, new_filename)
                shutil.move(src_path, dest_path)
                print(f"Moved {filename} to {dest_path}")

        time.sleep(5)

if __name__ == "__main__":
    download_folder = "your/download/folder/path"
    destination_path = "your/destination/folder/path"

    destination_folders = {
    'Applications': os.path.join(destination_path, 'Applications'),
    'Zip': os.path.join(destination_path, 'Zip'),
    'PDFs': os.path.join(destination_path, 'PDFs'),
    'WordDocs': os.path.join(destination_path, 'WordDocs'),
    'SpreadSheets': os.path.join(destination_path, 'SpreadSheets'),
    'PowerPoints': os.path.join(destination_path, 'PowerPoints'),
    'Images': os.path.join(destination_path, 'Images'),
    'Videos': os.path.join(destination_path, 'Videos'),
    'Sounds': os.path.join(destination_path, 'Sounds'),
    'Vectors': os.path.join(destination_path, 'Vectors'),
    'Icons': os.path.join(destination_path, 'Icons'),
    'Programming': os.path.join(destination_path, 'Programming'),
    'Databases': os.path.join(destination_path, 'Databases'),
    'Other': os.path.join(destination_path, 'Other')
    }

    organize_files(download_folder, destination_folders)
