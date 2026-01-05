"""Effect for Chitinous Plating (RLK_656).

Card Text: Gain 4 Armor. At the start of your next turn, gain 4 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(4)