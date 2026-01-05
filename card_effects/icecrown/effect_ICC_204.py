"""Effect for Professor Putricide (ICC_204).

Card Text: After you play a <b>Secret</b>,
put a random Hunter <b>Secret</b> into the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass