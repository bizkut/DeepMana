"""Effect for Amber Whelp (RLK_915).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, deal 3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)