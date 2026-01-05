"""Effect for Kabal Lackey (CFM_066).

Card Text: [x]<b>Battlecry:</b> The next <b>Secret</b>
you play this turn costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass