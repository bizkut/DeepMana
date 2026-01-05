"""Effect for Weapons Project (BOT_042).

Card Text: Each player equips a 2/3 weapon and
gains 6 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(2)