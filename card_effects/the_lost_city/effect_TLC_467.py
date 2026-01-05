"""Effect for Whispering Stone (TLC_467).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Get 2 random
Fel spells. They cost Health
instead of Mana.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)