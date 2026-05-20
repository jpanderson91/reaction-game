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
from game.scoring import calculate_points
from ui.animations import play_game_over, BURNING_DATACENTER_FRAMES
from game.escalation import generate_problem, present_escalation

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
    print(f"Score            : {stats['score']}")
    print(f"Streak           : {stats['streak']}")
    print(f"Lives            : {stats['lives']}")
        
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
    has_timer = random.random() < 0.3
    time_limit = random.uniform(3.0, 5.0) if has_timer else None
    while True:
        if has_timer and (time.perf_counter() - start_time) > time_limit:
            return "escalation", random_incident
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
            return "fail", random_incident
            
def main():
    stats = {"completed": 0, "total_time": 0.0, "best_time": None, "score": 0, "streak": 0, "lives": 3}
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
            elif result == "fail":
                stats["streak"] = 0
                stats["lives"] -= 1
                if stats["lives"] <= 0:
                    choice = play_game_over(BURNING_DATACENTER_FRAMES, stats["score"], get_single_key)
                    if choice == "new_game":
                        stats["streak"] = 0
                        stats["lives"] = 3   
                        stats["score"] = 0
                        stats["completed"] = 0
                        stats["total_time"] = 0.0
                        stats["best_time"] = None  
                    if choice == "quit":
                        break               
            elif result == "escalation":
                # show problem to the player
                problem, correct_answer = generate_problem(stats["completed"])
                # get their input
                user_input = present_escalation(problem, 60, get_single_key)
                # compare input to correct answer
                try:
                    if user_input is not None and int(user_input) == correct_answer:
                        stats["score"] += 100 # bonus points
                        stats["lives"] += 1 # gain a life
                        stats["streak"] += 1 #increment streak
                    else:
                        stats["lives"] -= 1# lose a life
                        stats["streak"] = 0# reset streak
                except ValueError:
                    # they typed something that isn't a number
                    stats["lives"] -= 1# lose a life
                    stats["streak"] = 0# reset streak
            else:
                stats["completed"] += 1
                stats["total_time"] += result
                stats["best_time"] = result if stats["best_time"] is None else min(stats["best_time"], result)
                print(incident['response'].format(time=result))
                print(incident["success_art"])
                stats["streak"] += 1
                points = calculate_points(result, stats["streak"])
                stats["score"] += points
                    
    except KeyboardInterrupt:
    # Handle clean exit
        completed = stats["completed"]
        average = stats["total_time"] / completed if completed > 0 else 0.0
        best_time = stats["best_time"]
        score = stats["score"]
        streak = stats["streak"]
        lives = stats["lives"]
        print("\n\n--- Loop Summary ---")
        print(f"Total Iterations : {completed}")
        print(f"Best Time        : {best_time:.4f} seconds")
        print(f"Average Time     : {average:.4f} seconds")
        print(f"Score            : {score}")
        print(f"Streak           : {streak}")
        print(f"Lives            : {lives}")
        print("--------------------")
    
if __name__ == "__main__":
        main()