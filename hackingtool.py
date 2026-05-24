#!/usr/bin/env python3
"""
HackingTool - A collection of hacking tools for security researchers.
Fork of Z4nzu/hackingtool

Usage:
    python3 hackingtool.py

Warning:
    This tool is intended for educational purposes and authorized testing only.
    Unauthorized use of these tools is illegal and unethical.
"""

import os
import sys
import subprocess

# Ensure Python 3 is being used
if sys.version_info.major < 3:
    print("[-] Python 3 is required to run this tool.")
    sys.exit(1)


BANNER = r"""
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

          ████████╗ ██████╗  ██████╗ ██╗
          ╚══██╔══╝██╔═══██╗██╔═══██╗██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ╚██████╔╝╚██████╔╝███████╗
             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

        [*] For Educational Purposes Only [*]
"""

MENU_CATEGORIES = [
    ("Anonymous Surfing Tools",      "anonsurf"),
    ("Information Gathering Tools",  "infogathering"),
    ("Wordlist Generator",           "wordlist"),
    ("Wireless Attack Tools",        "wireless"),
    ("SQL Injection Tools",          "sqli"),
    ("Phishing Attack Tools",        "phishing"),
    ("Web Attack Tools",             "webattack"),
    ("Post Exploitation Tools",      "postexploit"),
    ("Forensic Tools",               "forensic"),
    ("Payload Creation Tools",       "payload"),
    ("Exploit Framework Tools",      "exploit"),
    ("Reverse Engineering Tools",    "reversing"),
    ("DDOS Attack Tools",            "ddos"),
    ("Remote Administration Tools",  "rat"),
    ("XSS Attack Tools",             "xss"),
    ("Steganography Tools",          "stego"),
    ("SocialMedia Brute Force",      "socialmedia"),
    ("Android Hacking Tools",        "android"),
    ("IDN Homograph Attack Tools",   "idn"),
    ("Email Spoofing Tools",         "email"),
    ("Hash Cracking Tools",          "hash"),
    ("Wifi Deauthenticate Tools",    "wifi_deauth"),
    ("All In One Tools",             "allinone"),
    ("Termux Tools",                 "termux"),
    ("Stealth Tools",                "stealth"),
    ("Other Tools",                  "other"),
]


def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def check_root():
    """Check if the script is running with root privileges."""
    if os.geteuid() != 0:
        print("[!] Warning: Some tools may require root privileges.")
        print("[!] Consider running with sudo if tools fail to execute.\n")


def display_banner():
    """Display the ASCII art banner."""
    print(BANNER)


def display_main_menu():
    """Display the main tool category menu."""
    print("\n" + "=" * 60)
    print(" MAIN MENU ".center(60, "="))
    print("=" * 60)
    for idx, (category, _) in enumerate(MENU_CATEGORIES, start=1):
        print(f"  [{idx:02d}] {category}")
    print("  [00] Exit")
    print("=" * 60)


def get_user_choice(prompt="[?] Select an option: ", max_val=None):
    """Prompt the user for a numeric menu choice."""
    while True:
        try:
            choice = int(input(prompt).strip())
            if max_val is not None and not (0 <= choice <= max_val):
                print(f"[-] Please enter a number between 0 and {max_val}.")
                continue
            return choice
        except ValueError:
            print("[-] Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n[!] Interrupted. Exiting...")
            sys.exit(0)


def run_category(module_key: str):
    """
    Placeholder dispatcher — will delegate to the appropriate
    category module once individual modules are implemented.
    """
    print(f"\n[*] Loading module: {module_key} ...")
    # TODO: import and call the relevant category module
    print(f"[!] Module '{module_key}' is not yet implemented.")
    input("\n[Press ENTER to return to the main menu]")


def main():
    """Main entry point for HackingTool."""
    clear_screen()
    display_banner()
    check_root()

    while True:
        display_main_menu()
        choice = get_user_choice(max_val=len(MENU_CATEGORIES))

        if choice == 0:
            print("\n[*] Goodbye! Stay ethical.\n")
            sys.exit(0)

        category_name, module_key = MENU_CATEGORIES[choice - 1]
        clear_screen()
        print(f"\n[+] Selected: {category_name}")
        run_category(module_key)
        clear_screen()
        display_banner()


if __name__ == "__main__":
    main()
