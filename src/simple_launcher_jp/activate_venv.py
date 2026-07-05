import sys
import pathlib

def activate_venv(config, work_dir):
    venv_rel_path = config.get("venv")
    if not venv_rel_path:
        print("echo 'No virtual environment found. Run pyrun init first.'", file=sys.stderr)
        return

    venv_path = pathlib.Path(work_dir) / venv_rel_path
    
    if not venv_path.exists():
        print(f"echo 'Venv not found at {venv_path}.'", file=sys.stderr)
        return

    # Pfad zum activate Skript
    if sys.platform == "win32":
        activate_script = venv_path / "Scripts" / "activate.bat"
        # Windows Batch Aktivierung
        print(f"{activate_script}")
    else:
        # Linux/macOS
        activate_script = venv_path / "bin" / "activate"
        # WICHTIG: Hier geben wir den 'source' Befehl aus
        print(f"source {activate_script}")