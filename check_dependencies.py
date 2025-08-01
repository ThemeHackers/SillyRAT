#!/usr/bin/env python3
"""
Dependency Checker for SillyRAT
This script checks which dependencies are missing and provides installation instructions
"""

import sys
import importlib

def check_dependency(package_name, install_name=None):
    """Check if a package is available"""
    if install_name is None:
        install_name = package_name
    
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name} - Install with: pip install {install_name}")
        return False

def main():
    print("🔍 SillyRAT Dependency Checker")
    print("=" * 40)
    
    dependencies = [
        ("platform", None),  # Built-in
        ("psutil", "psutil"),
        ("tabulate", "tabulate"),
        ("pynput", "pynput"),
        ("pyscreenshot", "pyscreenshot"),
        ("pyperclip", "pyperclip"),
        ("cv2", "opencv-python"),
        ("PIL", "pillow"),
        ("numpy", "numpy"),
        ("threading", None),  # Built-in
        ("subprocess", None),  # Built-in
        ("os", None),  # Built-in
        ("sys", None),  # Built-in
        ("time", None),  # Built-in
        ("datetime", None),  # Built-in
        ("base64", None),  # Built-in
        ("socket", None),  # Built-in
        ("io", None),  # Built-in
    ]
    
    missing_count = 0
    total_count = len(dependencies)
    
    for package, install_name in dependencies:
        if not check_dependency(package, install_name):
            missing_count += 1
    
    print("\n" + "=" * 40)
    print(f"📊 SUMMARY")
    print(f"Total dependencies: {total_count}")
    print(f"Available: {total_count - missing_count}")
    print(f"Missing: {missing_count}")
    
    if missing_count > 0:
        print(f"\n🔧 To install missing dependencies, run:")
        print("pip install psutil tabulate pynput pyscreenshot pyperclip opencv-python pillow numpy")
    else:
        print(f"\n🎉 All dependencies are available!")
    
    return missing_count == 0

if __name__ == "__main__":
    main() 