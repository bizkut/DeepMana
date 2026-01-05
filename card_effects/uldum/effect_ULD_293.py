"""Effect for Cloud Prince (ULD_293).

Card Text: <b>Battlecry:</b> If you control a <b>Secret</b>, deal 6 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)