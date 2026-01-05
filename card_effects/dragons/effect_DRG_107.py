"""Effect for Violet Spellwing (DRG_107).

Card Text: <b>Deathrattle:</b> Add an 'Arcane Missiles' spell to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass