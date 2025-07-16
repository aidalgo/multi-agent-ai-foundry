# Console SK Directory Structure

```
src/console-sk/
├── main.py                 # Main console application
├── run.py                  # Application launcher with checks
├── setup.py                # Setup script for dependencies
├── test_setup.py           # Test script to verify setup
├── console_memory.py       # In-memory storage for console
├── utils_console.py        # Console utilities and agent factory
├── requirements.txt        # Python dependencies
├── .env.example           # Environment configuration template
├── README.md              # Documentation
├── STRUCTURE.md           # This file
└── backend/               # Essential backend components
    ├── __init__.py
    ├── app_config.py
    ├── event_utils.py
    ├── utils_date.py
    ├── models/
    │   ├── __init__.py
    │   └── messages_kernel.py
    ├── kernel_agents/
    │   ├── agent_base.py
    │   ├── hr_agent.py
    │   ├── marketing_agent.py
    │   ├── product_agent.py
    │   ├── procurement_agent.py
    │   ├── tech_support_agent.py
    │   ├── generic_agent.py
    │   ├── human_agent.py
    │   ├── planner_agent.py
    │   └── group_chat_manager.py
    ├── kernel_tools/
    │   ├── hr_tools.py
    │   ├── marketing_tools.py
    │   ├── product_tools.py
    │   ├── procurement_tools.py
    │   ├── tech_support_tools.py
    │   └── generic_tools.py
    └── context/
        ├── __init__.py
        └── cosmos_memory_kernel.py
```

## Key Files

### Core Application
- **main.py**: Main console application with interactive interface
- **run.py**: Launcher with environment checks and validation
- **setup.py**: Setup script for installing dependencies
- **test_setup.py**: Test script to verify configuration

### Console-Specific Components
- **console_memory.py**: In-memory storage replacing CosmosDB
- **utils_console.py**: Console utilities and simplified agent factory

### Backend Components (Essential)
- **backend/**: Essential backend functionality from main application
- **models/**: Data models and message types
- **kernel_agents/**: All agent implementations
- **kernel_tools/**: Tools and functions for each agent
- **context/**: Memory and storage contexts

## Architecture Notes

### Removed Files
The following files were removed from the backend as they were not used by the console application:
- **config_kernel.py**: Wrapper around app_config.py (not needed)
- **utils_kernel.py**: Complex utilities not used by console app
- **kernel_agents/agent_factory.py**: Replaced by ConsoleAgentFactory
- **kernel_agents/agent_utils.py**: Utility functions not used by console app

### Console vs Backend Agent Factory
The console application uses its own simplified agent factory (`ConsoleAgentFactory` in `utils_console.py`) instead of the backend's `AgentFactory` for better isolation and simpler initialization.

## Dependencies

The console application uses the same dependencies as the main application:
- Semantic Kernel
- Azure AI Projects
- Azure Identity
- Azure Cosmos (optional, uses in-memory storage)

## Usage Flow

1. Run `python setup.py` to install dependencies
2. Configure `.env` file with Azure credentials
3. Run `python test_setup.py` to verify setup
4. Run `python main.py` to start the console application
