"""Effect for Invincible (RLK_592).

Card Text: [x]<b>Reborn</b>
<b>Battlecry and Deathrattle:</b>
Give another random friendly
     Undead +5/+5 and <b>Taunt</b>.    
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5


def deathrattle(game, source):
    pass