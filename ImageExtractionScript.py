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
