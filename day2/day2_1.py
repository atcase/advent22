input_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
response_map = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

rules = {
    ("rock", "paper"): False,
    ("rock", "scissors"): True,
    ("paper", "rock"): True,
    ("paper", "scissors"): False,
    ("scissors", "rock"): False,
    ("scissors", "paper"): True,
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
    opp, resp = line.split()
    opponent_move = input_map[opp]
    our_response = response_map[resp]
    score += get_score(opponent_move, our_response)
print(score)