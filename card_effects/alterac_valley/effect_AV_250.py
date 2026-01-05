"""Effect for Snowball Fight! (AV_250).

Card Text: Deal $1 damage to a minion and <b>Freeze</b> it.
If it survives, repeat this on another minion!
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)