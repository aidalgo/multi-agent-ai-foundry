# Console Multi-Agent Custom Automation Engine

A simplified console version of the Multi-Agent Custom Automation Engine using Semantic Kernel and Azure AI Foundry agents.

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

## Usage

1. **Run the console application**:
   ```bash
   python main.py
   ```

2. **Alternative launcher**:
   ```bash
   python run.py
   ```

3. **Available commands**:
   - Type your task/goal and press Enter
   - Type `status` to see current plan status
   - Type `help` to see available commands
   - Type `quit` or `exit` to exit

4. **Example interaction**:
   ```
   >> Help me plan a product launch for a new mobile app
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
   
   Do you want to execute this plan? (y/n): y
   ```

## Architecture

The console application maintains the same multi-agent architecture as the full application:

```
Console App
├── Planner Agent        # Creates and manages plans
├── Specialized Agents   # HR, Marketing, Product, Procurement, Tech Support
├── Generic Agent        # Handles general tasks
├── Human Agent          # Human interaction interface
├── Group Chat Manager   # Manages group conversations
└── Console Memory       # In-memory storage for console sessions
```

## Key Components

- **`main.py`**: Main console application entry point
- **`console_memory.py`**: In-memory storage implementation
- **`utils_console.py`**: Console-specific utilities and agent factory
- **`backend/`**: Essential backend components from the main application

> **Note**: The console application uses a streamlined version of the backend components. Non-essential files like `config_kernel.py`, `utils_kernel.py`, `agent_factory.py`, and `agent_utils.py` have been removed as they are not used by the console application. Instead, the console uses its own simplified `ConsoleAgentFactory` for better isolation and simpler initialization.

## Features Comparison

| Feature | Full Application | Console Application |
|---------|------------------|-------------------|
| Multi-Agent System | ✅ | ✅ |
| Semantic Kernel | ✅ | ✅ |
| Azure AI Foundry | ✅ | ✅ |
| Web Interface | ✅ | ❌ |
| CosmosDB Storage | ✅ | ❌ (In-memory) |
| Real-time Updates | ✅ | ❌ |
| Authentication | Web Auth | Default Azure Credentials |
| Deployment | Container Apps | Local Only |

## Troubleshooting

1. **Authentication Issues**:
   ```bash
   az login
   az account show  # Verify correct subscription
   ```

2. **Import Errors**:
   - Ensure you're running from the `console-sk` directory
   - Check that all backend files are properly copied

3. **Azure AI Foundry Issues**:
   - Verify your AI project is deployed and accessible
   - Check that the endpoint URL is correct

## Development

The console application uses the same agent implementations as the full application but with simplified initialization and in-memory storage. This makes it perfect for:

- Testing agent interactions
- Developing new agents
- Debugging agent behavior
- Demonstrating the multi-agent system

## Next Steps

- Add more sophisticated console UI
- Implement persistent storage options
- Add configuration management
- Create agent performance monitoring
- Add batch processing capabilities

## Support

For issues and questions, please refer to the main project documentation or create an issue in the repository.
