"""
Console Multi-Agent Custom Automation Engine
Main application class extracted from main.py for better organization.
"""

import asyncio
import logging
import uuid
from typing import Dict, Optional

from config import AppConfig
from memory import ConsoleMemoryContext
from models import (
    AgentType,
    InputTask,
    StepStatus,
)
from utils import ConsoleAgentFactory, ConsoleUtils

logger = logging.getLogger(__name__)


class ConsoleMACAE:
    """Console Multi-Agent Custom Automation Engine."""
    
    def __init__(self):
        """Initialize the console application."""
        self.config = AppConfig()
        self.session_id = str(uuid.uuid4())
        self.user_id = "console_user"
        self.memory_store = None
        self.agents = {}
        self.planner_agent = None
        self.group_chat_manager = None
        self.current_plan = None
        
    async def initialize(self):
        """Initialize the console application."""
        try:
            # Initialize memory store
            self.memory_store = ConsoleMemoryContext(self.session_id, self.user_id)
            
            # Create all agents
            logger.info("Creating agents...")
            self.agents = await ConsoleAgentFactory.create_all_agents(
                session_id=self.session_id,
                user_id=self.user_id,
                memory_store=self.memory_store
            )
            
            # Get specific agents
            self.planner_agent = self.agents.get(AgentType.PLANNER.value)
            self.group_chat_manager = self.agents.get(AgentType.GROUP_CHAT_MANAGER.value)
            
            logger.info("Console MACAE initialized successfully!")
            
        except Exception as e:
            logger.error(f"Failed to initialize console application: {e}")
            raise
    
    async def run(self):
        """This method is no longer used as the main loop is handled in main.py"""
        pass
    
    async def show_status(self):
        """Show current plan status."""
        if not self.current_plan:
            print("No active plan.")
            return
            
        plan = await self.memory_store.get_plan(self.current_plan.id)
        if not plan:
            print("No active plan found.")
            return
            
        steps = await self.memory_store.get_steps_for_plan(plan.id)
        
        print(f"\nCurrent Plan: {plan.initial_goal}")
        print(f"Status: {plan.overall_status}")
        print(f"Steps: {len(steps)}")
        
        for i, step in enumerate(steps, 1):
            status_emoji = ConsoleUtils.format_step_status(step.status.value)
            agent_name = ConsoleUtils.format_agent_name(step.agent.value)
            print(f"  {i}. {status_emoji} {agent_name}: {step.action}")
        print()
    
    async def process_task(self, task: str):
        """Process a user task."""
        print(f"\nProcessing task: {task}")
        print("-" * 50)
        
        try:
            # Create input task
            input_task = InputTask(
                session_id=self.session_id,
                description=task
            )
            
            # Send to Planner Agent first to create the plan
            print("🤖 Sending task to Planner Agent...")
            
            # Check if Planner Agent exists
            if not self.planner_agent:
                print("❌ Planner Agent not available!")
                return
                
            # Let the planner create the plan first
            plan_response = await self.planner_agent.handle_input_task(input_task)
            
            if plan_response:
                print("✅ Plan created successfully!")
                
                # Get the created plan
                self.current_plan = await self.memory_store.get_latest_plan(
                    self.session_id, self.user_id
                )
                
                if self.current_plan:
                    print(f"\n📋 Plan: {self.current_plan.initial_goal}")
                    print(f"Status: {self.current_plan.overall_status}")
                    
                    # Get steps
                    steps = await self.memory_store.get_steps_for_plan(self.current_plan.id)
                    print(f"Steps ({len(steps)}):")
                    
                    for i, step in enumerate(steps, 1):
                        agent_name = ConsoleUtils.format_agent_name(step.agent.value)
                        truncated_action = ConsoleUtils.truncate_text(step.action, 80)
                        print(f"  {i}. {agent_name}: {truncated_action}")
                    
                    # Ask for approval to execute
                    print("\n" + "="*50)
                    approve = input("Do you want to execute this plan? (y/n): ").lower()
                    
                    if approve in ['y', 'yes']:
                        # Now use GroupChatManager to handle the execution
                        await self.start_group_chat_execution()
                    else:
                        print("Plan execution cancelled.")
                else:
                    print("❌ Could not retrieve created plan.")
            else:
                print("❌ Failed to create plan.")
                
        except Exception as e:
            logger.error(f"Error processing task: {e}")
            print(f"❌ Error: {e}")
    
    async def start_group_chat_execution(self):
        """Start the group chat execution loop where GroupChatManager stays in control."""
        if not self.current_plan:
            print("No plan to execute.")
            return
            
        print("\n🚀 Starting GroupChatManager execution loop...")
        print("-" * 50)
        
        try:
            # Check if GroupChatManager is available
            if not self.group_chat_manager:
                print("❌ GroupChatManager not available!")
                return
                
            # Let GroupChatManager handle the entire execution workflow
            print("🤖 GroupChatManager taking control of execution...")
            
            # Execute the plan through GroupChatManager
            await self.group_chat_manager.execute_plan(self.current_plan)
            
            # Check if all steps are completed
            steps = await self.memory_store.get_steps_for_plan(self.current_plan.id)
            incomplete_steps = [step for step in steps if step.status not in [StepStatus.completed, StepStatus.rejected]]
            
            if incomplete_steps:
                print(f"\n⏳ {len(incomplete_steps)} steps still in progress...")
                print("GroupChatManager will continue managing execution...")
                
                # Here you could implement a loop to check for completion
                # or wait for human feedback if needed
                while incomplete_steps:
                    # Wait a bit and check again
                    await asyncio.sleep(2)
                    steps = await self.memory_store.get_steps_for_plan(self.current_plan.id)
                    incomplete_steps = [step for step in steps if step.status not in [StepStatus.completed, StepStatus.rejected]]
                    
                    if len(incomplete_steps) == 0:
                        break
                        
                    # Show progress
                    completed_count = len(steps) - len(incomplete_steps)
                    print(f"📊 Progress: {completed_count}/{len(steps)} steps completed")
            
            # Final status update
            print("\n" + "="*50)
            print("✅ GroupChatManager execution completed!")
            await self.show_status()
            
        except Exception as e:
            logger.error(f"Error in group chat execution: {e}")
            print(f"❌ Error: {e}")
