import pathlib, json, venv, subprocess, os
import sys

init_file_content_template = {
    "name": "",
    "version": "",
    "author": "",
    "description": "",
    "workdir": "",
    "scripts": {},
    "dependencies": [],
    "venv": ""
}

def init_wizard(work_dir="."):
    print("welcome to the init wizard")
    work_dir = pathlib.Path(work_dir)
    
    if not work_dir.exists():
        work_dir.mkdir(parents=True)
    
    if work_dir.is_file():
        print(f"work dir {work_dir} is a file, cannot create init file")
        return
    
    init_file = work_dir / "pypack.json"
    
    if init_file.exists():
        print(f"init file {init_file} already exists, skipping creation")
        return

    init_file_content = init_file_content_template.copy()
    print("please enter the following information for your project:")
    init_file_content["name"] = input("Name: ")
    init_file_content["version"] = input("Version: ")
    init_file_content["author"] = input("Author: ")
    init_file_content["description"] = input("Description: ")
    print("code directory is the directory where your code is located, relative to the work dir")
    init_file_content["codedir"] = input("Code directory : ")
    deps = input("Dependencies (kommagetrennt): ")
    init_file_content["dependencies"] = [d.strip() for d in deps.split(",")] if deps else []
    init_file_content["scripts"] = {"test": f"{input('Test command: ')}"}
    
    
    
    code_dir = work_dir / init_file_content["codedir"]
    if not code_dir.exists():
        code_dir.mkdir(parents=True)
    
    print(f"init file created at {init_file}")
    vanv = input("Do you want to create a virtual environment? default yes (y/n) : ")
    if vanv.lower() == "y" or vanv.lower() == "":
        venv_dir = work_dir / "venv"
        if not venv_dir.exists():
            print(f"creating virtual environment at {venv_dir}")
            venv.create(venv_dir, with_pip=True)
            print(f"virtual environment created at {venv_dir}")
        init_file_content["venv"] = "venv"
    
    pre_install = input("Do you want to install dependencies now? default yes (y/n): ")
    if pre_install.lower() == "y" or pre_install.lower() == "":
        if init_file_content["venv"]:
            if init_file_content["venv"]:
                if os.name == "nt":
                    pip_path = pathlib.Path(work_dir) / init_file_content["venv"] / "Scripts" / "pip.exe"
                else:
                    pip_path = pathlib.Path(work_dir) / init_file_content["venv"] / "bin" / "pip"
                    
                if not pip_path.exists():
                    print(f"pip not found at {pip_path}, cannot install dependencies")
                    return
                for dep in init_file_content["dependencies"]:
                    print(f"installing dependency {dep}")
                    subprocess.run([str(pip_path), "install", dep], check=True)
            else:
                print("no virtual environment found, installing dependencies globally")
                for dep in init_file_content["dependencies"]:
                    print(f"installing dependency {dep}")
                    subprocess.run(["pip", "install", dep], check=True)
    
    with open(init_file, "w") as f:
        json.dump(init_file_content, f, indent=4)
    
if __name__ == "__main__":
    init_wizard(sys.argv[2])