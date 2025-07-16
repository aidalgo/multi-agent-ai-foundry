#!/usr/bin/env python3
"""
Console SK Launcher
Simple launcher script for the console application.
"""

import sys
import subprocess
import os

def check_requirements():
    """Check if requirements are installed."""
    try:
        import azure.identity
        import semantic_kernel
        import azure.ai.projects
        return True
    except ImportError as e:
        print(f"Missing required packages: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_env():
    """Check if environment is configured."""
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
        if not os.getenv(var):
            missing.append(var)
    
    if missing:
        print("Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease check your .env file or environment configuration.")
        return False
    
    return True

def main():
    """Main launcher function."""
    print("Console Multi-Agent Custom Automation Engine Launcher")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Load environment
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("Warning: python-dotenv not installed. Using system environment variables.")
    
    # Check environment
    if not check_env():
        sys.exit(1)
    
    # Check Azure authentication
    try:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
        print("✅ Azure credentials configured successfully")
    except Exception as e:
        print(f"❌ Azure credential error: {e}")
        print("Please run 'az login' to authenticate with Azure.")
        sys.exit(1)
    
    # Launch the main application
    try:
        print("🚀 Starting console application...")
        print()
        
        # Import and run the main application
        from main import main as app_main
        import asyncio
        
        asyncio.run(app_main())
        
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"❌ Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
