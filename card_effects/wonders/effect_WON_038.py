"""Effect for Flame Leviathan (WON_038).

Card Text: [x]<b>Rush</b>
When you draw this, deal
2 damage to all characters
except Mechs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)