"""Effect for EVIL Quartermaster (DRG_020).

Card Text: <b>Battlecry:</b> Add a <b>Lackey</b> to your hand. Gain 3 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(3)