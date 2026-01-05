"""Effect for Judgment of Justice (WC_033).

Card Text: <b>Secret:</b> When an enemy minion attacks, set its Attack and Health to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)