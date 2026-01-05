"""Effect for Igneous Lavagorger (TID_714).

Card Text: [x]<b>Taunt</b>
 <b>Battlecry:</b> <b>Dredge</b>. Gain
 Armor equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)