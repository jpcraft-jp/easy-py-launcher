#!/usr/bin/env python3
import json, sys, subprocess as sub

def main():
    if len(sys.argv) < 3:
        print("Nutzung: ./launcher.py run <command_name>")
        sys.exit(1)

    try:
        with open("./pack.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Fehler: pack.json nicht gefunden.")
        sys.exit(1)

    commands = data.get("commands", {})
    command_name = sys.argv[2]
    command = commands.get(command_name)

    if not command:
        print(f"Fehler: Befehl '{command_name}' nicht in pack.json gefunden.")
        sys.exit(1)

    # Ausführung mit Fehlerbehandlung
    try:
        sub.run(command, shell=True, cwd=data.get("work_dir", "."), check=True)
    except sub.CalledProcessError as e:
        print(f"Befehl '{command_name}' fehlgeschlagen mit Exit-Code {e.returncode}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()