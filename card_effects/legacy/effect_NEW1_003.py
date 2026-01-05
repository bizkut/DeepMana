"""Effect for Sacrificial Pact (NEW1_003).

Card Text: Destroy a friendly Demon. Restore #5 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()