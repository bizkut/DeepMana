"""Effect for Whizbang the Wonderful (BOT_914).

Card Text: [x]You start the game
with one of Whizbang's
Wonderful Decks!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass