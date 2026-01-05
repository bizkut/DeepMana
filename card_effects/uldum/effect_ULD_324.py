"""Effect for Impbalming (ULD_324).

Card Text: Destroy a minion. Shuffle 3 Worthless Imps into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()