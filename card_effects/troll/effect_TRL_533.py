"""Effect for Ice Cream Peddler (TRL_533).

Card Text: <b>Battlecry:</b> If you control a <b>Frozen</b> minion, gain 8 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(8)