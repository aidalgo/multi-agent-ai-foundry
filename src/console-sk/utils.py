"""
Utility functions and agent factory for the console application.
This file now imports from separate modules for better organization.

For backward compatibility, this file re-exports the main classes.
In new code, prefer importing directly from:
- agent_factory.py for ConsoleAgentFactory
- console_utils.py for ConsoleFormatter/ConsoleUtils
"""

# Import for backward compatibility
from agent_factory import ConsoleAgentFactory
from console_utils import ConsoleFormatter, ConsoleUtils, ConsoleColors

# Re-export for backward compatibility
__all__ = [
    'ConsoleAgentFactory',
    'ConsoleFormatter', 
    'ConsoleUtils',
    'ConsoleColors'
]
