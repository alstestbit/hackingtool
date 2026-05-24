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
    # Personal note: I mostly use this for CTFs, so info gathering
    # and hash cracking are the categories I care about most.
