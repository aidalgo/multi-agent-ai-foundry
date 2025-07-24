# Console Multi-Agent Custom Automation Engine

A simplified console version of the multi-agent system using Semantic Kernel and Azure AI Foundry.

## Overview

The Console MACAE (Multi-Agent Custom Automation Engine) is a command-line interface that demonstrates the core multi-agent capabilities of the system. It provides an interactive console where users can input natural language tasks and see how they are automatically processed by specialized AI agents.

## Features

- **Multi-Agent System**: Includes HR, Marketing, Product, Procurement, Tech Support, Generic, Human, Planner, and Group Chat Manager agents
- **Semantic Kernel Integration**: Uses Microsoft's Semantic Kernel for AI orchestration
- **Azure AI Foundry**: Leverages Azure AI Foundry for agent creation and management
- **Local Authentication**: Uses Azure Default Credentials for local development
- **In-Memory Storage**: Simplified storage for console testing (no CosmosDB required)
- **Interactive Console**: User-friendly console interface for task management

## Prerequisites

1. **Azure Setup**:
   - Azure subscription with AI services enabled
   - Azure OpenAI service deployed
   - Azure AI Foundry project created

2. **Local Setup**:
   - Python 3.8+
   - Azure CLI installed and configured
   - Authentication via `az login`

## Installation

1. **Navigate to the console directory**:
   ```bash
   cd src/console-sk
   ```

2. **Run the setup script**:
   ```bash
   python setup.py
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure credentials
   ```

4. **Login to Azure**:
   ```bash
   az login
   ```

5. **Test the setup**:
   ```bash
   python test_setup.py
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

## Configuration

Edit the `.env` file with your Azure credentials:

```env
# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_VERSION=2024-11-20

# Azure AI settings
AZURE_AI_SUBSCRIPTION_ID=your-subscription-id
AZURE_AI_RESOURCE_GROUP=your-resource-group
AZURE_AI_PROJECT_NAME=your-ai-project-name
AZURE_AI_AGENT_ENDPOINT=https://your-ai-project.cognitiveservices.azure.com/
```

## Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONSOLE APPLICATION                                │
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
```

### Agent Communication Flow

```
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
```

### Specialized Agents

```
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

### Key Files

#### Core Application
- **`main.py`** - Entry point and interactive console loop
- **`console_app.py`** - Main application class (`ConsoleMACAE`)
- **`config.py`** - Configuration management
- **`memory.py`** - Memory store implementation
- **`models.py`** - Data models and message types
- **`utils.py`** - Utility functions and agent factory
#### Agent System

**`ConsoleAgentFactory`**: Main factory for creating all agent types
- `create_all_agents()`: Create and initialize all agents for a session
- `_create_single_agent()`: Create an individual agent with type-specific parameters
- `_setup_agent_coordination()`: Set up inter-agent communication
- `get_available_agent_types()`: Return a list of available agent types
- `get_agent_class_mapping()`: Return a mapping of agent types to classes

**Agent Modules:**
- **`agents/base_agent.py`** — Base agent class
- **`agents/planner_agent.py`** — Task planning agent
- **`agents/group_chat_manager.py`** — Plan execution coordinator
- **`agents/hr_agent.py`** — HR-related tasks
- **`agents/marketing_agent.py`** — Marketing tasks
- **`agents/product_agent.py`** — Product management
- **`agents/procurement_agent.py`** — Procurement tasks
- **`agents/tech_support_agent.py`** — Technical support
- **`agents/generic_agent.py`** — General task handling
- **`agents/human_agent.py`** — Human interaction management

#### Tools and Utilities
- **`tools/`** - Specialized tool implementations for each agent
- **`utils/`** - Utility functions and helpers

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
   🤖 Sending task to planner agent...
   ✅ Plan created successfully!
   
   📋 Plan: Help me plan a product launch for a new mobile app
   Status: in_progress
   Steps (5):
     1. Marketing Agent: Create marketing strategy for mobile app launch
     2. Product Agent: Define product features and positioning
     3. HR Agent: Plan team structure for launch
     4. Procurement Agent: Source launch materials and vendors
     5. Tech Support Agent: Prepare technical documentation
## Usage Examples

### Running the Console Application

```bash
# Navigate to the console-sk directory
cd src/console-sk

# Run the application
python main.py
```

### Example Interactions

```
>> onboard new employee Sarah Johnson

🔄 Processing: onboard new employee Sarah Johnson
------------------------------------------------------------
🤖 Executing step 1: Start background check for Sarah Johnson
   Agent: hr

🤖 Executing step 2: Create employee record for Sarah Johnson
   Agent: hr

