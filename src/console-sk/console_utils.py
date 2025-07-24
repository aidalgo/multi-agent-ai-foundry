"""
Console utility functions for formatting and display.
Handles text formatting, status display, and console-specific operations.
"""

import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class ConsoleFormatter:
    """Handles formatting for console display."""
    
    @staticmethod
    def format_agent_response(response: str) -> str:
        """
        Format agent response for console display.
        Removes markdown formatting to make text more readable in terminal.
        
        Args:
            response: Raw agent response text
            
        Returns:
            Formatted text suitable for console display
        """
        if not response:
            return ""
        
        # Remove markdown formatting for console display
        formatted = response
        markdown_replacements = {
            "**": "",      # Bold
            "*": "",       # Italic
            "# ": "",      # H1
            "## ": "",     # H2
            "### ": "",    # H3
            "#### ": "",   # H4
            "##### ": "",  # H5
            "###### ": "", # H6
        }
        
        for markdown, replacement in markdown_replacements.items():
            formatted = formatted.replace(markdown, replacement)
        
        return formatted.strip()
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        """
        Truncate text to a maximum length with ellipsis.
        
        Args:
            text: Text to truncate
            max_length: Maximum allowed length
            
        Returns:
            Truncated text with ellipsis if needed
        """
        if len(text) <= max_length:
            return text
        return text[:max_length - 3] + "..."
    
    @staticmethod
    def format_step_status(status: str) -> str:
        """
        Format step status with visual indicators.
        
        Args:
            status: Status string
            
        Returns:
            Status with emoji indicator
        """
        status_symbols = {
            "planned": "⏳",
            "awaiting_feedback": "⏸️",
            "approved": "✅",
            "rejected": "❌",
            "action_requested": "🔄",
            "completed": "✅",
            "failed": "❌",
            "in_progress": "⚡",
            "pending": "⏳",
            "cancelled": "🚫",
        }
        symbol = status_symbols.get(status.lower(), "❓")
        return f"{symbol} {status.title()}"
    
    @staticmethod
    def format_agent_name(agent_type: str) -> str:
        """
        Format agent type name for display.
        
        Args:
            agent_type: Agent type identifier
            
        Returns:
            Human-readable agent name
        """
        agent_names = {
            "Hr_Agent": "HR Agent",
            "Marketing_Agent": "Marketing Agent",
            "Product_Agent": "Product Agent",
            "Procurement_Agent": "Procurement Agent",
            "Tech_Support_Agent": "Tech Support Agent",
            "Generic_Agent": "Generic Agent",
            "Human_Agent": "Human Agent",
            "Planner_Agent": "Planner Agent",
            "Group_Chat_Manager": "Group Chat Manager",
        }
        return agent_names.get(agent_type, agent_type.replace("_", " ").title())

    @staticmethod
    def format_list_items(items: list, bullet: str = "•") -> str:
        """
        Format a list of items with bullets.
        
        Args:
            items: List of items to format
            bullet: Bullet character to use
            
        Returns:
            Formatted list string
        """
        if not items:
            return ""
        
        return "\n".join(f"{bullet} {item}" for item in items)

    @staticmethod
    def create_separator(length: int = 60, char: str = "-") -> str:
        """
        Create a separator line.
        
        Args:
            length: Length of the separator
            char: Character to use for separator
            
        Returns:
            Separator string
        """
        return char * length

    @staticmethod
    def format_progress(current: int, total: int, width: int = 20) -> str:
        """
        Create a text-based progress bar.
        
        Args:
            current: Current progress value
            total: Total progress value
            width: Width of progress bar in characters
            
        Returns:
            Progress bar string
        """
        if total == 0:
            return f"[{'=' * width}] 0%"
        
        percentage = current / total
        filled = int(width * percentage)
        bar = "=" * filled + "-" * (width - filled)
        percent = int(percentage * 100)
        
        return f"[{bar}] {percent}%"


class ConsoleColors:
    """ANSI color codes for terminal output."""
    
    # Reset
    RESET = "\033[0m"
    
    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    @classmethod
    def colorize(cls, text: str, color: str) -> str:
        """Apply color to text."""
        return f"{color}{text}{cls.RESET}"
    
    @classmethod
    def success(cls, text: str) -> str:
        """Format success message."""
        return cls.colorize(text, cls.GREEN)
    
    @classmethod
    def error(cls, text: str) -> str:
        """Format error message."""
        return cls.colorize(text, cls.RED)
    
    @classmethod
    def warning(cls, text: str) -> str:
        """Format warning message."""
        return cls.colorize(text, cls.YELLOW)
    
    @classmethod
    def info(cls, text: str) -> str:
        """Format info message."""
        return cls.colorize(text, cls.BLUE)


# Backward compatibility aliases
ConsoleUtils = ConsoleFormatter  # For existing code that uses ConsoleUtils
