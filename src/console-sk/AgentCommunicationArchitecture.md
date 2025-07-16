# Agent Communication Architecture

This document provides a detailed explanation of how agents communicate within the Multi-Agent Custom Automation Engine (MACAE) system.

## System Overview

The MACAE system uses a multi-agent architecture where specialized AI agents collaborate to execute complex business tasks. The system is built on top of Semantic Kernel and Azure AI Foundry, providing a robust foundation for agent orchestration.

## Agent Communication Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              USER INTERACTION                                   │
│                                                                                 │
│  User Input: "onboard new employee Sarah Johnson"                              │
│                                    │                                           │
│                                    ▼                                           │
│                            ┌─────────────────┐                                │
│                            │   main.py       │                                │
│                            │ (Console Loop)  │                                │
│                            └─────────────────┘                                │
│                                    │                                           │
│                                    ▼                                           │
│                            ┌─────────────────┐                                │
│                            │ ConsoleMACAE    │                                │
│                            │ (console_app.py)│                                │
│                            └─────────────────┘                                │
└─────────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              TASK PLANNING                                     │
│                                                                                 │
│                            ┌─────────────────┐                                │
│                            │  PlannerAgent   │                                │
│                            │                 │                                │
│                            │ • Analyzes task │                                │
│                            │ • Creates plan  │                                │
│                            │ • Assigns steps │                                │
│                            │   to agents     │                                │
│                            └─────────────────┘                                │
│                                     │                                           │
│                                     ▼                                           │
│                            ┌─────────────────┐                                │
│                            │ Memory Store    │                                │
│                            │                 │                                │
│                            │ • Stores plan   │                                │
│                            │ • Stores steps  │                                │
│                            │ • Tracks status │                                │
│                            └─────────────────┘                                │
└─────────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           PLAN ORCHESTRATION                                   │
│                                                                                 │
│                            ┌─────────────────┐                                │
│                            │GroupChatManager │                                │
│                            │                 │                                │
│                            │ • Executes plan │                                │
│                            │ • Coordinates   │                                │
│                            │   agents        │                                │
│                            │ • Manages flow  │                                │
│                            └─────────────────┘                                │
│                                     │                                           │
│                                     ▼                                           │
│                          ┌─────────────────────┐                              │
│                          │ Sequential Step     │                              │
│                          │ Execution           │                              │
│                          │                     │                              │
│                          │ Step 1 → Step 2 →  │                              │
│                          │ Step 3 → ...       │                              │
│                          └─────────────────────┘                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          SPECIALIZED AGENTS                                    │
│                                                                                 │
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐           │
│ │   HR Agent  │  │Marketing    │  │ Product     │  │Procurement  │           │
│ │             │  │Agent        │  │ Agent       │  │Agent        │           │
│ │• Employee   │  │• Campaigns  │  │• Plans      │  │• Ordering   │           │
│ │  onboarding │  │• Analysis   │  │• Billing    │  │• Inventory  │           │
│ │• Reviews    │  │• Content    │  │• Upgrades   │  │• Vendors    │           │
│ │• Payroll    │  │• Social     │  │• Support    │  │• Tracking   │           │
│ └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘           │
│                                                                                 │
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                            │
│ │Tech Support │  │Generic      │  │Human        │                            │
│ │Agent        │  │Agent        │  │Agent        │                            │
│ │             │  │             │  │             │                            │
│ │• IT Setup   │  │• General    │  │• Approvals  │                            │
│ │• Passwords  │  │  tasks      │  │• Reviews    │                            │
│ │• VPN        │  │• Fallback   │  │• Feedback   │                            │
│ │• Software   │  │  handler    │  │• Validation │                            │
│ └─────────────┘  └─────────────┘  └─────────────┘                            │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Communication Patterns

### 1. Request-Response Pattern

