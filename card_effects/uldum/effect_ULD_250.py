"""Effect for Infested Goblin (ULD_250).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Add two 1/1 Scarabs with <b>Taunt</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass