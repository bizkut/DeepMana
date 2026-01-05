"""Effect for Jace Darkweaver (SW_044).

Card Text: <b>Battlecry:</b> Cast all Fel spells you've played this game <i>(targets enemies if possible)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass