"""Tool category definitions and registry for hackingtool.

This module defines all available hacking tool categories and provides
a registry mapping category names to their respective tool classes.
"""

from enum import Enum, auto


class ToolCategory(Enum):
    """Enumeration of all supported tool categories."""

    ANONYMOUSLY_HIDING = auto()
    INFORMATION_GATHERING = auto()
    WORDLIST_GENERATOR = auto()
    WIRELESS_ATTACK = auto()
    SQL_INJECTION = auto()
    PHISHING_ATTACK = auto()
    WEB_ATTACK = auto()
    POST_EXPLOITATION = auto()
    FORENSICS = auto()
    PAYLOAD_CREATOR = auto()
    EXPLOIT_FRAMEWORK = auto()
    REVERSE_ENGINEERING = auto()
    DDOS_ATTACK = auto()
    RAT = auto()
    XSS_ATTACK = auto()
    STEGANOGRAPHY = auto()
    SocialEngineering = auto()


# Human-readable labels for each category
CATEGORY_LABELS = {
    ToolCategory.ANONYMOUSLY_HIDING:  "Anonymously Hiding Tools",
    ToolCategory.INFORMATION_GATHERING: "Information Gathering Tools",
    ToolCategory.WORDLIST_GENERATOR:  "Wordlist Generator",
    ToolCategory.WIRELESS_ATTACK:    "Wireless Attack Tools",
    ToolCategory.SQL_INJECTION:      "SQL Injection Tools",
    ToolCategory.PHISHING_ATTACK:    "Phishing Attack Tools",
    ToolCategory.WEB_ATTACK:         "Web Attack Tools",
    ToolCategory.POST_EXPLOITATION:  "Post Exploitation Tools",
    ToolCategory.FORENSICS:          "Forensics Tools",
    ToolCategory.PAYLOAD_CREATOR:    "Payload Creator",
    ToolCategory.EXPLOIT_FRAMEWORK:  "Exploit Frameworks",
    ToolCategory.REVERSE_ENGINEERING: "Reverse Engineering Tools",
    ToolCategory.DDOS_ATTACK:        "DDoS Attack Tools",
    ToolCategory.RAT:                "Remote Access Trojans (RAT)",
    ToolCategory.XSS_ATTACK:         "XSS Attack Tools",
    ToolCategory.STEGANOGRAPHY:      "Steganography Tools",
    ToolCategory.SocialEngineering:  "Social Engineering Tools",
}

# Ordered list of categories as displayed in the main menu
MENU_ORDER = [
    ToolCategory.ANONYMOUSLY_HIDING,
    ToolCategory.INFORMATION_GATHERING,
    ToolCategory.WORDLIST_GENERATOR,
    ToolCategory.WIRELESS_ATTACK,
    ToolCategory.SQL_INJECTION,
    ToolCategory.PHISHING_ATTACK,
    ToolCategory.WEB_ATTACK,
    ToolCategory.POST_EXPLOITATION,
    ToolCategory.FORENSICS,
    ToolCategory.PAYLOAD_CREATOR,
    ToolCategory.EXPLOIT_FRAMEWORK,
    ToolCategory.REVERSE_ENGINEERING,
    ToolCategory.DDOS_ATTACK,
    ToolCategory.RAT,
    ToolCategory.XSS_ATTACK,
    ToolCategory.STEGANOGRAPHY,
    ToolCategory.SocialEngineering,
]


def get_category_label(category: ToolCategory) -> str:
    """Return the human-readable label for a given category.

    Args:
        category: A ToolCategory enum member.

    Returns:
        The display label string for that category.

    Raises:
        KeyError: If the category is not found in CATEGORY_LABELS.
    """
    return CATEGORY_LABELS[category]


def display_categories() -> None:
    """Print all tool categories with their menu index to stdout."""
    print("\n  Available Tool Categories:\n")
    for idx, category in enumerate(MENU_ORDER, start=1):
        label = get_category_label(category)
        print(f"  [{idx:>2}] {label}")
    print("  [ 0] Exit")
    print()