🤖 Executing step 3: Set up Office 365 account for Sarah Johnson
   Agent: tech_support
```

### Available Commands

- **`actions`** - Show all available actions
- **`examples`** - Show example requests  
- **`status`** - Check current plan status
- **`help`** - Show help message
- **`quit`** or **`exit`** - Exit the application

### Example Requests by Category

#### 1. HR & Employee Management
```
>> onboard new employee John Doe
>> schedule orientation session
>> process leave request  
>> schedule performance review
>> assign mentor to employee
>> set up payroll for employee
```

#### 2. IT & Technical Support
```
>> set up office 365 account for mike.smith@company.com
>> reset password for user john.doe
>> configure VPN access for remote employee
>> install software for employee
>> troubleshoot network issues
>> handle cybersecurity incident
```

#### 3. Marketing & Communications
```
>> create marketing campaign for product launch
>> analyze market trends in technology sector
>> create social media posts for holiday promotion
>> plan advertising budget
>> conduct customer survey
>> perform competitor analysis
```

#### 4. Procurement & Asset Management
```
>> order laptop for new developer
>> order software licenses
>> check inventory status
>> process purchase order for office supplies
>> track order status
>> manage vendor relationships
```

#### 5. Product & Service Management
```
>> add mobile extras pack to customer plan
>> get product information
>> modify customer service plan
>> check plan eligibility
>> process service upgrade/downgrade
```

## Data Models

### Core Message Types

```python
class InputTask:
    session_id: str
    user_id: str
    description: str
    timestamp: datetime
    status: TaskStatus

class Plan:
    id: str
    session_id: str
    user_id: str
    description: str
    status: PlanStatus
    steps: List[Step]
    created_at: datetime
    updated_at: datetime

class Step:
    id: str
    plan_id: str
    action: str
    agent: AgentType
    status: StepStatus
    result: Optional[str]
    agent_reply: Optional[str]
    human_feedback: Optional[str]
    created_at: datetime
    updated_at: datetime

class ActionRequest:
    step_id: str
    plan_id: str
    session_id: str
    action: str
    agent: AgentType
    context: Optional[dict]

class ActionResponse:
    step_id: str
    plan_id: str
    session_id: str
    result: str
    status: StepStatus
    timestamp: datetime
```

### Agent Types

```python
class AgentType(Enum):
    PLANNER = "planner"
    GROUP_CHAT_MANAGER = "group_chat_manager"
    HR = "hr"
    MARKETING = "marketing"
    PRODUCT = "product"
    PROCUREMENT = "procurement"
    TECH_SUPPORT = "tech_support"
    GENERIC = "generic"
    HUMAN = "human"
```

### Status Types

```python
class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class PlanStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class StepStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
```

## Memory Store

### In-Memory Implementation

The console application uses an in-memory store for simplicity:

```python
class ConsoleMemoryContext:
    def __init__(self):
        self._plans = {}
        self._steps = {}
        self._messages = {}
        self._context = {}
    
    async def create_plan(self, plan: Plan) -> Plan:
        self._plans[plan.id] = plan
        return plan
    
    async def get_plan(self, plan_id: str, session_id: str) -> Optional[Plan]:
        return self._plans.get(plan_id)
    
    async def update_step(self, step: Step) -> Step:
        self._steps[step.id] = step
        return step
    
    async def get_steps_for_plan(self, plan_id: str) -> List[Step]:
        return [step for step in self._steps.values() if step.plan_id == plan_id]
```

### Memory Operations

- **Plans**: Create, read, update, delete plans
- **Steps**: Create, read, update step execution status
- **Messages**: Store agent communication history
- **Context**: Maintain session context and variables

## Error Handling

### Retry Mechanisms

```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(Exception)
)
async def handle_action_request(self, action_request: ActionRequest) -> str:
    # Agent execution logic with automatic retry
    pass
```

### Fallback Strategies

1. **Primary Agent Fails** → **Generic Agent**
2. **Generic Agent Fails** → **Human Agent**  
3. **Human Agent** → **Manual Resolution**

### Error Types

- **LLM Errors**: API failures, rate limits, timeout
- **Tool Errors**: Tool execution failures
- **Memory Errors**: Storage/retrieval issues
- **Agent Errors**: Agent initialization or execution failures

## Configuration

### Environment Variables

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-11-20

# Azure AI Foundry Configuration
AZURE_AI_SUBSCRIPTION_ID=your-subscription-id
AZURE_AI_RESOURCE_GROUP=your-resource-group
AZURE_AI_PROJECT_NAME=your-project-name
AZURE_AI_AGENT_ENDPOINT=https://your-project.cognitiveservices.azure.com/
```

