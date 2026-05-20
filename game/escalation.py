import random
import operator
import time

def generate_problem(rounds_completed):
    ops_simple = {
        "+": operator.add,
        "-": operator.sub
    }
    ops_medium = {
        "*": operator.mul
    }        
    # determine difficulty based on rounds
    if rounds_completed < 10:
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        symbol = random.choice(["+", "-"])
        answer = ops_simple[symbol](num1, num2)
        return f"{num1} {symbol} {num2}", answer
       
        
    elif rounds_completed < 20:
         
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        symbol = "*"
        answer = ops_medium[symbol](num1, num2)
        return f"{num1} {symbol} {num2}", answer
        
    elif rounds_completed >= 20:
        all_ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        sym1 = random.choice(["+", "-", "*"])
        sym2 = random.choice(["+", "-", "*"])
        answer = all_ops[sym2](all_ops[sym1](num1, num2), num3)
        return f"({num1} {sym1} {num2}) {sym2} {num3}", answer

def present_escalation(problem, time_limit, get_key_func):
    print(f"⚠️ ESCALATION: Solve → {problem}")
    user_input = ""
    start = time.perf_counter()
    # loop: check time, print countdown + input so far, read key
    # Enter → return user_input
    # backspace → remove last char
    # digit or minus → append to user_input
    # time expired → return None
    while True:
        remaining = time_limit - (time.perf_counter() - start)
        if remaining < 0:
            print ("\n⏰ Time's up!")
            return None
        print(f"\r⏱️ {remaining:.0f}s | Answer: {user_input}  ", end="", flush=True)
        key = get_key_func()
        if key is None:
            continue
        if key in ("\r", "\n"):
            return user_input
        if key == "\x7f": # backspace
            user_input = user_input[:-1]
        elif key in "0123456789-":
            user_input += key

    