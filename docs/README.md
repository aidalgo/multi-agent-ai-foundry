# Documentation Structure

This document outlines the current documentation structure for the console-based Multi-Agent Custom Automation Engine.

## Current Documentation

### **Main Files**
- **[README.md](../README.md)** - Project overview and introduction
- **[SETUP.md](../SETUP.md)** - Complete setup guide for getting started
- **[next-steps.md](../next-steps.md)** - What to do after initial setup

### **Documentation (`docs/`)**
- **[AzureAccountSetUp.md](./AzureAccountSetUp.md)** - Azure account configuration and permissions
- **[AzureGPTQuotaSettings.md](./AzureGPTQuotaSettings.md)** - Managing Azure OpenAI quota
- **[CustomizeSolution.md](./CustomizeSolution.md)** - Guide for customizing agents and tools
- **[SampleQuestions.md](./SampleQuestions.md)** - Example prompts to try with the console app
- **[TRANSPARENCY_FAQ.md](./TRANSPARENCY_FAQ.md)** - Responsible AI information

### **Console Application (`src/console-sk/`)**
- **[README.md](../src/console-sk/README.md)** - Detailed technical documentation for the console app
- **[.env.example](../src/console-sk/.env.example)** - Environment configuration template
- Additional agent, tool, and configuration documentation

## Archived Documentation (`docs/archived/`)

The following documentation was moved to the archived folder as it relates to the previous web application version:

- **DeploymentGuide.md** - Azure deployment for web application
- **LocalDeployment.md** - Dev container setup for web development  
- **ManualAzureDeployment.md** - Manual Azure deployment process
- **azure_app_service_auth_setup.md** - App Service authentication
- **CustomizingAzdParameters.md** - Azure Developer CLI parameters
- **DeleteResourceGroup.md** - Resource cleanup instructions
- **quota_check.md** - Quota checking for web deployment
- **re-use-log-analytics.md** - Log Analytics configuration
- **create_new_app_registration.md** - Azure AD app registration
- **NON_DEVCONTAINER_SETUP.md** - Alternative development setup
- **CustomizeSolution.md** (original) - Web application customization guide

## Quick Navigation

### **I want to...**

**Get Started**
→ [SETUP.md](../SETUP.md)

**Try the Console App**  
→ [SampleQuestions.md](./SampleQuestions.md)

**Customize for My Use Case**
→ [CustomizeSolution.md](./CustomizeSolution.md)

**Understand Technical Details**
→ [Console README](../src/console-sk/README.md)

**Troubleshoot Issues**
→ [SETUP.md - Troubleshooting](../SETUP.md#troubleshooting)

**Learn About Previous Web Version**
→ [Archived Documentation](./archived/)

## Documentation Maintenance

This documentation structure is designed for the console-only version. Key principles:

1. **Simplicity**: Focus on what's needed for console application
2. **Clarity**: Clear paths for different user goals
3. **Preservation**: Archive rather than delete previous documentation
4. **Practicality**: Emphasis on getting started and customizing

For questions or improvements to documentation, please open an issue or submit a pull request.