```
GroupChatManager                    Specialized Agent
       │                                   │
       │    ActionRequest                  │
       │─────────────────────────────────→│
       │                                   │
       │                                   │ ┌─────────────────┐
       │                                   │ │ Process Action  │
       │                                   │ │ • Use tools     │
       │                                   │ │ • Call LLM      │
       │                                   │ │ • Update state  │
       │                                   │ └─────────────────┘
       │                                   │
       │    ActionResponse                 │
       │←─────────────────────────────────│
       │                                   │
```

### 2. Shared Memory Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                    Memory Store                                  │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   Plans     │  │   Steps     │  │  Messages   │             │
│  │             │  │             │  │             │             │
│  │ • Task desc │  │ • Action    │  │ • Agent     │             │
│  │ • Status    │  │ • Agent     │  │   comms     │             │
│  │ • Steps     │  │ • Status    │  │ • History   │             │
│  │ • Results   │  │ • Results   │  │ • Context   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└─────────────────────────────────────────────────────────────────┘
         ▲                   ▲                   ▲
         │                   │                   │
   ┌─────────┐         ┌─────────┐         ┌─────────┐
   │Agent A  │         │Agent B  │         │Agent C  │
   │         │         │         │         │         │
   │ Read/   │         │ Read/   │         │ Read/   │
   │ Write   │         │ Write   │         │ Write   │
   └─────────┘         └─────────┘         └─────────┘
```

### 3. Event-Driven Execution

```
Step 1: Background Check        Step 2: Create Record       Step 3: Setup Office 365
┌─────────────────────┐        ┌─────────────────────┐     ┌─────────────────────┐
│     HR Agent        │        │     HR Agent        │     │  Tech Support       │
│                     │        │                     │     │  Agent              │
│ Status: In Progress │───────▶│ Status: Waiting     │────▶│ Status: Waiting     │
│                     │        │                     │     │                     │
│ ┌─────────────────┐ │        │ ┌─────────────────┐ │     │ ┌─────────────────┐ │
│ │ - Check refs    │ │        │ │ - Create profile│ │     │ │ - Setup email   │ │
│ │ - Verify docs   │ │        │ │ - Generate ID   │ │     │ │ - Config access │ │
│ │ - Update status │ │        │ │ - Send welcome  │ │     │ │ - Set permissions│ │
│ └─────────────────┘ │        │ └─────────────────┘ │     │ └─────────────────┘ │
└─────────────────────┘        └─────────────────────┘     └─────────────────────┘
```

## Message Flow Detail

### 1. InputTask Creation

```python
# User input is converted to InputTask
InputTask {
    session_id: "uuid-123",
    user_id: "console_user",
    description: "onboard new employee Sarah Johnson",
    timestamp: "2025-07-16T10:00:00Z"
}
```

### 2. Plan Generation

```python
# PlannerAgent creates structured plan
Plan {
    id: "plan-456",
    session_id: "uuid-123",
    description: "Employee onboarding for Sarah Johnson",
    steps: [
        Step {
            id: "step-1",
            plan_id: "plan-456",
            action: "Start background check for Sarah Johnson",
            agent: AgentType.HR,
            status: StepStatus.pending
        },
        Step {
            id: "step-2", 
            plan_id: "plan-456",
            action: "Create employee record for Sarah Johnson",
            agent: AgentType.HR,
            status: StepStatus.pending
        },
        Step {
            id: "step-3",
            plan_id: "plan-456", 
            action: "Set up Office 365 account for Sarah Johnson",
            agent: AgentType.TECH_SUPPORT,
            status: StepStatus.pending
        }
    ]
}
```

### 3. Action Execution

```python
# GroupChatManager sends ActionRequest to agent
ActionRequest {
    step_id: "step-1",
    plan_id: "plan-456",
    session_id: "uuid-123",
    action: "Start background check for Sarah Johnson",
    agent: AgentType.HR
}

