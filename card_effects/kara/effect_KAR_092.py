"""Effect for Medivh's Valet (KAR_092).

Card Text: <b>Battlecry:</b> If you control a <b>Secret</b>, deal 3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)