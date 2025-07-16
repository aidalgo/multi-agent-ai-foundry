"""
Console Agent Factory - Simplified agent creation for console application.
This uses the existing agent implementations but with simplified initialization.
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Type

# Add the backend directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional for this module

from console_memory import ConsoleMemoryContext
from backend.models.messages_kernel import AgentType

logger = logging.getLogger(__name__)


class ConsoleAgentFactory:
    """Factory for creating agents in the console application."""
    
    @classmethod
    async def create_all_agents(
        cls,
        session_id: str,
        user_id: str,
        memory_store: Optional[ConsoleMemoryContext] = None,
        temperature: float = 0.0,
    ) -> Dict[str, Any]:
        """Create all agents for a session.
        
        Args:
            session_id: The session identifier
            user_id: The user identifier
            memory_store: Optional memory store (will create if not provided)
            temperature: Temperature for agent responses
            
        Returns:
            Dictionary of agent instances mapped by their names
        """
        
        if memory_store is None:
            memory_store = ConsoleMemoryContext(session_id, user_id)
        
        agents = {}
        
        # Import agent classes
        try:
            from backend.kernel_agents.hr_agent import HrAgent
            from backend.kernel_agents.marketing_agent import MarketingAgent
            from backend.kernel_agents.product_agent import ProductAgent
            from backend.kernel_agents.procurement_agent import ProcurementAgent
            from backend.kernel_agents.tech_support_agent import TechSupportAgent
            from backend.kernel_agents.generic_agent import GenericAgent
            from backend.kernel_agents.human_agent import HumanAgent
            from backend.kernel_agents.planner_agent import PlannerAgent
            from backend.kernel_agents.group_chat_manager import GroupChatManager
            
            # Create AI project client for agent creation
            from backend.app_config import config
            ai_project_client = config.get_ai_project_client()
            
            # Agent creation mapping
            agent_classes = {
                AgentType.HR: HrAgent,
                AgentType.MARKETING: MarketingAgent,
                AgentType.PRODUCT: ProductAgent,
                AgentType.PROCUREMENT: ProcurementAgent,
                AgentType.TECH_SUPPORT: TechSupportAgent,
                AgentType.GENERIC: GenericAgent,
                AgentType.HUMAN: HumanAgent,
                AgentType.PLANNER: PlannerAgent,
                AgentType.GROUP_CHAT_MANAGER: GroupChatManager,
            }
            
            # Create agents
            for agent_type, agent_class in agent_classes.items():
                try:
                    logger.info(f"Creating {agent_type.value} agent...")
                    
                    # Special handling for planner agent which needs additional parameters
                    if agent_type == AgentType.PLANNER:
                        agent = await agent_class.create(
                            session_id=session_id,
                            user_id=user_id,
                            memory_store=memory_store,
                            agent_name=agent_type.value,
                            client=ai_project_client,
                            system_message=agent_class.default_system_message(agent_type.value),
                            tools=None,  # Let the agent load its own tools
                            available_agents=list(AgentType),
                            agent_instances=None,  # Will be populated after all agents are created
                        )
                    elif agent_type == AgentType.GROUP_CHAT_MANAGER:
                        agent = await agent_class.create(
                            session_id=session_id,
                            user_id=user_id,
                            memory_store=memory_store,
                            agent_name=agent_type.value,
                            client=ai_project_client,
                            system_message=agent_class.default_system_message(agent_type.value),
                            tools=None,  # Let the agent load its own tools
                            agent_tools_list=[],  # Empty list for console
                            agent_instances=None,  # Will be populated after all agents are created
                        )
                    else:
                        # Create agent using the class's create method
                        agent = await agent_class.create(
                            session_id=session_id,
                            user_id=user_id,
                            memory_store=memory_store,
                            agent_name=agent_type.value,
                            client=ai_project_client,
                            system_message=agent_class.default_system_message(agent_type.value),
                            tools=None,  # Let the agent load its own tools
                        )
                    
                    if agent:
                        agents[agent_type.value] = agent
                        logger.info(f"Created {agent_type.value} agent successfully")
                    else:
                        logger.warning(f"Failed to create {agent_type.value} agent")
                        
                except Exception as e:
                    logger.error(f"Error creating {agent_type.value} agent: {e}")
                    continue
            
            # Update agent instances for planner and group chat manager
            if agents:
                planner_agent = agents.get(AgentType.PLANNER.value)
                if planner_agent:
                    planner_agent._agent_instances = agents
                    
                group_chat_manager = agents.get(AgentType.GROUP_CHAT_MANAGER.value)
                if group_chat_manager:
                    group_chat_manager._agent_instances = agents
            
            logger.info(f"Created {len(agents)} agents successfully")
            return agents
            
        except Exception as e:
            logger.error(f"Error creating agents: {e}")
            raise


class ConsoleUtils:
    """Utility functions for console application."""
    
    @staticmethod
    def format_agent_response(response: str) -> str:
        """Format agent response for console display."""
        if not response:
            return ""
        
        # Remove markdown formatting for console display
        response = response.replace("**", "")
        response = response.replace("*", "")
        response = response.replace("# ", "")
        response = response.replace("## ", "")
        response = response.replace("### ", "")
        
        return response.strip()
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        """Truncate text to a maximum length."""
        if len(text) <= max_length:
            return text
        return text[:max_length - 3] + "..."
    
    @staticmethod
    def format_step_status(status: str) -> str:
        """Format step status for console display."""
        status_symbols = {
            "planned": "⏳",
            "awaiting_feedback": "⏸️",
            "approved": "✅",
            "rejected": "❌",
            "action_requested": "🔄",
            "completed": "✅",
            "failed": "❌",
        }
        return status_symbols.get(status, "❓")
    
    @staticmethod
    def format_agent_name(agent_type: str) -> str:
        """Format agent name for console display."""
        agent_names = {
            "Hr_Agent": "HR Agent",
            "Marketing_Agent": "Marketing Agent",
            "Product_Agent": "Product Agent",
            "Procurement_Agent": "Procurement Agent",
            "Tech_Support_Agent": "Tech Support Agent",
            "Generic_Agent": "Generic Agent",
            "Human_Agent": "Human Agent",
            "Planner_Agent": "Planner Agent",
            "Group_Chat_Manager": "Group Chat Manager",
        }
        return agent_names.get(agent_type, agent_type)