# Agent responds with ActionResponse
ActionResponse {
    step_id: "step-1",
    plan_id: "plan-456", 
    session_id: "uuid-123",
    result: "Background check initiated for Sarah Johnson...",
    status: StepStatus.completed
}
```

## Agent Lifecycle

### 1. Agent Creation

```python
# Agents are created through ConsoleAgentFactory
agents = await ConsoleAgentFactory.create_all_agents(
    session_id=session_id,
    user_id=user_id,
    memory_store=memory_store,
    temperature=0.0
)
```

### 2. Agent Initialization

```python
# Each agent is initialized with:
# - Azure AI client
# - Memory store reference
# - System message/prompt
# - Available tools
# - Cross-references to other agents
```

### 3. Agent Execution

```python
# Agent processes ActionRequest:
# 1. Retrieves step from memory
# 2. Adds context to chat history
# 3. Invokes LLM with tools
# 4. Processes response
# 5. Updates step status
# 6. Returns ActionResponse
```

## Tool Integration

Each agent has access to specialized tools:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    HR Agent     │    │ Marketing Agent │    │Tech Support     │
│                 │    │                 │    │Agent            │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │  HR Tools   │ │    │ │Marketing    │ │    │ │Tech Support │ │
│ │             │ │    │ │Tools        │ │    │ │Tools        │ │
│ │• Onboarding │ │    │ │• Campaigns  │ │    │ │• IT Setup   │ │
│ │• Reviews    │ │    │ │• Analytics  │ │    │ │• Passwords  │ │
│ │• Payroll    │ │    │ │• Content    │ │    │ │• Access     │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Key Communication Principles

### 1. Asynchronous Processing
- All agent communication is asynchronous
- Uses Python async/await pattern
- Enables concurrent processing where possible

### 2. State Management
- Shared memory store maintains system state
- All agents can read/write to memory
- Ensures consistency across agents

### 3. Error Handling
- Robust error handling at each communication layer
- Failed steps can be retried or escalated
- Human agent can intervene when needed

### 4. Scalability
- Modular agent design allows easy extension
- New agents can be added without system changes
- Tool integration is pluggable

## Console Application Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Console Application                            │
│                                                                     │
│  1. User enters: "onboard new employee Sarah Johnson"              │
│                                                                     │
│  2. collect_missing_info() enhances task if needed                 │
│                                                                     │
│  3. ConsoleMACAE.process_task() called                             │
│                                                                     │
│  4. PlannerAgent.handle_input_task() creates plan                  │
│                                                                     │
│  5. GroupChatManager.execute_plan() starts execution              │
│                                                                     │
│  6. For each step:                                                 │
│     - Create ActionRequest                                          │
│     - Send to appropriate agent                                     │
│     - Agent uses tools and LLM                                     │
│     - Return ActionResponse                                         │
│     - Update step status                                           │
│                                                                     │
│  7. Display results to user                                        │
│                                                                     │
│  8. Return to input prompt                                         │
└─────────────────────────────────────────────────────────────────────┘
```

## Sequence Diagram: Complete Agent Communication Flow

The following sequence diagram shows the complete interaction flow from user input to task completion:

