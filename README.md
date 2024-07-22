
# Image Extraction Script
## Description
This project provides a script to extract all images from subdirectories within a specified folder and save them into a single folder with sequential filenames.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)

## Usage
To use the script, you need to provide the path to the folder containing subdirectories with images.

    1. Update the folder_path with the appropriate path.
    2. Run the script:

### Example
Here is an example of how to use the script:

    import os
    import shutil


    def extract_images(folder_path):
        counter = 1
        for root, dirs, files in os.walk(folder_path):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                for file in os.listdir(dir_path):
                    if file.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.gif')):
                        src_path = os.path.join(dir_path, file)
                        dst_path = os.path.join(folder_path, f"{counter}.{file.split('.')[-1]}")
                        shutil.copy(src_path, dst_path)
                        counter += 1


    # Example usage:
    folder_path = "/path/to/your/image/folder"
    extract_images(folder_path)


## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).



