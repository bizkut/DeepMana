"""Effect for Forbidden Words (DAL_723).

Card Text: [x]Spend all your Mana.
Destroy a minion with that
much Attack or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()