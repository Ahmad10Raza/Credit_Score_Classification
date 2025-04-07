import os
from pathlib import Path

def create_empty_project(base_dir="credit_score_app"):
    """Creates the folder structure with empty files"""
    
    # Define the structure (keys are paths, values indicate if it's a file)
    structure = {
        'app/__init__.py': 'file',
        'app/routes.py': 'file',
        'app/ml_model.py': 'file',
        'app/static/': 'dir',
        'app/templates/': 'dir',
        'app/models/': 'dir',
        'app/data/': 'dir',
        'config.py': 'file',
        'run.py': 'file'
    }

    try:
        # Create all directories and files
        for path, type_ in structure.items():
            full_path = Path(base_dir) / path
            
            if type_ == 'dir':
                full_path.mkdir(parents=True, exist_ok=True)
            else:
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.touch()  # Create empty file
            
        print(f"Successfully created project structure at: {Path(base_dir).resolve()}")
        return True
        
    except Exception as e:
        print(f"Error creating structure: {e}")
        return False

if __name__ == '__main__':
    project_name = input("Enter project name (default: credit_score_app): ").strip() or "credit_score_app"
    create_empty_project(project_name)