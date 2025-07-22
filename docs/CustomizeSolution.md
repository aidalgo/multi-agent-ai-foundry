# Customizing the Console Multi-Agent System

This guide explains how to customize the console-based Multi-Agent Custom Automation Engine for your specific use cases.

## Overview

The console application provides a simplified but powerful multi-agent system that you can extend and customize. The example solution demonstrates how multiple specialized agents work together to accomplish complex tasks through an interactive command-line interface.

## Key Customization Areas

### 1. **Agent Definitions** (`src/console-sk/agents/`)

Each agent has specific roles and capabilities. You can:
- Modify existing agent prompts and behaviors
- Add new specialized agents for your domain
- Customize agent tools and functions

### 2. **Tools and Functions** (`src/console-sk/tools/`)

Define the actual business logic that agents can execute:
- Replace stub functions with real implementations
- Add new tools for your specific workflows  
- Integrate with your existing systems and APIs

### 3. **Configuration** (`src/console-sk/config.py`)

Customize Azure AI settings:
- Model selection and parameters
- Authentication configuration
- Environment-specific settings

### 4. **Data Models** (`src/console-sk/models.py`)

Extend data structures for your domain:
- Add custom message types
- Define domain-specific data models
- Enhance agent communication protocols

## Adding a New Agent

To add a new agent to the system:

### Step 1: Define Agent Tools

Create functions your agent will use:

```python
# In src/console-sk/tools/finance_tools.py
async def calculate_budget(amount: float, category: str) -> str:
    """Calculate budget allocation for a category."""
    # Implement your business logic here
    return f"Allocated ${amount} to {category}"

async def generate_financial_report(period: str) -> str:
    """Generate a financial report for the specified period."""
    # Implement reporting logic
    return f"Financial report for {period} generated"
```

### Step 2: Create Agent Class

```python
# In src/console-sk/agents/finance_agent.py
from semantic_kernel.kernel import Kernel
from semantic_kernel.functions import kernel_function

class FinanceAgent:
    def __init__(self, kernel: Kernel):
        self.kernel = kernel
        self.name = "Finance Agent"
        self.role = "Financial planning and analysis"
    
    @kernel_function(name="budget_calculation")
    async def calculate_budget(self, amount: str, category: str) -> str:
        # Implementation here
        pass
```

### Step 3: Register the Agent

Add your agent to the agent factory in `src/console-sk/utils.py`:

```python
from agents.finance_agent import FinanceAgent

class ConsoleAgentFactory:
    def create_agents(self):
        agents = {
            # ... existing agents
            AgentType.FINANCE: FinanceAgent(self.kernel),
        }
        return agents
```

### Step 4: Update Agent Types

Add your new agent type to `src/console-sk/models.py`:

```python
class AgentType(Enum):
    # ... existing types
    FINANCE = "finance"
```

## Customization Examples

### Example 1: Integration with External APIs

```python
# In tools/external_integration.py
import httpx

async def call_external_api(endpoint: str, data: dict) -> str:
    """Integrate with your existing systems."""
    async with httpx.AsyncClient() as client:
        response = await client.post(endpoint, json=data)
        return response.json()
```

### Example 2: Custom Validation Logic

```python
# In agents/compliance_agent.py
async def validate_request(self, request: str) -> bool:
    """Add your compliance validation logic."""
    # Check against company policies
    # Validate against regulatory requirements
    return is_compliant
```

### Example 3: Domain-Specific Prompts

Customize agent prompts for your industry:

```python
SYSTEM_PROMPT = '''
You are a specialized healthcare agent focused on patient care coordination.
Your role is to:
- Ensure HIPAA compliance in all communications
- Coordinate between medical departments
- Prioritize patient safety and care quality
...
'''
```

## Environment Configuration

Update your `.env` file with custom settings:

```bash
# Azure AI Configuration
AZURE_OPENAI_ENDPOINT=your-endpoint
AZURE_OPENAI_DEPLOYMENT_NAME=your-model
AZURE_AI_PROJECT_NAME=your-project

# Custom Application Settings
CUSTOM_API_ENDPOINT=https://your-api.com
COMPANY_NAME=Your Company
INDUSTRY_SPECIFIC_SETTING=value
```

## Testing Your Customizations

1. **Unit Tests**: Create tests for your custom tools and agents
2. **Integration Tests**: Test agent interactions and workflows
3. **Console Testing**: Use the `test_setup.py` script to verify configuration

```bash
cd src/console-sk
python test_setup.py
```

## Best Practices

### Security
- Never hardcode sensitive information
- Use Azure Key Vault for secrets in production
- Validate all external inputs

### Performance  
- Keep agent tools focused and efficient
- Use async patterns for I/O operations
- Monitor token usage and costs

### Maintainability
- Document your custom agents and tools
- Use clear naming conventions
- Separate business logic from agent orchestration

## Deployment Considerations

The console application is designed for:
- Local development and testing
- Proof of concept demonstrations
- Development environment experimentation

For production use, consider:
- Implementing proper logging and monitoring
- Adding authentication and authorization
- Creating a web or API interface
- Using persistent storage (database)
- Implementing proper error handling and retry logic

## Next Steps

1. **Start Small**: Begin by customizing existing agents
2. **Add Tools**: Implement real business functions
3. **Test Thoroughly**: Validate your customizations work correctly
4. **Scale Up**: Add more agents and complex workflows
5. **Production Ready**: Consider architecture for production deployment

For more technical details about the original web application architecture, see the archived documentation in `docs/archived/`.
