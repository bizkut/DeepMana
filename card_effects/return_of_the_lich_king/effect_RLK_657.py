"""Effect for Underking (RLK_657).

Card Text: [x]<b>Rush</b>
<b>Battlecry and Deathrattle:</b>
Gain 6 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(6)


def deathrattle(game, source):
    pass