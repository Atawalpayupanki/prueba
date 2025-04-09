import subprocess
import os
import sys

# Nombre del entorno virtual
env_name = ".venv"

# Crear el entorno virtual
subprocess.run([sys.executable, "-m", "venv", env_name])
print(f"Entorno virtual '{env_name}' creado.")

activate_script = os.path.join(env_name, "Scripts", "activate")

subprocess.run([sys.executable, "-m", "venv", env_name])
repositorio="nigeria"
comandos = [
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "first commit"],
    ["git", "branch", "-M", "main"],
    ["git", "remote", "add", "origin", f"https://github.com/Atawalpayupanki/{repositorio}"],
    ["git", "push", "-u", "origin", "main"]
]
for comando in comandos:
    subprocess.run(comando)
