import os
import shutil

# Define project folders (Modify as needed)
PROJECTS = [
    "FBP1", "FBP2", "FBP3", "FBP4", "FBP5",
    "INP1", "INP2", "INP3", "INP4", "INP5"
]

# Base directory where projects are located
BASE_DIR = "../project_files"  # Change this to your actual path

# Destination folder
READY_DIR = os.path.join(BASE_DIR, "../READY")

# Ensure READY folder exists
os.makedirs(READY_DIR, exist_ok=True)

def collect_files():
    for project in PROJECTS:
        project_src = os.path.join(BASE_DIR, project, "src", "posts")
        project_ready = os.path.join(READY_DIR, project)

        # Ensure project-specific READY folder exists
        os.makedirs(project_ready, exist_ok=True)

        if os.path.exists(project_src) and os.path.isdir(project_src):
            for file_name in os.listdir(project_src):
                file_path = os.path.join(project_src, file_name)

                if os.path.isfile(file_path):  # Only process files
                    dest_path = os.path.join(project_ready, file_name)

                    # Move the file to the READY folder
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {file_path} → {dest_path}")

        else:
            print(f"Skipping {project} (No src/posts folder found)")

if __name__ == "__main__":
    collect_files()
    print("\n✅ File collection completed!")
