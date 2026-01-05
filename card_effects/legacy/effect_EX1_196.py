"""Effect for Scarlet Subjugator (EX1_196).

Card Text: <b>Battlecry:</b> Give an enemy minion -2 Attack until your next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2