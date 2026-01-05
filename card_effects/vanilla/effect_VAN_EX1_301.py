"""Effect for Felguard (VAN_EX1_301).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Destroy one of your Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()