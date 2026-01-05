"""Effect for Agamaggan (EDR_489).

Card Text: [x]<b>Battlecry:</b> The next card you
play costs your OPPONENT'S
Health instead of Mana
<i>(up to 10)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 10, source)