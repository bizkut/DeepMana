"""Effect for Infest (OG_045).

Card Text: Give your minions "<b>Deathrattle:</b> Add a random Beast to your hand."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1