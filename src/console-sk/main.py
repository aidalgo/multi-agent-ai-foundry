#!/usr/bin/env python3
"""
Console Multi-Agent Custom Automation Engine
A simplified console version of the multi-agent system using Semantic Kernel and Azure AI Foundry.
"""

import asyncio
import logging
import sys
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Environment variables won't be loaded from .env file.")

from azure.identity import DefaultAzureCredential
from console_app import ConsoleMACAE


# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Define available action categories and examples
AVAILABLE_ACTIONS = {
    "HR & Employee Management": [
        "Onboard a new employee (name: John Doe)",
        "Schedule orientation session",
        "Assign mentor to employee",
        "Set up payroll for employee",
        "Process leave request",
        "Schedule performance review",
        "Update employee record",
        "Generate employee directory"
    ],
    "IT & Technical Support": [
        "Set up Office 365 account for employee",
        "Configure laptop for new employee",
        "Reset employee password",
        "Set up VPN access",
        "Install software for employee",
        "Troubleshoot network issues",
        "Handle cybersecurity incident",
        "Configure server or database access"
    ],
    "Marketing & Communications": [
        "Create marketing campaign",
        "Analyze market trends",
        "Generate social media posts",
        "Plan advertising budget",
        "Conduct customer survey",
        "Perform competitor analysis",
        "Schedule marketing event",
        "Create content calendar"
    ],
    "Procurement & Asset Management": [
        "Order hardware (laptops, monitors, etc.)",
        "Order software licenses",
        "Check inventory status",
        "Process purchase order",
        "Track order status",
        "Manage vendor relationships",
        "Handle equipment returns",
        "Schedule maintenance"
    ],
    "Product & Service Management": [
        "Add mobile extras pack to customer plan",
        "Get product information",
        "Modify customer service plan",
        "Check plan eligibility",
        "Process service upgrade/downgrade",
        "Handle customer billing inquiry"
    ]
}


def show_welcome_message():
    """Display the welcome message and available actions."""
    print("=" * 80)
    print("   Multi-Agent Custom Automation Engine - Console")
    print("=" * 80)
    print()
    print("🤖 Welcome to the Multi-Agent AI System!")
    print()
    
    print("📝 Example Requests:")
    print("=" * 50)
    
    examples = [
        "onboard new employee Sarah Johnson",
        "set up office 365 account for mike.smith@company.com",
        "create marketing campaign for product launch",
        "order laptop for new developer",
        "schedule orientation for new hire",
        "reset password for user john.doe",
        "analyze market trends in technology sector",
        "process purchase order for office supplies",
        "configure VPN access for remote employee",
        "create social media posts for holiday promotion"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i:2d}. {example}")
    
    print()
    print("💡 How to use:")
    print("• Type a natural language request (e.g., 'onboard new employee John Smith')")
    print("• Use 'actions' to see all available actions")
    print("• Use 'examples' to see example requests")
    print("• Use 'status' to check current plan status")
    print("• Use 'help' for this message")
    print("• Use 'quit' or 'exit' to exit")
    print()


def show_examples():
    """Show example requests."""
    print("\n📝 Example Requests:")
    print("=" * 50)
    
    examples = [
        "onboard new employee Sarah Johnson",
        "set up office 365 account for mike.smith@company.com",
        "create marketing campaign for product launch",
        "order laptop for new developer",
        "schedule orientation for new hire",
        "reset password for user john.doe",
        "analyze market trends in technology sector",
        "process purchase order for office supplies",
        "configure VPN access for remote employee",
        "create social media posts for holiday promotion"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i:2d}. {example}")
    
    print("\n💡 Just type any of these examples or create your own request!")
    print()


def show_all_actions():
    """Show all available actions in detail."""
    print("\n🛠️  All Available Actions:")
    print("=" * 50)
    
    for category, actions in AVAILABLE_ACTIONS.items():
        print(f"\n🔸 {category}:")
        for action in actions:
            print(f"   • {action}")
    
    print("\n💡 You can request any of these actions in natural language!")
    print("Example: 'I need to onboard a new employee named Alex Wilson'")
    print()


def collect_missing_info(task_description: str) -> str:
    """Pass through function that lets the agent decide what information it needs."""
    # No pre-processing - let the agent handle information gathering dynamically
    return task_description


async def main():
    """Main entry point for the console application."""
    try:
        # Initialize the console application
        console_app = ConsoleMACAE()
        await console_app.initialize()
        
        # Show welcome message
        show_welcome_message()
        
        # Run the interactive console loop
        while True:
            try:
                user_input = input(">> ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit']:
                    print("👋 Goodbye!")
                    break
                    
                if user_input.lower() in ['help']:
                    show_welcome_message()
                    continue
                    
                if user_input.lower() in ['actions', 'list']:
                    show_all_actions()
                    continue
                    
                if user_input.lower() in ['examples', 'example']:
                    show_examples()
                    continue
                    
                if user_input.lower() == 'status':
                    await console_app.show_status()
                    continue
                
                # Let the agent dynamically gather all required information
                # No pre-processing of the task
                task = user_input
                
                # Process the task
                print(f"\n🔄 Processing: {task}")
                print("-" * 60)
                
                # Process the user input as a task
                # The planner agent will identify and request all necessary information
                # through its dynamic parameter analysis and clarification requests
                await console_app.process_task(task)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error processing input: {e}")
                print(f"❌ Error: {e}")
                print("💡 Try typing 'help' for available commands or 'examples' for sample requests.")
        
    except KeyboardInterrupt:
        print("\n👋 Application interrupted by user.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
