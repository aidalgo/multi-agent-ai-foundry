# Sample Questions

To help you get started with the console application, here are some **Sample Prompts** you can try:

1. Run each of the following sample prompts and verify that a plan is generated:
   - Launch a new marketing campaign
   - Procure new office equipment
   - Initiate a new product launch
     
2. Run the **Onboard employee** prompt:
   - Remove the employee name from the prompt to test how the solution handles missing information.
   - The solution should ask for the missing detail before proceeding.

3. Try running known **RAI test prompts** to confirm safeguard behavior:
   - You should see a message indicating that a plan could not be generated due to policy restrictions.

## How to Use

1. Navigate to the console-sk directory:
   ```bash
   cd src/console-sk
   ```

2. Run the console application:
   ```bash
   python main.py
   ```

3. Enter one of the sample prompts above when prompted

4. Observe how the multi-agent system:
   - Analyzes your request
   - Creates a plan with multiple agents
   - Coordinates between specialized agents (HR, Marketing, Product, etc.)
   - Provides a structured response

_This structured approach helps ensure the system handles prompts gracefully, verifies plan generation flows, and confirms RAI protections are working as intended._
