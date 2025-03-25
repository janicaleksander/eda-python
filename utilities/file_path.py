from pathlib import Path

def path_to_file():
    project_root = Path(__file__).resolve().parent.parent
    return project_root / "dataset.csv"

if __name__ == '__main__':
    path_to_file()
