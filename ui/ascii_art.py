from pyfiglet import figlet_format
from colorama import Fore, Back, Style

def side_by_side(left, right, spacing=4):
    left_lines = left.splitlines()
    right_lines = right.splitlines()
    left_width = max(len(line) for line in left_lines)
    max_lines = max(len(left_lines), len(right_lines))
    result = []
    for i in range(max_lines):
        l = left_lines[i] if i < len(left_lines) else ""
        r = right_lines[i] if i < len(right_lines) else ""
        result.append(f"{l:<{left_width}}{' ' * spacing}{r}")
    return "\n".join(result)


CLOUD_ART = r"""
      _____
     |.---.|
     ||___||
     |+  .'|
     | _ _ |
     |_____/
"""

def print_banner(text="Reaction Game"):
    print(Back.BLACK + Fore.GREEN)
    combined = side_by_side(CLOUD_ART, figlet_format(text))
    combined = side_by_side(combined, CLOUD_ART)
    print(combined)
    print(Style.RESET_ALL)