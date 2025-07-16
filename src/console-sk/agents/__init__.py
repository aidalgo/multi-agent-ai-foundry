"""
Agent classes for the console multi-agent system.
"""

from agents.base_agent import BaseAgent
from .planner_agent import PlannerAgent
from .group_chat_manager import GroupChatManager
from .hr_agent import HrAgent
from .marketing_agent import MarketingAgent
from .product_agent import ProductAgent
from .procurement_agent import ProcurementAgent
from .tech_support_agent import TechSupportAgent
from .generic_agent import GenericAgent
from .human_agent import HumanAgent

__all__ = [
    "BaseAgent",
    "PlannerAgent",
    "GroupChatManager",
    "HrAgent",
    "MarketingAgent",
    "ProductAgent",
    "ProcurementAgent",
    "TechSupportAgent",
    "GenericAgent",
    "HumanAgent",
]
