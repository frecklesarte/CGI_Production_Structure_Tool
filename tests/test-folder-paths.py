# Determine: How configurations and structures to be generaed between OS
import os
from pathlib import Path

print("The Modules have been initialized")

def create_production_structure(production_name: str, base_path: Path = Path('.')):
    """
    Creates a basic folder structure for 3D production.

    Args:
        production_name: The name of the project. This will be the root directory.
        base_path: The directory where the project will be created. Defaults to current directory.
    """
    production_root = base_path / production_name


    # Define the structure as a list of paths relative to the project root
    structure = [
        "pre-production/",
        "pre-production/__init__.py",
        "pre-production/main.py",
        "pre-production/research-and-development/",
        "pre-production/research-and-development/__init__.py",
        "pre-production/research-and-development/reference-material/",
        "pre-production/research-and-development/reference-material/__init__.py",
        "pre-production/research-and-development/reference-material/animation-references/",
        "pre-production/research-and-development/reference-material/animation-references/__init__.py",
        "pre-production/research-and-development/reference-material/reference-boards/",
        "pre-production/research-and-development/reference-material/reference-boards/__init__.py",
        "pre-production/research-and-development/technical-specifications/",
        "pre-production/research-and-development/technical-specifications/__init__.py",
        "pre-production/writing/",
        "pre-production/writing/__init.py",
        "pre-production/visual-developments/",
        "production/",
        "post-production/",
        ".gitignore",
    ]

    print(f"Creating Production structure '{production_name}' at '{production_root}'...")

    try:
        # Create the root directory
        production_root.mkdir(parents=True, exist_ok=True)
        print(f"Created Production structure: {production_root}")

        # Create subdirectories and files
        for item_path_str in structure:
            # Construct the full path
            full_path = production_root / item_path_str

            # Check if it's a directory or a file
            if item_path_str.endswith('/'):
                # It's a directory
                full_path.mkdir(parents=True, exist_ok=True)
                print(f"    Created directory: {full_path.relative_to(production_root)}")
            else:
                #It's a file, ensure its parent directory
                full_path.parent.mkdir(parents=True, exist_ok=True)
                # Create an empty file
                full_path.touch()
                print(f"    Created files: {full_path.relative_to(production_root)}")

        print(f"Production '{production_name}' structure created successfully!")

    except OSError as e:
        print(f"Error creating production structure: {e}")

if __name__ == "__main__":
    # Example usage:
    # To run this: python test-folder-paths.py production_name
    import sys

    if len(sys.argv) < 2:
        print("Usage: python test-folder-paths.py <production_name>")
        sys.exit(1)

    production_name = sys.argv[1]
    create_production_structure(production_name)