```
User          ConsoleMACAE    PlannerAgent    Memory Store    GroupChatManager    Specialized Agent    Tools
 │                 │               │               │                │                    │              │
 │ "onboard new    │               │               │                │                    │              │
 │  employee"      │               │               │                │                    │              │
 │────────────────▶│               │               │                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │ InputTask     │               │                │                    │              │
 │                 │──────────────▶│               │                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │               │ LLM Analysis  │                │                    │              │
 │                 │               │ (Create Plan) │                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │               │ Store Plan    │                │                    │              │
 │                 │               │──────────────▶│                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │               │ Store Steps   │                │                    │              │
 │                 │               │──────────────▶│                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │ PlanResponse  │               │                │                    │              │
 │                 │◀──────────────│               │                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │ Get Plan      │               │                │                    │              │
 │                 │──────────────────────────────▶│                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │ Plan Data     │               │                │                    │              │
 │                 │◀──────────────────────────────│                │                    │              │
 │                 │               │               │                │                    │              │
 │                 │ Execute Plan  │               │                │                    │              │
 │                 │──────────────────────────────────────────────▶│                    │              │
 │                 │               │               │                │                    │              │
 │                 │               │               │ Get Steps      │                    │              │
 │                 │               │               │◀───────────────│                    │              │
 │                 │               │               │                │                    │              │
 │                 │               │               │ Steps Data     │                    │              │
 │                 │               │               │────────────────▶│                    │              │
 │                 │               │               │                │ ActionRequest      │              │
 │                 │               │               │                │ (Step 1)          │              │
 │                 │               │               │                │───────────────────▶│              │
 │                 │               │               │                │                    │              │
 │                 │               │               │                │                    │ Get Step     │
 │                 │               │               │                │                    │ Details      │
 │                 │               │               │                │                    │─────────────▶│
 │                 │               │               │                │                    │              │
 │                 │               │               │                │                    │ Step Data    │
 │                 │               │               │                │                    │◀─────────────│
 │                 │               │               │                │                    │              │
 │                 │               │               │                │                    │ LLM Call     │
 │                 │               │               │                │                    │ + Tools      │
 │                 │               │               │                │                    │──────────────▶│
 │                 │               │               │                │                    │              │
 │                 │               │               │                │                    │ Tool Results │
 │                 │               │               │                │                    │◀──────────────│
 │                 │               │               │                │                    │              │
 │                 │               │               │                │                    │ Update Step  │
 │                 │               │               │                │                    │ Status       │
 │                 │               │               │                │                    │─────────────▶│
 │                 │               │               │                │                    │              │
 │                 │               │               │                │ ActionResponse     │              │
 │                 │               │               │                │ (Step 1 Complete) │              │
 │                 │               │               │                │◀───────────────────│              │
 │                 │               │               │                │                    │              │
 │                 │               │               │                │ ActionRequest      │              │
 │                 │               │               │                │ (Step 2)          │              │
 │                 │               │               │                │───────────────────▶│              │
 │                 │               │               │                │                    │              │
 │                 │               │               │                │ ... (repeat for   │              │
 │                 │               │               │                │ each step)        │              │
 │                 │               │               │                │                    │              │
 │                 │ Plan Complete │               │                │                    │              │
 │                 │◀──────────────────────────────────────────────│                    │              │
 │                 │               │               │                │                    │              │
 │ "Task Complete" │               │               │                │                    │              │
 │◀────────────────│               │               │                │                    │              │
```

## Data Flow Architecture

### Core Data Models

The system uses several key data models for communication:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              DATA MODELS                                       │
│                                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│  │ InputTask   │    │    Plan     │    │    Step     │    │AgentMessage │    │
│  │             │    │             │    │             │    │             │    │
│  │• session_id │    │• id         │    │• id         │    │• id         │    │
│  │• user_id    │    │• session_id │    │• plan_id    │    │• session_id │    │
│  │• description│    │• user_id    │    │• action     │    │• from_agent │    │
│  │• timestamp  │    │• description│    │• agent      │    │• to_agent   │    │
│  │• status     │    │• status     │    │• status     │    │• content    │    │
│  └─────────────┘    │• created_at │    │• created_at │    │• timestamp  │    │
│                     │• updated_at │    │• updated_at │    │• message_type│    │
│                     └─────────────┘    │• result     │    └─────────────┘    │
│                                        │• feedback   │                       │
│                                        │• agent_reply│                       │
│  ┌─────────────┐    ┌─────────────┐    └─────────────┘    ┌─────────────┐    │
│  │ActionRequest│    │ActionResponse│                      │  Context    │    │
│  │             │    │             │                      │             │    │
│  │• step_id    │    │• step_id    │                      │• session_id │    │
│  │• plan_id    │    │• plan_id    │                      │• user_id    │    │
│  │• session_id │    │• session_id │                      │• variables  │    │
│  │• action     │    │• result     │                      │• history    │    │
│  │• agent      │    │• status     │                      │• metadata   │    │
│  │• context    │    │• timestamp  │                      │• preferences│    │
│  └─────────────┘    └─────────────┘                      └─────────────┘    │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Error Handling and Recovery Patterns

