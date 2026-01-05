"""Effect for Bring It On! (CORE_ICC_837).

Card Text: Gain 10 Armor. Reduce the Cost of minions in your opponent's hand by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(10)