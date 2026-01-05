"""Effect for Thickhide Kodo (BAR_535).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Gain 5 Armor.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)