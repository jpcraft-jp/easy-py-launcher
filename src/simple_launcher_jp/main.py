import sys, json
from .run import run
from .init_wizard import init_wizard




def main():
    type_hint = sys.argv[1]
    
    if type_hint == "init":
        init_wizard(sys.argv[2])
    
    try:
        with open("pypack.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("pypack.json not found, please run 'pyrun init' to create it")
        sys.exit(1)
    
    
    
    if type_hint == "run":
        run(config["scripts"][sys.argv[2]], sys.argv[3:], config.get("workdir", "."))

    if type_hint == "activate":
        venv_path = config.get("venv")
        if not venv_path:
            print("No virtual environment found in pypack.json, please run 'pyrun init' to create it")
            sys.exit(1)
        if sys.platform == "win32":
            activate_script = f"{venv_path}\\Scripts\\activate"
        else:
            activate_script = f"{venv_path}/bin/activate"
        print(f"To activate the virtual environment, run: source ./{activate_script}")

if __name__ == "__main__":
    main()
    