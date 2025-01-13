import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("source_dir", type=str, help="Path to the source directory.")
    parser.add_argument("destination_dir", type=str, nargs="?", default="dist", help="Path to the destination directory (default: 'dist').")
    return parser.parse_args()

def create_directory(path):
    # Create a directory if it doesn't exist
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {path}: {e}")

def copy_and_sort_files(src_dir, dest_dir):
    # Recursively copy files from src_dir to dest_dir, sorting them by file extension
    try:
        for entry in os.listdir(src_dir):
            full_path = os.path.join(src_dir, entry)

            if os.path.isdir(full_path):
                # Recursively handle directories
                copy_and_sort_files(full_path, dest_dir)
            elif os.path.isfile(full_path):
                # Sort files by extension
                file_extension = os.path.splitext(entry)[1].lstrip(".").lower() or "no_extension"
                target_dir = os.path.join(dest_dir, file_extension)
                create_directory(target_dir)

                try:
                    shutil.copy2(full_path, target_dir)
                    print(f"Copied: {full_path} to {target_dir}")
                except IOError as e:
                    print(f"Error copying file {full_path}: {e}")
    except PermissionError as e:
        print(f"Permission error accessing {src_dir}: {e}")
    except FileNotFoundError as e:
        print(f"Directory not found: {src_dir}: {e}")

def main():
    args = parse_arguments()
    source_dir = os.path.abspath(args.source_dir)
    destination_dir = os.path.abspath(args.destination_dir)

    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    create_directory(destination_dir)
    copy_and_sort_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
