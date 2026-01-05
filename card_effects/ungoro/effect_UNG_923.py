"""Effect for Iron Hide (UNG_923).

Card Text: Gain 5 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)