"""
Console Memory Context - Simplified in-memory storage for console application.
This replaces the CosmosDB dependency with in-memory storage for local testing.
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Type

from models import (
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
        logger.info(f"Updated session: {session.id}")
        return session
    
    # Plan management
    async def create_plan(self, plan: Plan) -> Plan:
        """Create a new plan."""
        self._plans[plan.id] = plan
        logger.info(f"Created plan: {plan.id}")
        return plan
    
    async def get_plan(self, plan_id: str) -> Optional[Plan]:
        """Get a plan by ID."""
        return self._plans.get(plan_id)
    
    async def update_plan(self, plan: Plan) -> Plan:
        """Update an existing plan."""
        self._plans[plan.id] = plan
        logger.info(f"Updated plan: {plan.id}")
        return plan
    
    async def get_plans_for_session(self, session_id: str, user_id: str) -> List[Plan]:
        """Get all plans for a session."""
        return [
            plan for plan in self._plans.values()
            if plan.session_id == session_id and plan.user_id == user_id
        ]
    
    async def get_latest_plan(self, session_id: str, user_id: str) -> Optional[Plan]:
        """Get the latest plan for a session."""
        plans = await self.get_plans_for_session(session_id, user_id)
        if not plans:
            return None
        return max(plans, key=lambda p: p.created_at)
    
    # Step management
    async def create_step(self, step: Step) -> Step:
        """Create a new step."""
        self._steps[step.id] = step
        logger.info(f"Created step: {step.id}")
        return step
    
    async def get_step(self, step_id: str, session_id: str = None) -> Optional[Step]:
        """Get a step by ID."""
        # session_id is ignored in console implementation since we store all steps in memory
        return self._steps.get(step_id)
    
    async def update_step(self, step: Step) -> Step:
        """Update an existing step."""
        self._steps[step.id] = step
        logger.info(f"Updated step: {step.id}")
        return step
    
    async def get_steps_for_plan(self, plan_id: str) -> List[Step]:
        """Get all steps for a plan."""
        return [
            step for step in self._steps.values()
            if step.plan_id == plan_id
        ]
    
    async def get_pending_steps(self, plan_id: str) -> List[Step]:
        """Get all pending steps for a plan."""
        return [
            step for step in self._steps.values()
            if step.plan_id == plan_id and step.status == StepStatus.planned
        ]
    
    # Agent message management
    async def create_agent_message(self, message: AgentMessage) -> AgentMessage:
        """Create a new agent message."""
        self._agent_messages[message.id] = message
        logger.info(f"Created agent message: {message.id}")
        return message
    
    async def get_agent_message(self, message_id: str) -> Optional[AgentMessage]:
        """Get an agent message by ID."""
        return self._agent_messages.get(message_id)
    
    async def update_agent_message(self, message: AgentMessage) -> AgentMessage:
        """Update an existing agent message."""
        self._agent_messages[message.id] = message
        logger.info(f"Updated agent message: {message.id}")
        return message
    
    async def get_messages_for_session(self, session_id: str) -> List[AgentMessage]:
        """Get all agent messages for a session."""
        return [
            message for message in self._agent_messages.values()
            if message.session_id == session_id
        ]
    
    async def get_messages_for_plan(self, plan_id: str) -> List[AgentMessage]:
        """Get all agent messages for a plan."""
        return [
            message for message in self._agent_messages.values()
            if message.plan_id == plan_id
        ]
    
    async def get_messages_for_step(self, step_id: str) -> List[AgentMessage]:
        """Get all agent messages for a step."""
        return [
            message for message in self._agent_messages.values()
            if message.step_id == step_id
        ]
    
    # Memory record management (for agent memory)
    async def save_memory_record(self, collection_name: str, record_id: str, data: Dict[str, Any]) -> None:
        """Save a memory record."""
        if collection_name not in self._memory_records:
            self._memory_records[collection_name] = {}
        
        self._memory_records[collection_name][record_id] = data
        logger.debug(f"Saved memory record: {collection_name}/{record_id}")
    
    async def get_memory_record(self, collection_name: str, record_id: str) -> Optional[Dict[str, Any]]:
        """Get a memory record."""
        if collection_name not in self._memory_records:
            return None
        
        return self._memory_records[collection_name].get(record_id)
    
    async def search_memory_records(self, collection_name: str, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search memory records (simple text search for console)."""
        if collection_name not in self._memory_records:
            return []
        
        results = []
        for record_id, data in self._memory_records[collection_name].items():
            # Simple text search in the data
            data_str = json.dumps(data, default=str).lower()
            if query.lower() in data_str:
                results.append(data)
                if len(results) >= limit:
                    break
        
        return results
    
    async def delete_memory_record(self, collection_name: str, record_id: str) -> bool:
        """Delete a memory record."""
        if collection_name not in self._memory_records:
            return False
        
        if record_id in self._memory_records[collection_name]:
            del self._memory_records[collection_name][record_id]
            logger.debug(f"Deleted memory record: {collection_name}/{record_id}")
            return True
        
        return False
    
    # Utility methods
    async def clear_all_data(self) -> None:
        """Clear all data from memory (for testing)."""
        self._sessions.clear()
        self._plans.clear()
        self._steps.clear()
        self._agent_messages.clear()
        self._memory_records.clear()
        logger.info("Cleared all data from memory")
    
    # Missing methods used by agents
    async def add_item(self, item: BaseDataModel) -> None:
        """Add any data model item to the appropriate storage."""
        if isinstance(item, Session):
            await self.create_session(item)
        elif isinstance(item, Plan):
            await self.create_plan(item)
        elif isinstance(item, Step):
            await self.create_step(item)
        elif isinstance(item, AgentMessage):
            await self.create_agent_message(item)
        else:
            logger.warning(f"Unknown item type: {type(item).__name__}")

    async def add_step(self, step: Step) -> None:
        """Add a step to memory."""
        await self.create_step(step)

    async def add_plan(self, plan: Plan) -> None:
        """Add a plan to memory."""
        await self.create_plan(plan)

    async def get_plan_by_session(self, session_id: str) -> Optional[Plan]:
        """Get the latest plan for a session."""
        return await self.get_latest_plan(session_id, self.user_id)

    async def get_steps_by_plan(self, plan_id: str) -> List[Step]:
        """Get all steps for a plan (alias for get_steps_for_plan)."""
        return await self.get_steps_for_plan(plan_id)

    async def delete_step(self, step_id: str, session_id: str = None) -> bool:
        """Delete a step by ID."""
        if step_id in self._steps:
            del self._steps[step_id]
            logger.info(f"Deleted step: {step_id}")
            return True
        return False
    
    async def get_stats(self) -> Dict[str, int]:
        """Get statistics about stored data."""
        return {
            "sessions": len(self._sessions),
            "plans": len(self._plans),
            "steps": len(self._steps),
            "agent_messages": len(self._agent_messages),
            "memory_collections": len(self._memory_records),
        }
