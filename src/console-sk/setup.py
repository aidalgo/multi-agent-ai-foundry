#!/usr/bin/env python3
"""
Setup script for the Console Multi-Agent Custom Automation Engine.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install required dependencies."""
    print("Installing dependencies...")
    
    try:
        # Install requirements
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, cwd=Path(__file__).parent)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_azure_cli():
    """Check if Azure CLI is installed."""
    print("Checking Azure CLI...")
    
    try:
        result = subprocess.run(["az", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Azure CLI is installed")
            return True
        else:
            print("❌ Azure CLI is not working properly")
            return False
    except FileNotFoundError:
        print("❌ Azure CLI is not installed")
        print("Please install Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli")
        return False

def check_environment():
    """Check environment setup."""
    print("Checking environment setup...")
    
    env_file = Path(__file__).parent / ".env"
    
    if env_file.exists():
        print("✅ .env file found")
        return True
    else:
        print("❌ .env file not found")
        print("Please create a .env file based on .env.example")
        return False

def main():
    """Main setup function."""
    print("Console MACAE Setup")
    print("=" * 40)
    
    # Change to the script directory
    os.chdir(Path(__file__).parent)
    
    steps = [
        ("Install dependencies", install_dependencies),
        ("Check Azure CLI", check_azure_cli),
        ("Check environment", check_environment),
    ]
    
    passed = 0
    for step_name, step_func in steps:
        print(f"\n{step_name}...")
        if step_func():
            passed += 1
    
    print(f"\nSetup Results: {passed}/{len(steps)} steps completed")
    
    if passed == len(steps):
        print("\n✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Run 'az login' to authenticate with Azure")
        print("2. Configure your .env file with Azure credentials")
        print("3. Run 'python test_setup.py' to verify everything works")
        print("4. Run 'python main.py' to start the console application")
        return True
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
