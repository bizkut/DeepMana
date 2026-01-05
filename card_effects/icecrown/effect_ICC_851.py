"""Effect for Prince Keleseth (ICC_851).

Card Text: <b>Battlecry:</b> If your deck has no 2-Cost cards, give all minions in your deck +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2