### 1. Agent Failure Recovery

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           ERROR HANDLING FLOW                                  │
│                                                                                 │
│  Step Execution                                                                 │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐                                                               │
│  │ Agent Call  │                                                               │
│  │             │                                                               │
│  │ • Try LLM   │                                                               │
│  │ • Use Tools │                                                               │
│  │ • Process   │                                                               │
│  └─────────────┘                                                               │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                      │
│  │   Success   │     │   Failure   │     │   Timeout   │                      │
│  │             │     │             │     │             │                      │
│  │ • Complete  │     │ • Log error │     │ • Retry     │                      │
│  │   step      │     │ • Mark step │     │ • Escalate  │                      │
│  │ • Continue  │     │   failed    │     │ • Fallback  │                      │
│  │   plan      │     │ • Notify    │     │   agent     │                      │
│  └─────────────┘     │   human     │     └─────────────┘                      │
│                      │ • Retry?    │                                           │
│                      └─────────────┘                                           │
│                             │                                                   │
│                             ▼                                                   │
│                      ┌─────────────┐                                           │
│                      │Human Agent  │                                           │
│                      │Intervention │                                           │
│                      │             │                                           │
│                      │ • Review    │                                           │
│                      │ • Approve   │                                           │
│                      │ • Modify    │                                           │
│                      │ • Cancel    │                                           │
│                      └─────────────┘                                           │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Retry Mechanisms

```python
# Example retry pattern in BaseAgent
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(Exception)
)
async def handle_action_request(self, action_request: ActionRequest) -> str:
    # Agent execution logic with automatic retry
    pass
```

### 3. Fallback Strategies

```
Primary Agent        Fallback Agent        Human Agent
     │                     │                    │
     │ ActionRequest       │                    │
     │────────────────────▶│                    │
     │                     │                    │
     │ Failed              │                    │
     │◀────────────────────│                    │
     │                     │                    │
     │ Escalate to Generic │                    │
     │────────────────────▶│                    │
     │                     │                    │
     │ Still Failed        │                    │
     │◀────────────────────│                    │
     │                     │                    │
     │ Escalate to Human   │                    │
     │──────────────────────────────────────────▶│
     │                     │                    │
     │ Manual Resolution   │                    │
     │◀──────────────────────────────────────────│
```

## Performance and Scalability Considerations

### 1. Concurrent Step Execution

While the current implementation executes steps sequentially, the architecture supports parallel execution:

```python
# Future enhancement: Parallel step execution
async def execute_parallel_steps(self, steps: List[Step]):
    # Group steps by dependency
    independent_steps = self.get_independent_steps(steps)
    
    # Execute in parallel
    tasks = []
    for step in independent_steps:
        task = asyncio.create_task(self._execute_step(step))
        tasks.append(task)
    
    # Wait for completion
    await asyncio.gather(*tasks)
```

### 2. Load Balancing

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           LOAD BALANCING                                       │
│                                                                                 │
│  Multiple Requests                                                              │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐                                                               │
│  │Load Balancer│                                                               │
│  │             │                                                               │
│  │ • Route     │                                                               │
│  │   requests  │                                                               │
│  │ • Monitor   │                                                               │
│  │   load      │                                                               │
│  └─────────────┘                                                               │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                      │
│  │ Agent Pool  │     │ Agent Pool  │     │ Agent Pool  │                      │
│  │     #1      │     │     #2      │     │     #3      │                      │
│  │             │     │             │     │             │                      │
│  │ • HR Agent  │     │ • Marketing │     │ • Tech      │                      │
│  │ • Product   │     │   Agent     │     │   Support   │                      │
│  │   Agent     │     │ • Generic   │     │ • Human     │                      │
│  └─────────────┘     │   Agent     │     │   Agent     │                      │
│                      └─────────────┘     └─────────────┘                      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 3. Caching Strategy

```python
# Memory store with caching
class ConsoleMemoryContext:
    def __init__(self):
        self._cache = {}
        self._cache_ttl = 300  # 5 minutes
    
    @lru_cache(maxsize=128)
    async def get_plan(self, plan_id: str) -> Optional[Plan]:
        # Cached plan retrieval
        pass
    
    async def invalidate_cache(self, session_id: str):
        # Clear cache on session changes
        pass
```

