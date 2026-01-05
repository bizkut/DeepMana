"""Effect for Scrap Golem (BT_249).

Card Text: <b>Taunt</b>. <b>Deathrattle</b>: Gain Armor equal to this minion's Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)