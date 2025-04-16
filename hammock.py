#!/usr/bin/env python3

import os
import sys
import subprocess
import ast
import importlib.util
from pathlib import Path
import shutil

VENV_DIR = ".venv"
PYTHON_EXEC = "python3"

def print_bold(text):
    print(f"\033[1m{text}\033[0m")

def venv_exists():
    return Path(VENV_DIR).exists()

def create_venv():
    print_bold("🔧 Creating virtual environment...")
    subprocess.run([PYTHON_EXEC, "-m", "venv", VENV_DIR], check=True)

    # 🩹 Fix for macOS/Python 3.13 missing pip: explicitly install pip if needed
    pip_path = Path(VENV_DIR) / "bin" / "pip"
    if not pip_path.exists():
        print_bold("🛠️  Pip not found in venv. Running ensurepip...")
        subprocess.run([f"./{VENV_DIR}/bin/python", "-m", "ensurepip", "--upgrade"], check=True)

def get_venv_python():
    return f"./{VENV_DIR}/bin/python"

def get_venv_pip():
    return f"./{VENV_DIR}/bin/pip"

def extract_imports(script_path):
    with open(script_path, "r") as f:
        node = ast.parse(f.read(), filename=script_path)
    imports = set()
    for item in ast.walk(node):
        if isinstance(item, ast.Import):
            for alias in item.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(item, ast.ImportFrom):
            if item.module:
                imports.add(item.module.split('.')[0])
    return sorted(list(imports))

def is_builtin_module(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec is not None and (
        module_name in sys.builtin_module_names or
        "site-packages" not in spec.origin
    )

def install_missing_modules(modules):
    pip_path = get_venv_pip()
    for mod in modules:
        if not importlib.util.find_spec(mod):
            print_bold(f"📦 Installing missing module: {mod}")
            subprocess.run([pip_path, "install", mod], check=False)

def run_script(script_path, args):
    cmd = [get_venv_python(), script_path] + args
    print_bold(f"🚀 Running: {' '.join(cmd)}")
    subprocess.run(cmd)

def cleanup_venv():
    if Path(VENV_DIR).exists():
        print_bold("🧹 Cleaning up virtual environment...")
        shutil.rmtree(VENV_DIR)

def main():
    if len(sys.argv) < 2:
        print("Usage: hammock.py <your_script.py> [args]")
        sys.exit(1)

    script_path = sys.argv[1]
    script_args = sys.argv[2:]

    if not Path(script_path).exists():
        print(f"❌ Script not found: {script_path}")
        sys.exit(1)

    try:
        if not venv_exists():
            create_venv()

        all_imports = extract_imports(script_path)
        external_modules = [m for m in all_imports if not is_builtin_module(m)]

        if external_modules:
            print_bold("🔍 External modules found:")
            for mod in external_modules:
                print(f" - {mod}")
            install_missing_modules(external_modules)
        else:
            print_bold("✅ No external modules found to install.")

        run_script(script_path, script_args)

    finally:
        cleanup_venv()

if __name__ == "__main__":
    main()
