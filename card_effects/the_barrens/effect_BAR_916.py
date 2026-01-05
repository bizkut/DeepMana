"""Effect for Blood Shard Bristleback (BAR_916).

Card Text: [x]<b>Lifesteal</b>. <b>Battlecry:</b> If your
deck contains 10 or fewer
cards, deal 6 damage
to a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 10, source)