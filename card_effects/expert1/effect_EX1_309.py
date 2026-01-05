"""Effect for Siphon Soul (EX1_309).

Card Text: Destroy a minion. Restore #3 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()