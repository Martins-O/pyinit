# pyinit_enhanced.py
import os
import platform
import subprocess
from pathlib import Path
from colorama import Fore, Style, init
import argparse

init()  # Initialize colorama

def parse_args():
    parser = argparse.ArgumentParser(description="Python Project Initializer")
    parser.add_argument('--no-venv', action='store_true', help='Skip creating virtual environment')
    return parser.parse_args()

def prompt_folder_creation():
    folders = []
    print("📁 Let's set up your project structure.")
    while True:
        name = input("Enter folder/subfolder name (or just press Enter to finish): ").strip()
        if not name:
            break
        folders.append(name)
    return folders

def create_project_structure(project_path, folders):
    for folder in folders:
        full_path = project_path / folder
        full_path.mkdir(parents=True, exist_ok=True)
        print(Fore.CYAN + f"📁 Created: {full_path}" + Style.RESET_ALL)

def create_files(project_path):
    (project_path / "requirements.txt").touch()
    with open(project_path / ".gitignore", "w") as f:
        f.write("""# Python
__pycache__/
*.py[cod]
.venv/
.env
""")
    with open(project_path / "main.py", "w") as f:
        f.write("""def main():
    print('Hello, world!')

if __name__ == '__main__':
    main()
""")
    print(Fore.GREEN + "✅ Basic files created." + Style.RESET_ALL)

def create_venv(project_path):
    venv_path = project_path / ".venv"
    subprocess.run(["python3" if platform.system() != "Windows" else "python", "-m", "venv", str(venv_path)])
    return venv_path

def activate_virtual_env(venv_path: Path):
    system = platform.system()
    print("\n⚡ Virtual environment created.")
    if system == "Windows":
        activate_script = venv_path / "Scripts" / "activate.bat"
        os.system(f'start cmd /K "{activate_script}"')
    elif system == "Darwin":
        activate_script = venv_path / "bin" / "activate"
        print(f"\n📝 To activate the virtual environment on macOS, run:\n\n    source {activate_script}\n")
    elif system == "Linux":
        activate_script = venv_path / "bin" / "activate"
        if os.system("which gnome-terminal > /dev/null 2>&1") == 0:
            os.system(f'gnome-terminal -- bash -c "source {activate_script}; exec bash"')
        else:
            print(f"\n📝 To activate the virtual environment, run:\n\n    source {activate_script}\n")
    else:
        print("❗ Unsupported OS for auto-activation. Please activate manually.")

def init_git(project_path):
    try:
        subprocess.run(["git", "init"], cwd=project_path)
        print(Fore.YELLOW + "📘 Git repository initialized." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Git init failed: {e}" + Style.RESET_ALL)

def main():
    args = parse_args()

    project_name = input("📝 Enter project name: ").strip()
    if not project_name:
        print("❌ Project name cannot be empty.")
        return

    project_path = Path.cwd() / project_name
    project_path.mkdir(parents=True, exist_ok=True)

    folders = prompt_folder_creation()
    create_project_structure(project_path, folders)
    create_files(project_path)

    if not args.no_venv:
        venv_path = create_venv(project_path)
        activate_virtual_env(venv_path)

    git_choice = input("📘 Do you want to initialize a Git repository? (y/n): ").lower().strip()
    if git_choice == 'y':
        init_git(project_path)

    print(Fore.GREEN + f"\n✅ Project '{project_name}' initialized successfully!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()