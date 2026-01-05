"""Effect for Blastcrystal Potion (CFM_608).

Card Text: Destroy a minion and one of your Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()