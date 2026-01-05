"""Effect for Emberscale Drake (TRL_323).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, gain 5 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)