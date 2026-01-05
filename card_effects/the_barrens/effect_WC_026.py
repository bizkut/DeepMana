"""Effect for Kresh, Lord of Turtling (WC_026).

Card Text: <b>Frenzy:</b> Gain 8 Armor. <b>Deathrattle:</b> Equip a 2/5 Turtle Spike.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(8)