"""Base class for all hacking tools in the hackingtool suite.

This module provides the foundational structure that all tool categories
and individual tools should inherit from.
"""

import os
import subprocess
import shutil
from abc import ABC, abstractmethod
from typing import Optional

# Default directory where cloned tools will be stored.
# Change this to "~/tools" or another path if you don't want to use /opt/
DEFAULT_CLONE_DIR = "/opt"


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
        """Clone the tool's repository into DEFAULT_CLONE_DIR."""
        dest = os.path.join(DEFAULT_CLONE_DIR, self.name.lower().replace(' ', '_'))
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
        return f"{self.name}: {self.description}"
