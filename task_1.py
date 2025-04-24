import os
import sys
import shutil
import argparse

def copy_and_sort_files(source_path, destination_path):
    """
    Recursively copy files from source_path to destination_path,
    sorting them into subdirectories based on file extensions.
    """
    try:
        # List all items in the source directory
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)
            
            try:
                if os.path.isdir(item_path):
                    # If it's a directory, recursively process it
                    copy_and_sort_files(item_path, destination_path)
                else:
                    # If it's a file, determine its extension and copy it
                    _, extension = os.path.splitext(item)
                    
                    # Remove the dot from the extension
                    extension = extension[1:] if extension else "no_extension"
                    
                    # Create the subdirectory if it doesn't exist
                    extension_dir = os.path.join(destination_path, extension)
                    if not os.path.exists(extension_dir):
                        os.makedirs(extension_dir)
                    
                    # Copy the file to the appropriate subdirectory
                    destination_file = os.path.join(extension_dir, item)
                    shutil.copy2(item_path, destination_file)
                    print(f"Copied: {item_path} -> {destination_file}")
            
            except Exception as e:
                print(f"Error processing {item_path}: {e}")
    
    except Exception as e:
        print(f"Error accessing {source_path}: {e}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Copy and sort files by extension.')
    parser.add_argument('source_dir', help='Source directory path')
    parser.add_argument('destination_dir', nargs='?', default='dist', help='Destination directory path (default: dist)')
    
    # Parse arguments
    args = parser.parse_args()
    
    source_dir = args.source_dir
    destination_dir = args.destination_dir
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return 1
    
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except Exception as e:
            print(f"Error creating destination directory '{destination_dir}': {e}")
            return 1
    
    print(f"Copying files from '{source_dir}' to '{destination_dir}'...")
    copy_and_sort_files(source_dir, destination_dir)
    print("Done!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
