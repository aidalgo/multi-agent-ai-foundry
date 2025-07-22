# Multi-Agent Custom Automation Engine - Console Demo

Welcome to the *Multi-Agent Custom Automation Engine* console demonstration, designed to showcase how AI agents can automate complex organizational tasks through an interactive command-line interface. This console demo provides a hands-on way to explore AI-driven orchestration systems that coordinate multiple specialized agents to accomplish various business processes.

When dealing with complex organizational tasks, users often face significant challenges, including coordinating across multiple departments, maintaining consistency in processes, and ensuring efficient resource utilization.

The Multi-Agent Custom Automation Engine console demo allows users to input tasks through an interactive console and see how they are automatically processed by a group of AI agents, each specialized in different aspects of business operations.

<br/>

<div align="center">
  
[**DEMO OVERVIEW**](#demo-overview) \| [**GETTING STARTED**](#getting-started) \| [**BUSINESS SCENARIO**](#business-scenario) \| [**DOCUMENTATION**](#documentation)

</div>
<br/>

<h2><img src="./docs/images/readme/solution-overview.png" width="48" />
Demo overview
</h2>

This console demo leverages Azure OpenAI Service and Azure AI Foundry to create an intelligent automation pipeline through an interactive command-line interface. It demonstrates a multi-agent approach where specialized AI agents work together to plan, execute, and validate tasks based on user input.

**🎯 This is a demonstration application designed for:**
- Learning about multi-agent AI systems
- Exploring Azure AI capabilities
- Prototyping automation workflows
- Understanding agent coordination patterns

**📺 Console Interface Architecture**
```
User Input → Planner Agent → Specialized Agents → Coordinated Response
    ↓              ↓               ↓                    ↓
 Task Entry → Plan Creation → Task Execution → Results Display
```

### Console Demo Architecture
The original web application architecture diagrams below show the full solution concept. This console demo implements the core multi-agent orchestration in a simplified, interactive format.

|![image](./docs/images/readme/architecture.png)|
|---|
|*Original web application architecture (reference)*|

### Agent Interaction Flow
|![image](./docs/images/readme/agent_flow.png)|
|---|
|*Multi-agent coordination pattern (implemented in console)*|

### How to customize this demo
If you'd like to customize the console demo for your specific use cases:

[Customization Guide](./docs/CustomizeSolution.md)

<br/>

### Additional resources

[Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)

[Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)

<br/>

### Key demo features
<details open>
  <summary>Click to learn more about what this console demo demonstrates</summary>

  - **Multi-Agent Coordination** <br/>
  Shows how different AI agents (HR, Marketing, Product, etc.) work together to accomplish complex tasks.
  
  - **Interactive Learning** <br/>
  Provides hands-on experience with AI agent orchestration through a simple console interface.

  - **Azure AI Integration** <br/>
  Demonstrates real integration with Azure OpenAI Service and Azure AI Foundry.

  - **Customizable Framework** <br/>
  Serves as a foundation for building your own multi-agent solutions.

</details>

<br /><br />
<h2><img src="./docs/images/readme/quick-deploy.png" width="48" />
Getting started
</h2>

### 🚀 Run the Console Demo

**Prerequisites:**
- Azure subscription with Azure OpenAI access
- Python 3.8+
- Azure CLI

**Quick Start:**
1. Set up your Azure resources (Azure OpenAI + AI Foundry)
2. Configure your environment
3. Run the console application

[� **Complete Setup Guide**](./SETUP.md)

### 💡 Try Sample Prompts
Once running, try these examples:
- "Launch a new marketing campaign"
- "Help me onboard a new employee"
- "Plan a product launch strategy"

[📝 **More Examples**](./docs/SampleQuestions.md)

> ℹ️ **Note: Azure OpenAI Quota**
 <br/>Make sure you have sufficient Azure OpenAI quota in your subscription. You can check your quota in the Azure portal under your Azure OpenAI resource.

<br/>

### Requirements and Costs

**Azure Requirements:**
- [Azure subscription](https://azure.microsoft.com/free/) with permissions to create resources
- Access to Azure OpenAI Service
- Azure AI Foundry project

**Supported Regions:**
East US, East US2, Japan East, UK South, Sweden Central (check [Azure Products by Region](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/table) for current availability)

**Cost Structure:**
This console demo uses pay-per-use Azure services:

| Service | Purpose | Cost |
|---|---|---|
| [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/) | Powers the AI agents | [Usage-based pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |
| [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/) | Agent project infrastructure | [Minimal project costs](https://azure.microsoft.com/pricing/details/machine-learning/) |

💡 **Cost Tip:** Since this runs locally, you only pay for AI model usage during console sessions.

<br/>



<br /><br />
<h2><img src="./docs/images/readme/business-scenario.png" width="48" />
Business Scenario
</h2>

### 🎯 Console Demo Experience

**The Challenge:**
Imagine you're a business manager who needs to coordinate a complex project that involves multiple departments. Traditionally, this would require:
- Scheduling meetings with HR, Marketing, Product teams
- Manually tracking action items across departments  
- Ensuring consistent communication and follow-up
- Managing dependencies between different workstreams

**The Console Demo:**
Instead, you simply open a terminal and type:
```
> "Help me launch a new marketing campaign for our Q2 product release"
```

**What Happens Next:**
1. **Planner Agent** analyzes your request and creates a coordinated plan
2. **Marketing Agent** suggests campaign strategies and channels
3. **Product Agent** provides technical specifications and positioning
4. **HR Agent** identifies team resource needs
5. **Procurement Agent** estimates budget requirements
6. **All agents coordinate** to deliver a comprehensive, actionable plan

### 💼 Real-World Applications

This console demo showcases automation patterns applicable to:

- **Project Planning**: Multi-department initiative coordination
- **Process Automation**: Standardized workflow execution
- **Resource Allocation**: Cross-functional team planning  
- **Compliance Management**: Multi-stakeholder review processes
- **Strategic Planning**: Coordinated business analysis

### 🔄 Interactive Learning

The console interface lets you:
- **Experiment** with different prompt styles
- **Observe** how agents coordinate and specialize
- **Learn** about multi-agent system patterns
- **Prototype** your own automation scenarios

### Business value demonstration
<details>
  <summary>Click to learn more about what this demo showcases</summary>

  - **Process Automation Patterns** <br/>
  Demonstrates how AI can coordinate complex, multi-step business processes.

  - **Agent Specialization** <br/>
  Shows how different agents can be optimized for specific domains (HR, Marketing, Finance, etc.).

  - **Scalable Architecture** <br/>
  Provides a foundation that can be extended for production use cases.

  - **Cost-Effective Exploration** <br/>
  Allows organizations to experiment with multi-agent AI without infrastructure overhead.

</details>

<br /><br />

<h2><img src="./docs/images/readme/supporting-documentation.png" width="48" />
Documentation
</h2>

### 📚 Available Guides

| Guide | Purpose |
|---|---|
| [Setup Guide](./SETUP.md) | Complete setup instructions |
| [Sample Questions](./docs/SampleQuestions.md) | Example prompts to try |
| [Customization Guide](./docs/CustomizeSolution.md) | How to modify for your use case |
| [Azure Account Setup](./docs/AzureAccountSetUp.md) | Azure prerequisites |
| [Console Technical Docs](./src/console-sk/README.md) | Detailed technical documentation |

### 🗂️ Architecture Reference
For those interested in the full web application this demo is based on, see [archived documentation](./docs/archived/).

### 🔒 Security Considerations

This console demo uses:
- **Azure Default Credentials** for local authentication
- **Azure OpenAI Service** with built-in responsible AI features
- **Local execution** - no web endpoints or external access

For production implementations, consider:
- Proper authentication and authorization
- Network security and access controls  
- Audit logging and monitoring
- Data encryption and privacy controls

<br/>