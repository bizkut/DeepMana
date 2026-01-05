"""Effect for Torrent (BT_110).

Card Text: [x]Deal $8 damage to a
minion. Costs (3) less if
you cast a spell last turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)