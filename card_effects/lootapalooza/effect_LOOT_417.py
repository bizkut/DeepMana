"""Effect for Cataclysm (LOOT_417).

Card Text: Destroy all minions. Discard 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()