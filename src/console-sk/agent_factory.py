"""
Agent Factory for the console application.
Handles creation and initialization of all agent types.
"""

import logging
from typing import Any, Dict, Optional

from config import config
from models import AgentType

logger = logging.getLogger(__name__)


class ConsoleAgentFactory:
    """Factory for creating agents in the console application."""
    
    @classmethod
    async def create_all_agents(
        cls,
        session_id: str,
        user_id: str,
        memory_store: Optional[Any] = None,
        temperature: float = 0.0,
    ) -> Dict[str, Any]:
        """
        Create all agents for a session.
        
        Args:
            session_id: Unique session identifier
            user_id: User identifier
            memory_store: Memory context for agents (optional)
            temperature: Temperature setting for AI models
            
        Returns:
            Dictionary of created agents keyed by agent type
        """
        
        if memory_store is None:
            from memory import ConsoleMemoryContext
            memory_store = ConsoleMemoryContext(session_id, user_id)
        
        agents = {}
        
        # Import agent classes
        try:
            from agents.hr_agent import HrAgent
            from agents.marketing_agent import MarketingAgent
            from agents.product_agent import ProductAgent
            from agents.procurement_agent import ProcurementAgent
            from agents.tech_support_agent import TechSupportAgent
            from agents.generic_agent import GenericAgent
            from agents.human_agent import HumanAgent
            from agents.planner_agent import PlannerAgent
            from agents.group_chat_manager import GroupChatManager
            
            # Create AI project client for agent creation
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
            
            # Create agents using the factory methods
            for agent_type, agent_class in agent_classes.items():
                try:
                    logger.info(f"Creating {agent_type.value} agent...")
                    
                    agent = await cls._create_single_agent(
                        agent_type=agent_type,
                        agent_class=agent_class,
                        session_id=session_id,
                        user_id=user_id,
                        memory_store=memory_store,
                        ai_project_client=ai_project_client
                    )
                    
                    if agent:
                        agents[agent_type.value] = agent
                        logger.info(f"Created {agent_type.value} agent successfully")
                    else:
                        logger.warning(f"Failed to create {agent_type.value} agent")
                        
                except Exception as e:
                    logger.error(f"Error creating {agent_type.value} agent: {e}")
                    continue
            
            # Post-creation setup: Update agent instances for coordination
            cls._setup_agent_coordination(agents)
            
            logger.info(f"Created {len(agents)} agents successfully")
            return agents
            
        except Exception as e:
            logger.error(f"Error creating agents: {e}")
            raise

    @classmethod
    async def _create_single_agent(
        cls,
        agent_type: AgentType,
        agent_class,
        session_id: str,
        user_id: str,
        memory_store: Any,
        ai_project_client: Any
    ):
        """Create a single agent with type-specific parameters."""
        
        base_params = {
            "session_id": session_id,
            "user_id": user_id,
            "memory_store": memory_store,
            "agent_name": agent_type.value,
            "client": ai_project_client,
            "system_message": agent_class.default_system_message(agent_type.value),
            "tools": None,  # Let the agent load its own tools
        }
        
        # Special handling for planner agent which needs additional parameters
        if agent_type == AgentType.PLANNER:
            base_params.update({
                "available_agents": list(AgentType),
                "agent_instances": None,  # Will be populated after all agents are created
            })
            
        elif agent_type == AgentType.GROUP_CHAT_MANAGER:
            base_params.update({
                "agent_tools_list": [],  # Empty list for console
                "agent_instances": None,  # Will be populated after all agents are created
            })
        
        return await agent_class.create(**base_params)

    @classmethod
    def _setup_agent_coordination(cls, agents: Dict[str, Any]) -> None:
        """Set up coordination between agents after all are created."""
        if not agents:
            return
            
        # Update agent instances for planner and group chat manager
        planner_agent = agents.get(AgentType.PLANNER.value)
        if planner_agent:
            planner_agent._agent_instances = agents
            logger.debug("Updated planner agent with agent instances")
            
        group_chat_manager = agents.get(AgentType.GROUP_CHAT_MANAGER.value)
        if group_chat_manager:
            group_chat_manager._agent_instances = agents
            logger.debug("Updated group chat manager with agent instances")

    @classmethod
    def get_available_agent_types(cls) -> list[AgentType]:
        """Get list of all available agent types."""
        return list(AgentType)

    @classmethod
    def get_agent_class_mapping(cls) -> Dict[AgentType, type]:
        """Get mapping of agent types to their classes."""
        from agents.hr_agent import HrAgent
        from agents.marketing_agent import MarketingAgent
        from agents.product_agent import ProductAgent
        from agents.procurement_agent import ProcurementAgent
        from agents.tech_support_agent import TechSupportAgent
        from agents.generic_agent import GenericAgent
        from agents.human_agent import HumanAgent
        from agents.planner_agent import PlannerAgent
        from agents.group_chat_manager import GroupChatManager
        
        return {
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
