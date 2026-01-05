"""Effect for Heavy Plate (SW_094).

Card Text: <b>Tradeable</b>
Gain 8 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(8)