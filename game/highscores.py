import json

def load_highscores(filepath="data/highscores.json"):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_highscores(score, filepath="data/highscores.json"):
    # adds score to the list
    # sorts
    # keeps top 5
    # writes back
    scores = load_highscores(filepath)
    scores.append(score)
    scores.sort(reverse=True)
    scores = scores[:5]
    with open(filepath, "w") as f:
        json.dump(scores, f)