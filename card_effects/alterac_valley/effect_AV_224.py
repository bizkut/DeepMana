"""Effect for Spring the Trap (AV_224).

Card Text: Deal $3 damage to a minion and cast a <b>Secret</b> from your deck. <b>Honorable Kill:</b> Cast 2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)