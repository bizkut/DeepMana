"""Effect for Ice Barrier (VAN_EX1_289).

Card Text: [x]<b>Secret:</b> As soon as your
hero is attacked, gain
8 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(8)