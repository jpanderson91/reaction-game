import random
import string
import time
import sys
import tty
import termios
import select
import pyfiglet
from colorama import Fore, Back, Style, init
from ui.ascii_art import print_banner
from events.alerts import incidents

#Variables to track timing



# Add a simple main() that runs one round of WAIT
# # -> random delay -> GO -> input -> elapsed time and prints the result



def get_single_key():
    """Reads a single keypress without blocking the game flow."""
    fd = sys.stdin.fileno()
    original_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        dr, _, _ = select.select([sys.stdin], [], [], 0.05)
        if dr:
            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)
        
def show_start_screen(stats, first_run=True):
    if first_run:
        print_banner()
    if stats["completed"] > 0:
        average = stats["total_time"] / stats["completed"]
        print()
        print(f"Incidents Resolved: {stats['completed']}")
        print(f"Best time: {stats['best_time']:.4f}s")
        print(f"Average: {average:.4f}s")
        
    print()
    print("Press Enter to start, or ESC to exit.")
    while True:
        key = get_single_key()
        if key in ("\r", "\n"):
            return "play"
        if key and ord(key) == 27:
            return "exit"

def play_round():
    print("WAIT...")
    delay = random.uniform(2.0, 5.0)
    elapsed = 0
    random_incident = random.choice(incidents)
    target_key = random.choice(string.ascii_lowercase)
    while elapsed < delay:
        key = get_single_key()
        if key and ord(key) == 27:
            print("\nCancelled. Returning to the start screen.")
            return None, None
        elapsed += 0.05
    print(f"\n{random_incident['alert']} - Press '{target_key}' to resolve!")
    start_time = time.perf_counter()
    while True:
        key = get_single_key()
        if key is None:
            continue
        if key == target_key:
            return time.perf_counter() - start_time, random_incident
        if ord(key) == 27:
            print("\nCancelled. Returning to the start screen.")
            return None, None
        else:
            print("Wrong key try again!")
            print(random_incident["fail_art"])

def main():
    stats = {"completed": 0, "total_time": 0.0, "best_time": None}
    first_run = True
    try:
        while True:
            action = show_start_screen(stats, first_run)
            first_run = False
            if action == "exit":
                break
            result, incident = play_round()
            if result is None:
                continue
            stats["completed"] += 1
            stats["total_time"] += result
            stats["best_time"] = result if stats["best_time"] is None else min(stats["best_time"], result)
            print(incident['response'].format(time=result))
            print(incident["success_art"])
                    
    except KeyboardInterrupt:
    # Handle clean exit
        completed = stats["completed"]
        average = stats["total_time"] / completed if completed > 0 else 0.0
        best_time = stats["best_time"]
        print("\n\n--- Loop Summary ---")
        print(f"Total Iterations : {completed}")
        print(f"Best Time        : {best_time:.4f} seconds")
        print(f"Average Time     : {average:.4f} seconds")
        print("--------------------")
    
if __name__ == "__main__":
        main()