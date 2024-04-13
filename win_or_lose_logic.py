def determine_win_or_loss(bet, chosen_number, winning_number):
    if chosen_number == winning_number:
        return "win"
    else:
        return "loss"