### Configuration File

The application uses `config.py` for configuration management:

```python
# Agent Configuration
TEMPERATURE = 0.0
MAX_TOKENS = 4000
AGENT_TIMEOUT = 30

# Memory Configuration
MEMORY_STORE_TYPE = "in_memory"
SESSION_TIMEOUT = 3600

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

## Development

### Adding New Agents

1. Create new agent class inheriting from `BaseAgent`:

```python
class CustomAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.agent_type = AgentType.CUSTOM
    
    @staticmethod
    def default_system_message(agent_type: str) -> str:
        return "You are a custom agent..."
    
    async def handle_action_request(self, action_request: ActionRequest) -> str:
        # Custom agent logic
        pass
```

2. Add to agent factory in `utils.py`:

```python
agent_classes = {
    AgentType.CUSTOM: CustomAgent,
    # ...existing agents
}
```

3. Register in `AgentType` enum:

```python
class AgentType(Enum):
    CUSTOM = "custom"
    # ...existing types
```

### Adding New Tools

1. Create tool class in `tools/` directory:

```python
class CustomTools:
    @kernel_function(
        name="custom_action",
        description="Performs a custom action"
    )
    async def custom_action(self, parameter: str) -> str:
        # Tool implementation
        return f"Custom action result: {parameter}"
```

2. Register tools with agent:

```python
def load_tools(self):
    custom_tools = CustomTools()
    self.kernel.add_plugin(custom_tools, "custom_tools")
```

### Testing

#### Unit Tests

```bash
# Run unit tests
pytest tests/unit/

# Run specific test file
pytest tests/unit/test_console_app.py

# Run with coverage
pytest --cov=src/console-sk tests/unit/
```

#### Integration Tests

```bash
# Run integration tests
pytest tests/integration/

# Run end-to-end tests
pytest tests/e2e/
```

#### Manual Testing

```bash
# Test console application
python main.py

# Test with sample requests
>> onboard new employee Test User
>> create marketing campaign for product launch
>> order laptop for new developer
>> status
>> help
>> quit
```

## Performance Considerations

### Response Times
- **Average response time**: 1-3 seconds per step
- **Complex tasks**: May take 5-10 seconds
- **Network latency**: Depends on Azure region

### Memory Usage
- **In-memory store**: Suitable for development/testing
- **Session data**: Limited by available RAM
- **Long-running sessions**: May require memory cleanup

### Scalability Limitations
- **Single-threaded**: Steps executed sequentially
- **Single session**: One user at a time
- **No persistence**: Data lost on restart

## Limitations

1. **Sequential Execution**: Steps are executed one at a time
2. **In-Memory Storage**: No persistence between sessions
3. **Single Session**: One user/session at a time
4. **Limited Error Recovery**: Basic retry mechanisms
5. **No Real Tool Integration**: Simulated tool responses
6. **No Authentication**: No user authentication system
7. **No Logging**: Limited logging capabilities

## Future Enhancements

### Short-term
1. **Parallel Step Execution**: Execute independent steps concurrently
2. **Enhanced Error Handling**: More sophisticated retry and fallback
3. **Better Logging**: Comprehensive logging system
4. **Configuration Management**: External configuration files

### Long-term
1. **Persistent Storage**: Database backend for memory store
2. **Multi-Session Support**: Handle multiple users simultaneously
3. **Real Tool Integration**: Connect to actual business systems
4. **Web Interface**: Optional web frontend
5. **Authentication**: User authentication and authorization
6. **Monitoring Dashboard**: Real-time monitoring
7. **Custom Agent Builder**: UI for creating custom agents

## Troubleshooting

### Common Issues

#### Authentication Errors
```bash
# Solution: Re-authenticate with Azure
az login
az account set --subscription "your-subscription-id"
```

#### Module Import Errors
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

#### Agent Timeout Errors
```bash
# Solution: Increase timeout in config.py
AGENT_TIMEOUT = 60  # Increase from 30 to 60 seconds
```

#### Memory Issues
```bash
# Solution: Restart application periodically
# Or implement memory cleanup in future versions
```

### Debug Mode

Enable debug mode for detailed logging:

```python
# In config.py
LOG_LEVEL = "DEBUG"

# Or set environment variable
export LOG_LEVEL=DEBUG
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest`
6. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add docstrings for public methods
- Keep functions focused and small

### Testing Requirements

- Unit tests for all new functionality
- Integration tests for agent interactions
- Manual testing with sample scenarios

## License

This project is licensed under the MIT License - see the LICENSE file for details.
