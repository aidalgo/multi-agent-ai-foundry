#!/usr/bin/env python3
"""
Test script to verify the console application setup.
"""

import sys
import os
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Environment variables won't be loaded from .env file.")
    print("Install with: pip install python-dotenv")

def test_imports():
    """Test that all required imports work."""
    print("Testing imports...")
    
    try:
        from azure.identity import DefaultAzureCredential
        print("✅ Azure Identity import successful")
    except ImportError as e:
        print(f"❌ Azure Identity import failed: {e}")
        return False
    
    try:
        from config import AppConfig
        print("✅ App Config import successful")
    except ImportError as e:
        print(f"❌ App Config import failed: {e}")
        return False
    
    try:
        from models import AgentType
        print("✅ Models import successful")
    except ImportError as e:
        print(f"❌ Models import failed: {e}")
        return False
    
    try:
        from memory import ConsoleMemoryContext
        print("✅ Console Memory import successful")
    except ImportError as e:
        print(f"❌ Console Memory import failed: {e}")
        return False
    
    try:
        from utils import ConsoleAgentFactory
        print("✅ Console Utils import successful")
    except ImportError as e:
        print(f"❌ Console Utils import failed: {e}")
        return False
    
    return True

def test_env_setup():
    """Test environment setup."""
    print("\nTesting environment setup...")
    
    required_vars = [
        'AZURE_OPENAI_ENDPOINT',
        'AZURE_OPENAI_DEPLOYMENT_NAME',
        'AZURE_AI_SUBSCRIPTION_ID',
        'AZURE_AI_RESOURCE_GROUP',
        'AZURE_AI_PROJECT_NAME',
        'AZURE_AI_AGENT_ENDPOINT'
    ]
    
    missing = []
    for var in required_vars:
        if os.getenv(var):
            print(f"✅ {var} is set")
        else:
            print(f"❌ {var} is missing")
            missing.append(var)
    
    if missing:
        print(f"\nMissing environment variables: {missing}")
        print("Please set these in your .env file or environment")
        return False
    
    return True

def test_azure_auth():
    """Test Azure authentication."""
    print("\nTesting Azure authentication...")
    
    try:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
        print("✅ DefaultAzureCredential created successfully")
        return True
    except Exception as e:
        print(f"❌ Azure authentication failed: {e}")
        print("Please run 'az login' to authenticate with Azure")
        return False

def main():
    """Run all tests."""
    print("Console MACAE Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_env_setup,
        test_azure_auth,
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nResults: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("✅ All tests passed! Console application should work.")
        return True
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
