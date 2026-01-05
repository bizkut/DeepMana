"""Effect for Frozen Buckler (AV_109).

Card Text: Gain 10 Armor. At the start of your next turn, lose 5 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(10)