"""Effect for Baba Naga (TSC_017).

Card Text: <b>Battlecry:</b> If you've cast
a spell while holding this, deal 3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)