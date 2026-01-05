"""Effect for Eternium Rover (BOT_059).

Card Text: Whenever this minion takes damage, gain 2 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(2)