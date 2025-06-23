# To start the game use call durak_game, after the game is finished it will return either player_cheated (the game is finished because the player cheated), the variable who_win_ with the value True (the player won) or False (the player lost)

define e = Character('Eileen', color="#c8ffc8")

# Example of launching a mini-game:
label start:

    scene room
    show eileen

    e "Let's play the card durak!"

    # The game call itself
    call durak_game

    # here are the actions after the game, we need to show the background and sprites again
    scene room
    show eileen
    with Dissolve(.3)

    if who_win_ == 0: # opponent wins
        e "Hehe, I win~"
    elif who_win_ == 1: # draw
        e "We have a draw!"
    else: # player wins
        e "Wow, you won! Congratulations!"

    e "And here is the general continuation of the plot."

    return
