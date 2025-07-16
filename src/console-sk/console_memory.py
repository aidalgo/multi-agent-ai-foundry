"""
Console Memory Context - Simplified in-memory storage for console application.
This replaces the CosmosDB dependency with in-memory storage for local testing.
"""

import asyncio
import json
import logging
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Type

# Add the backend directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from backend.models.messages_kernel import (
    AgentMessage,
    BaseDataModel,
    Plan,
    PlanStatus,
    Session,
    Step,
    StepStatus,
)

logger = logging.getLogger(__name__)


class ConsoleMemoryContext:
    """In-memory storage context for console application."""
    
    def __init__(self, session_id: str, user_id: str):
        """Initialize the console memory context."""
        self.session_id = session_id
        self.user_id = user_id
        
        # In-memory storage
        self._sessions: Dict[str, Session] = {}
        self._plans: Dict[str, Plan] = {}
        self._steps: Dict[str, Step] = {}
        self._agent_messages: Dict[str, AgentMessage] = {}
        self._memory_records: Dict[str, Dict[str, Any]] = {}
        
        logger.info(f"Console memory context initialized for session: {session_id}")
    
    # Session management
    async def create_session(self, session: Session) -> Session:
        """Create a new session."""
        self._sessions[session.id] = session
        logger.info(f"Created session: {session.id}")
        return session
    
    async def get_session(self, session_id: str) -> Optional[Session]:
        """Get a session by ID."""
        return self._sessions.get(session_id)
    
    async def update_session(self, session: Session) -> Session:
        """Update an existing session."""
        self._sessions[session.id] = session
        return session
    
    # Plan management
    async def create_plan(self, plan: Plan) -> Plan:
        """Create a new plan."""
        self._plans[plan.id] = plan
        logger.info(f"Created plan: {plan.id} - {plan.initial_goal}")
        return plan
    
    async def add_plan(self, plan: Plan) -> Plan:
        """Add a new plan (alias for create_plan)."""
        return await self.create_plan(plan)
    
    async def get_plan(self, plan_id: str) -> Optional[Plan]:
        """Get a plan by ID."""
        return self._plans.get(plan_id)
    
    async def update_plan(self, plan: Plan) -> Plan:
        """Update an existing plan."""
        self._plans[plan.id] = plan
        return plan
    
    async def get_latest_plan(self, session_id: str, user_id: str) -> Optional[Plan]:
        """Get the latest plan for a session."""
        session_plans = [
            plan for plan in self._plans.values()
            if plan.session_id == session_id and plan.user_id == user_id
        ]
        
        if not session_plans:
            return None
            
        # Return the most recent plan
        return max(session_plans, key=lambda p: p.timestamp)
    
    async def get_plan_by_session(self, session_id: str) -> Optional[Plan]:
        """Get the latest plan for a session (alias for get_latest_plan)."""
        # Find the latest plan for this session
        session_plans = [
            plan for plan in self._plans.values()
            if plan.session_id == session_id
        ]
        
        if not session_plans:
            return None
            
        # Return the most recent plan
        return max(session_plans, key=lambda p: p.timestamp)
    
    # Step management
    async def create_step(self, step: Step) -> Step:
        """Create a new step."""
        self._steps[step.id] = step
        logger.info(f"Created step: {step.id} - {step.action}")
        return step
    
    async def add_step(self, step: Step) -> Step:
        """Add a new step (alias for create_step)."""
        return await self.create_step(step)
    
    async def get_step(self, step_id: str, session_id: str) -> Optional[Step]:
        """Get a step by ID and session ID."""
        step = self._steps.get(step_id)
        if step and step.session_id == session_id:
            return step
        return None
    
    async def update_step(self, step: Step) -> Step:
        """Update an existing step."""
        self._steps[step.id] = step
        return step
    
    async def get_steps_for_plan(self, plan_id: str) -> List[Step]:
        """Get all steps for a specific plan."""
        plan_steps = [
            step for step in self._steps.values()
            if step.plan_id == plan_id
        ]
        
        # Sort by timestamp
        return sorted(plan_steps, key=lambda s: s.timestamp)
    
    async def get_steps_by_plan(self, plan_id: str) -> List[Step]:
        """Get all steps for a specific plan (alias for get_steps_for_plan)."""
        return await self.get_steps_for_plan(plan_id)
    
    # Agent message management
    async def create_agent_message(self, message: AgentMessage) -> AgentMessage:
        """Create a new agent message."""
        self._agent_messages[message.id] = message
        logger.info(f"Created agent message: {message.id}")
        return message
    
    async def get_agent_message(self, message_id: str) -> Optional[AgentMessage]:
        """Get an agent message by ID."""
        return self._agent_messages.get(message_id)
    
    async def get_agent_messages_for_session(self, session_id: str) -> List[AgentMessage]:
        """Get all agent messages for a session."""
        session_messages = [
            msg for msg in self._agent_messages.values()
            if msg.session_id == session_id
        ]
        
        # Sort by timestamp
        return sorted(session_messages, key=lambda m: m.timestamp)
    
    # Memory record management (for Semantic Kernel compatibility)
    async def upsert_async(self, collection_name: str, record: Dict[str, Any]) -> str:
        """Upsert a memory record."""
        if collection_name not in self._memory_records:
            self._memory_records[collection_name] = {}
        
        record_id = record.get('id', str(uuid.uuid4()))
        self._memory_records[collection_name][record_id] = record
        
        logger.debug(f"Upserted memory record: {record_id} in collection: {collection_name}")
        return record_id
    
    async def get_async(self, collection_name: str, record_id: str) -> Optional[Dict[str, Any]]:
        """Get a memory record."""
        collection = self._memory_records.get(collection_name, {})
        return collection.get(record_id)
    
    async def query_items(self, collection_name: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Query memory records from a collection."""
        collection = self._memory_records.get(collection_name, {})
        items = list(collection.values())
        
        # Sort by timestamp if available
        try:
            items.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        except (TypeError, KeyError):
            pass
        
        return items[:limit]
    
    async def delete_collection_async(self, collection_name: str) -> None:
        """Delete a collection."""
        if collection_name in self._memory_records:
            del self._memory_records[collection_name]
            logger.info(f"Deleted collection: {collection_name}")
    
    # Generic item management
    async def add_item(self, item: BaseDataModel) -> None:
        """Add a generic item to the appropriate storage."""
        if isinstance(item, Session):
            await self.create_session(item)
        elif isinstance(item, Plan):
            await self.create_plan(item)
        elif isinstance(item, Step):
            await self.create_step(item)
        elif isinstance(item, AgentMessage):
            await self.create_agent_message(item)
        else:
            logger.warning(f"Unknown item type: {type(item)}")
    
    # Utility methods
    async def get_all_data(self) -> Dict[str, Any]:
        """Get all stored data for debugging."""
        return {
            'sessions': self._sessions,
            'plans': self._plans,
            'steps': self._steps,
            'agent_messages': self._agent_messages,
            'memory_records': self._memory_records,
        }
    
    async def clear_all_data(self) -> None:
        """Clear all stored data."""
        self._sessions.clear()
        self._plans.clear()
        self._steps.clear()
        self._agent_messages.clear()
        self._memory_records.clear()
        logger.info("Cleared all data from console memory context")
    
    async def add_item(self, item: Any) -> Any:
        """Add an item to the memory store (generic method for messages, etc.)."""
        # This is a generic method that handles various item types
        # For now, we'll just log it since we don't have a specific storage for all item types
        logger.info(f"Adding item of type {type(item).__name__}: {item}")
        return item
    
    def get_stats(self) -> Dict[str, int]:
        """Get statistics about stored data."""
        return {
            'sessions': len(self._sessions),
            'plans': len(self._plans),
            'steps': len(self._steps),
            'agent_messages': len(self._agent_messages),
            'memory_collections': len(self._memory_records),
        }
