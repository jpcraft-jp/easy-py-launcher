import sys, subprocess


def run(command, args, workdir="."):
    try:
        full_command = ""
        if args:
            full_command = f"{command} {' '.join(args)}"
        else:
            full_command = command
        print(f"DEBUG: full_command = '{full_command}'")
        print(f"DEBUG: workdir = '{workdir}'")
        subprocess.run(full_command, shell=True, cwd=workdir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Befehl '{command}' mit Argumenten {args} fehlgeschlagen mit Exit-Code {e.returncode}")
        sys.exit(e.returncode)
    

if __name__ == "__main__":
    run(sys.argv[2], sys.argv[3:], ".")