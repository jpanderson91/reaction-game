def calculate_points(reaction_time, streak):
    score = 100
    if reaction_time < 2.0:
        score += 300
    elif reaction_time < 3.0:
        score += 200
    elif reaction_time < 4.0: 
        score += 100
    if streak > 2:
        score *= 3
    return score
        