import os
import subprocess

def build():

    if not os.path.exists("venv"):
        print("Criando venv...")
        subprocess.run(["python", "-m", "venv", "venv"])

    pip = "venv/Scripts/pip"
    pyinstaller = "venv/Scripts/pyinstaller"

    print("Instalando dependências...")
    subprocess.run([pip, "install", "-r", "requirements.txt"])

    print("Gerando installer...")

    subprocess.run([
        pyinstaller,
        "--onefile",
        "--distpath", "installer",
        "serial_logger.py"
    ])

if __name__ == "__main__":
    build()