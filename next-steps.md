# Next Steps - Console Multi-Agent System

## Getting Started

### 1. **Complete Setup**
If you haven't already, follow the [Setup Guide](./SETUP.md) to configure your environment and Azure resources.

### 2. **Run Your First Session**
```bash
cd src/console-sk
python main.py
```

Try these sample prompts:
- "Launch a new marketing campaign"
- "Help me onboard a new employee"
- "Plan a product launch strategy"

### 3. **Explore Capabilities**
Review [Sample Questions](./docs/SampleQuestions.md) to understand what the multi-agent system can do.

## Customization Options

### **Add Your Own Agents**
Follow the [Customization Guide](./docs/CustomizeSolution.md) to:
- Create domain-specific agents
- Add custom tools and functions
- Integrate with your existing systems

### **Environment Configuration**
Customize settings in `src/console-sk/.env`:
- Model selection and parameters
- Custom API endpoints
- Company-specific configurations

### **Testing and Validation**
Use the built-in test suite:
```bash
cd src/console-sk
python test_setup.py
```

## Development Workflow

### **Local Development**
1. Make changes to agents, tools, or configuration
2. Test with `python test_setup.py`
3. Run interactive sessions with `python main.py`
4. Iterate based on results

### **Production Considerations**
For production use, consider:
- Implementing persistent storage (database)
- Adding authentication and authorization
- Creating web or API interfaces
- Implementing monitoring and logging
- Adding proper error handling and retry logic

## Advanced Features

### **Memory and Context**
The console application maintains conversation history in memory. For persistent storage across sessions, consider integrating with Azure Cosmos DB or other databases.

### **Multi-Agent Orchestration**
Explore how agents coordinate:
- Planner agent creates execution plans
- Specialized agents handle specific tasks
- Group chat manager orchestrates communication
- Human-in-the-loop for validation

### **Tool Integration**
Add real business functions:
- Replace stub functions with actual implementations
- Integrate with your APIs and systems
- Add validation and error handling

## Troubleshooting

### **Common Issues**
- **Authentication**: Ensure `az login` is completed
- **Quota**: Check Azure OpenAI quota availability
- **Dependencies**: Verify all Python packages are installed
- **Configuration**: Double-check environment variables

### **Getting Help**
1. Run `python test_setup.py` to diagnose issues
2. Check console logs for specific error messages
3. Review Azure portal for resource status
4. Consult [Azure Account Setup](./docs/AzureAccountSetUp.md) for permission issues

## Community and Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check `src/console-sk/README.md` for technical details
- **Examples**: See `docs/SampleQuestions.md` for usage examples

## Migration to Production

When ready to deploy beyond console testing:

1. **Architecture**: Design for your production scale and requirements
2. **Storage**: Implement persistent data storage
3. **Authentication**: Add proper user authentication
4. **Interface**: Build web, mobile, or API interfaces
5. **Monitoring**: Implement comprehensive logging and monitoring
6. **Security**: Follow security best practices for your deployment

The console version provides the foundation - extend it to meet your production needs!

More information about [Bicep](https://aka.ms/bicep) language.

### Build from source (no Dockerfile)

#### Build with Buildpacks using Oryx

If your project does not contain a Dockerfile, we will use [Buildpacks](https://buildpacks.io/) using [Oryx](https://github.com/microsoft/Oryx/blob/main/doc/README.md) to create an image for the services in `azure.yaml` and get your containerized app onto Azure.

To produce and run the docker image locally:

1. Run `azd package` to build the image.
2. Copy the *Image Tag* shown.
3. Run `docker run -it <Image Tag>` to run the image locally.

#### Exposed port

Oryx will automatically set `PORT` to a default value of `80` (port `8080` for Java). Additionally, it will auto-configure supported web servers such as `gunicorn` and `ASP .NET Core` to listen to the target `PORT`. If your application already listens to the port specified by the `PORT` variable, the application will work out-of-the-box. Otherwise, you may need to perform one of the steps below:

1. Update your application code or configuration to listen to the port specified by the `PORT` variable
1. (Alternatively) Search for `targetPort` in a .bicep file under the `infra/app` folder, and update the variable to match the port used by the application.

## Billing

Visit the *Cost Management + Billing* page in Azure Portal to track current spend. For more information about how you're billed, and how you can monitor the costs incurred in your Azure subscriptions, visit [billing overview](https://learn.microsoft.com/azure/developer/intro/azure-developer-billing).

## Troubleshooting

Q: I visited the service endpoint listed, and I'm seeing a blank page, a generic welcome page, or an error page.

A: Your service may have failed to start, or it may be missing some configuration settings. To investigate further:

1. Run `azd show`. Click on the link under "View in Azure Portal" to open the resource group in Azure Portal.
2. Navigate to the specific Container App service that is failing to deploy.
3. Click on the failing revision under "Revisions with Issues".
4. Review "Status details" for more information about the type of failure.
5. Observe the log outputs from Console log stream and System log stream to identify any errors.
6. If logs are written to disk, use *Console* in the navigation to connect to a shell within the running container.

For more troubleshooting information, visit [Container Apps troubleshooting](https://learn.microsoft.com/azure/container-apps/troubleshooting). 

### Additional information

For additional information about setting up your `azd` project, visit our official [docs](https://learn.microsoft.com/azure/developer/azure-developer-cli/make-azd-compatible?pivots=azd-convert).
