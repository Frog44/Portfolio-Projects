import os
import shutil

def organize_downloads(folder_path):
    # Get the list of files in the Downloads folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Define categories for file types
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".pptx", ".csv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Executables": [".exe", ".msi"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
    }

    # Create subfolders if they don't exist
    for category in categories.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Organize files into subfolders
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()

        # Determine the category of the file
        category_found = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                category_path = os.path.join(folder_path, category)
                shutil.move(os.path.join(folder_path, file), os.path.join(category_path, file))
                print(f"Moved {file} to {category} folder.")
                category_found = True
                break

        # If the file doesn't match any category, move it to "Other" folder
        if not category_found:
            other_path = os.path.join(folder_path, "Other")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(os.path.join(folder_path, file), os.path.join(other_path, file))
            print(f"Moved {file} to Other folder.")

if __name__ == "__main__":
    # Replace with the path to your Downloads folder
    downloads_folder_path = "/Users/Robbie/Downloads"

    organize_downloads(downloads_folder_path)
