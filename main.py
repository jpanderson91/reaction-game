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
from ui.animations import INCIDENT_ACTIVE_FRAMES, RESOLVE_SUCCESS_FRAMES, RESOLVE_FAILURE_FRAMES, play_result_screen, clear_screen, play_wait_screen, ENGINEER_DESK_FRAMES, play_game_over, BURNING_DATACENTER_FRAMES, play_start_screen, START_SCREEN_WITH_IMAGE_FRAMES
from game.escalation import generate_problem, present_escalation
from game.highscores import load_highscores, save_highscores



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
    print("Wait..")
    delay = random.uniform(2.0, 5.0)
    random_incident = random.choice(incidents)
    target_key = random.choice(string.ascii_lowercase)
    wait_result = play_wait_screen(ENGINEER_DESK_FRAMES, delay, get_single_key)
    if wait_result == "cancel":
        return None, None
    # after play_wait_screen returns, flush any buffered input
    while get_single_key() is not None:
        pass
    start_time = time.perf_counter()
    has_timer = random.random() < 0.3
    time_limit = random.uniform(3.0, 5.0) if has_timer else None
    i = 0
    while True:
        clear_screen()
        print(INCIDENT_ACTIVE_FRAMES[i % len(INCIDENT_ACTIVE_FRAMES)])
        print(f"\n{random_incident['alert']} - Press '{target_key}' to resolve!")
        if has_timer and (time.perf_counter() - start_time) > time_limit:
            return "escalation", random_incident
        key = get_single_key()
        if key is None:
            pass
        elif key == target_key:
            return time.perf_counter() - start_time, random_incident
        elif ord(key) == 27:
            return None, None
        else:
            return "fail", random_incident
        i += 1
        for _ in range(4):
            key = get_single_key()
            if key == target_key:
                return time.perf_counter() - start_time, random_incident
            if key and ord(key) == 27:
                return None, None
            if key is not None:
                return "fail", random_incident
            
def main():
    stats = {"completed": 0, "total_time": 0.0, "best_time": None, "score": 0, "streak": 0, "lives": 3}
    show_start = True
    highscores = load_highscores()
    stats["highscores"] = highscores
    
    try:
        while True:
            if show_start:
                action = play_start_screen(START_SCREEN_WITH_IMAGE_FRAMES, stats, get_single_key)
                show_start = False
                
                if action == "exit":
                    break

            result, incident = play_round()
            if result is None:
                show_start = True
                continue
            elif result == "fail":
                play_result_screen(RESOLVE_FAILURE_FRAMES, "Wrong key!", get_single_key)
                stats["streak"] = 0
                stats["lives"] -= 1
                if stats["lives"] <= 0:
                    choice = play_game_over(BURNING_DATACENTER_FRAMES, stats["score"], get_single_key)
                    save_highscores(stats["score"])
                    stats["highscores"] = load_highscores()
                    if choice == "new_game":
                        stats["streak"] = 0
                        stats["lives"] = 3   
                        stats["score"] = 0
                        stats["completed"] = 0
                        stats["total_time"] = 0.0
                        stats["best_time"] = None
                        show_start = True
                    if choice == "quit":
                        break               
            elif result == "escalation":
                problem, correct_answer = generate_problem(stats["completed"])
                user_input = present_escalation(problem, 60, get_single_key)
                try:
                    if user_input is not None and int(user_input) == correct_answer:
                        stats["score"] += 100
                        stats["lives"] += 1
                        stats["streak"] += 1
                    else:
                        stats["lives"] -= 1
                        stats["streak"] = 0
                except ValueError:
                    stats["lives"] -= 1
                    stats["streak"] = 0
            else:
                stats["completed"] += 1
                stats["total_time"] += result
                stats["best_time"] = result if stats["best_time"] is None else min(stats["best_time"], result)
                play_result_screen(RESOLVE_SUCCESS_FRAMES, incident['response'].format(time=result), get_single_key)
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