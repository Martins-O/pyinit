Sure! Here’s the updated “How To” guide that includes the new flags and functionalities added to the pyinitpro CLI tool.

⸻

✅ How to Set Up and Use pyinitpro CLI (Cross-Platform Guide)

⸻

📁 1. Clone the project

git clone https://github.com/Martins-O/pyinitpro.git



⸻

🧰 2. Install pipx (if not installed)

macOS or Linux:

brew install pipx   # macOS

python3 -m pip install --user pipx

pipx ensurepath

Windows (via PowerShell):

python -m pip install --user pipx

pipx ensurepath

Restart your terminal after running pipx ensurepath.

⸻

🚀 3. Install pyinitpro using pipx

In the terminal, navigate to the root of your pyinitpro project:

cd pyinitpro

pipx install .

✅ This makes the pyinitpro command available globally.

⸻

✅ 4. Usage

Now you can run pyinitpro from anywhere in your terminal:

pyinitpro

It will prompt you to:
	•	Create a new project or use an existing one:
	•	New project: Asks for the project name, subfolders, etc.
	•	Existing project: Asks for the path and sets up the folders.
	•	Create a Python virtual environment (optional):
	•	You can skip this with the --no-venv flag.
	•	You can specify a Python version with the --python-version flag.
	•	Add dependencies to requirements.txt:
	•	Provide a comma-separated list of dependencies via the --dependencies flag.
	•	If no dependencies are provided, a preconfigured template for requirements.txt will be created.
	•	Initialize a Git repository (optional):
	•	You can choose to initialize a Git repo by answering y when prompted.
	•	If desired, add a remote repository URL with the --git-remote flag.
	•	Interactive Setup (optional):
	•	Enable an interactive setup where you will be prompted for custom folder names by using the --interactive flag.

Example usage with flags:

pyinitpro --interactive --dependencies flask,requests --python-version 3.9 --git-remote https://github.com/your-repo.git



⸻

💡 Notes
	•	To uninstall pyinitpro:

pipx uninstall pyinitpro

    •	For more information, visit the project's GitHub repository: https://github.com/Martins-O/pyinitpro
