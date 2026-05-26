"""Base class for all hacking tools in the hackingtool suite.

This module provides the foundational structure that all tool categories
and individual tools should inherit from.
"""

import os
import subprocess
import shutil
from abc import ABC, abstractmethod
from typing import Optional


class BaseTool(ABC):
    """Abstract base class for all hacking tools."""

    def __init__(self, name: str, description: str, install_command: Optional[str] = None,
                 repo_url: Optional[str] = None):
        """
        Initialize a tool instance.

        Args:
            name: The display name of the tool.
            description: A brief description of what the tool does.
            install_command: Shell command to install the tool (if applicable).
            repo_url: GitHub/GitLab repository URL for cloning.
        """
        self.name = name
        self.description = description
        self.install_command = install_command
        self.repo_url = repo_url

    @abstractmethod
    def run(self) -> None:
        """Execute the tool. Must be implemented by subclasses."""
        pass

    def is_installed(self) -> bool:
        """Check whether the tool binary is available on PATH."""
        return shutil.which(self.name.lower()) is not None

    def install(self) -> bool:
        """
        Attempt to install the tool using the provided install command or repo URL.

        Returns:
            True if installation succeeded, False otherwise.
        """
        if self.is_installed():
            print(f"[*] {self.name} is already installed.")
            return True

        if self.repo_url:
            return self._clone_repo()

        if self.install_command:
            return self._run_install_command()

        print(f"[!] No installation method defined for {self.name}.")
        return False

    def _clone_repo(self) -> bool:
        """Clone the tool's repository into /opt/."""
        dest = f"/opt/{self.name.lower().replace(' ', '_')}"
        if os.path.exists(dest):
            print(f"[*] Repository already cloned at {dest}.")
            return True
        try:
            print(f"[*] Cloning {self.repo_url} into {dest} ...")
            subprocess.run(["git", "clone", self.repo_url, dest], check=True)
            print(f"[+] Successfully cloned {self.name}.")
            return True
        except subprocess.CalledProcessError as exc:
            print(f"[!] Failed to clone {self.name}: {exc}")
            return False

    def _run_install_command(self) -> bool:
        """Run the shell install command for the tool."""
        try:
            print(f"[*] Installing {self.name} ...")
            subprocess.run(self.install_command, shell=True, check=True)
            print(f"[+] Successfully installed {self.name}.")
            return True
        except subprocess.CalledProcessError as exc:
            print(f"[!] Installation failed for {self.name}: {exc}")
            return False

    def __str__(self) -> str:
        status = "installed" if self.is_installed() else "not installed"
        return f"{self.name} [{status}] — {self.description}"


class ToolCategory(ABC):
    """Abstract base class representing a category of tools."""

    def __init__(self, name: str, description: str):
        """
        Initialize a tool category.

        Args:
            name: Display name of the category.
            description: Short description of the category's purpose.
        """
        self.name = name
        self.description = description
        self.tools: list[BaseTool] = []

    def add_tool(self, tool: BaseTool) -> None:
        """Register a tool within this category."""
        self.tools.append(tool)

    def display_menu(self) -> None:
        """Print a numbered menu of all tools in this category."""
        print(f"\n{'='*50}")
        print(f"  {self.name}")
        print(f"  {self.description}")
        print(f"{'='*50}")
        for idx, tool in enumerate(self.tools, start=1):
            installed_marker = "[+]" if tool.is_installed() else "[ ]"
            print(f"  {idx:>2}. {installed_marker} {tool.name:<30} {tool.description}")
        print(f"   0. Back to main menu")
        print(f"{'='*50}")

    @abstractmethod
    def run(self) -> None:
        """Present the category menu and handle user selection."""
        pass
