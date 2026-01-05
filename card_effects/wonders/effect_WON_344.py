"""Effect for Spellslinger (WON_344).

Card Text: <b>Battlecry:</b> Both players
get a random spell.
Yours costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass