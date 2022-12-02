input_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
response_map = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}
rules = {
    ("rock", "paper"): False,
    ("rock", "scissors"): True,
    ("paper", "rock"): True,
    ("paper", "scissors"): False,
    ("scissors", "rock"): False,
    ("scissors", "paper"): True,
}
strategy = {
    ("rock", "lose"): "scissors",
    ("rock", "win"): "paper",
    ("paper", "lose"): "rock",
    ("paper", "win"): "scissors",
    ("scissors", "lose"): "paper",
    ("scissors", "win"): "rock",
}

shape_scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def get_score(opponent, response):
    shape_score = shape_scores[response]
    if opponent == response:
        return 3 + shape_score
    opponent_wins = rules[(opponent, response)]
    if opponent_wins:
        return shape_score
    return 6 + shape_score

data = open("input")
score = 0
for line in data:
    opp, outcome = line.split()
    opponent_move = input_map[opp]
    desired_outcome = response_map[outcome]
    if desired_outcome == "draw":
        our_move = opponent_move
    else:
        our_move = strategy[(opponent_move, desired_outcome)]
    score += get_score(opponent_move, our_move)
print(score)