# Console Setup Guide

This guide will help you set up and run the Multi-Agent Custom Automation Engine console application.

## Prerequisites

1. **Azure Account**: Sign up for a [free Azure account](https://azure.microsoft.com/free/)
2. **Python 3.8+**: Install Python from [python.org](https://www.python.org/downloads/)
3. **Azure CLI**: Install from [Microsoft Docs](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
4. **Azure AI Resources**: Set up Azure OpenAI and Azure AI Foundry (see below)

## Azure Setup

### 1. Azure Account Setup
Follow the [Azure Account Setup Guide](./docs/AzureAccountSetUp.md) to ensure you have the necessary permissions.

### 2. Azure OpenAI Service
1. Create an Azure OpenAI resource in the Azure portal
2. Deploy a GPT-4o model
3. Note your endpoint and deployment name

### 3. Azure AI Foundry Project
1. Navigate to [Azure AI Foundry](https://ai.azure.com/)
2. Create a new AI Project
3. Note your project details (subscription, resource group, project name)

For quota management, see [Azure GPT Quota Settings](./docs/AzureGPTQuotaSettings.md).

## Local Setup

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd multi-agent-ai-foundry/src/console-sk
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Copy the example environment file and update it with your Azure details:

```bash
cp .env.example .env
```

Edit `.env` with your Azure configuration:
```bash
# Azure AI Configuration
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_AI_SUBSCRIPTION_ID=your-subscription-id
AZURE_AI_RESOURCE_GROUP=your-resource-group
AZURE_AI_PROJECT_NAME=your-project-name
AZURE_AI_AGENT_ENDPOINT=https://your-project.api.azureml.ms
```

### 4. Authenticate with Azure
```bash
az login
```

### 5. Test Setup
```bash
python test_setup.py
```

You should see all tests pass:
```
Console MACAE Test Suite
========================================
Testing imports...
✅ Azure Identity import successful
✅ App Config import successful
✅ Models import successful
✅ Console Memory import successful
✅ Console Utils import successful

Testing environment setup...
✅ AZURE_OPENAI_ENDPOINT is set
✅ AZURE_OPENAI_DEPLOYMENT_NAME is set
✅ AZURE_AI_SUBSCRIPTION_ID is set
✅ AZURE_AI_RESOURCE_GROUP is set
✅ AZURE_AI_PROJECT_NAME is set
✅ AZURE_AI_AGENT_ENDPOINT is set

Testing Azure authentication...
✅ DefaultAzureCredential created successfully

Results: 3/3 tests passed
✅ All tests passed! Console application should work.
```

## Running the Application

### Start the Console Application
```bash
python main.py
```

### Try Sample Prompts
Once the application starts, try these sample prompts:
- "Launch a new marketing campaign"
- "Procure new office equipment"  
- "Onboard a new employee named John Smith"

See [Sample Questions](./docs/SampleQuestions.md) for more examples.

## Troubleshooting

### Common Issues

**Import Errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct directory: `src/console-sk`

**Azure Authentication Errors**
- Run `az login` to authenticate
- Verify your Azure account has proper permissions
- Check that your subscription has Azure OpenAI quota

**Environment Configuration**
- Verify all required environment variables are set in `.env`
- Check that your Azure resources exist and are properly configured
- Ensure your OpenAI deployment is active

**Model Access Issues**
- Verify your Azure OpenAI deployment name matches the environment variable
- Check quota availability in Azure AI Foundry
- Ensure the model is deployed and accessible

### Getting Help

1. Check the console output for specific error messages
2. Run `python test_setup.py` to verify setup
3. Review [Azure Account Setup](./docs/AzureAccountSetUp.md) for permission issues
4. See [Customization Guide](./docs/CustomizeSolution.md) for advanced configuration

## Next Steps

- Explore [Sample Questions](./docs/SampleQuestions.md) to understand capabilities
- Read the [Customization Guide](./docs/CustomizeSolution.md) to add your own agents
- Check the [Console README](./src/console-sk/README.md) for detailed technical information
