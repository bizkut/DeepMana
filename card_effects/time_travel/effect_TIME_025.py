"""Effect for Twilight Timehopper (TIME_025).

Card Text: [x]<b>Battlecry:</b> Shuffle 2
Shreds of Time into your
deck. When drawn, deal 3
damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)