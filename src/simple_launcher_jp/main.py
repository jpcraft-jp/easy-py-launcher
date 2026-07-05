import sys, json
from .run import run
from .init_wizard import init_wizard
from .activate_venv import activate_venv

def main():
    type_hint = sys.argv[1]
    
    if type_hint == "init":
        init_wizard(sys.argv[2])
        sys.exit(0)
    
    try:
        with open("pypack.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("pypack.json not found, please run 'pyrun init' to create it")
        sys.exit(1)
    
    
    
    if type_hint == "run":
        run(config["scripts"][sys.argv[2]], sys.argv[3:], config.get("codedir", "."))

    if type_hint == "activate":
        activate_venv(config, config.get("workdir", "."))

if __name__ == "__main__":
    main()
    