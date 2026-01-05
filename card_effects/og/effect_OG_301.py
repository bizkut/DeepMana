"""Effect for Ancient Shieldbearer (OG_301).

Card Text: <b>Battlecry:</b> If your C'Thun has at least 10 Attack, gain 10 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(10)