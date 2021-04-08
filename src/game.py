def play(player_1, player_2):

    if player_1.gesture == "paper" and player_2.gesture == "rock":
        return player_1.name
    if player_1.gesture == "rock" and player_2.gesture == "paper":
        return player_2.name
    elif player_1.gesture == "paper" and player_2.gesture == "scissors":
        return player_2.name
    elif player_1.gesture == "scissors" and player_2.gesture == "paper":
        return player_1.name
    elif player_1.gesture == player_2.gesture:
        return 'Draw'




