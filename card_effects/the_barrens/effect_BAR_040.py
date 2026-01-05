"""Effect for South Coast Chieftain (BAR_040).

Card Text: <b>Battlecry:</b> If you control another Murloc, deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)