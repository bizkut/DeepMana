"""Effect for Za'qul (TSC_959).

Card Text: [x]Your Abyssal Curses heal you
for the damage they deal.
<b>Battlecry:</b> Give your opponent
an Abyssal Curse.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)