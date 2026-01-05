"""Effect for Sunreaver Warmage (DAL_539).

Card Text: <b>Battlecry:</b> If you're holding a spell that costs (5) or more, deal 4 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)