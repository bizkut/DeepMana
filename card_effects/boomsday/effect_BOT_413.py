"""Effect for Brainstormer (BOT_413).

Card Text: [x]<b>Battlecry:</b> Gain +1 Health
for each spell in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)