## Monitoring and Observability

### 1. Agent Health Monitoring

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MONITORING DASHBOARD                                 │
│                                                                                 │
│  Agent Status                    Performance Metrics                           │
│  ┌─────────────┐                ┌─────────────┐                               │
│  │ HR Agent    │ ● Online       │ Response     │ 1.2s avg                     │
│  │ Marketing   │ ● Online       │ Time         │                               │
│  │ Tech Support│ ● Online       │              │                               │
│  │ Product     │ ● Online       │ Success Rate │ 98.5%                        │
│  │ Procurement │ ● Degraded     │              │                               │
│  │ Generic     │ ● Online       │ Error Rate   │ 1.5%                         │
│  │ Human       │ ● Online       │              │                               │
│  └─────────────┘                └─────────────┘                               │
│                                                                                 │
│  Active Plans                    Recent Errors                                 │
│  ┌─────────────┐                ┌─────────────┐                               │
│  │ • Plan-123  │ In Progress    │ • Timeout   │ ProcurementAgent              │
│  │ • Plan-124  │ Completed      │ • API Error │ TechSupportAgent              │
│  │ • Plan-125  │ Failed         │ • LLM Error │ MarketingAgent                │
│  │ • Plan-126  │ Waiting        │             │                               │
│  └─────────────┘                └─────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Tracing and Logging

```python
# Distributed tracing example
import opentelemetry.trace as trace

tracer = trace.get_tracer(__name__)

async def handle_action_request(self, action_request: ActionRequest) -> str:
    with tracer.start_as_current_span("agent_execution") as span:
        span.set_attribute("agent.type", self.agent_type)
        span.set_attribute("step.id", action_request.step_id)
        span.set_attribute("plan.id", action_request.plan_id)
        
        try:
            result = await self._execute_action(action_request)
            span.set_attribute("execution.status", "success")
            return result
        except Exception as e:
            span.set_attribute("execution.status", "error")
            span.set_attribute("error.message", str(e))
            raise
```

## Security Considerations

### 1. Authentication and Authorization

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           SECURITY LAYERS                                      │
│                                                                                 │
│  User Request                                                                   │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐                                                               │
│  │Authentication│                                                               │
│  │             │                                                               │
│  │ • Azure AD  │                                                               │
│  │ • API Keys  │                                                               │
│  │ • Tokens    │                                                               │
│  └─────────────┘                                                               │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐                                                               │
│  │Authorization│                                                               │
│  │             │                                                               │
│  │ • Role-based│                                                               │
│  │ • Permissions│                                                              │
│  │ • Scope     │                                                               │
│  └─────────────┘                                                               │
│       │                                                                         │
│       ▼                                                                         │
│  ┌─────────────┐                                                               │
│  │Agent Access │                                                               │
│  │Control      │                                                               │
│  │             │                                                               │
│  │ • Tool      │                                                               │
│  │   permissions│                                                              │
│  │ • Data      │                                                               │
│  │   access    │                                                               │
│  └─────────────┘                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Data Encryption

```python
# Sensitive data handling
class SecureMemoryStore:
    def __init__(self):
        self.encryption_key = os.environ.get("ENCRYPTION_KEY")
        self.cipher = Fernet(self.encryption_key)
    
    async def store_sensitive_data(self, data: dict):
        # Encrypt before storing
        encrypted_data = self.cipher.encrypt(json.dumps(data).encode())
        await self._store(encrypted_data)
    
    async def retrieve_sensitive_data(self, key: str) -> dict:
        # Decrypt after retrieval
        encrypted_data = await self._retrieve(key)
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
```

This comprehensive architecture documentation provides developers and architects with a complete understanding of how the Multi-Agent Custom Automation Engine operates, communicates, and scales. The system's modular design allows for easy extension and customization while maintaining robust communication patterns and error handling capabilities.
