"""Effect for Against All Odds (WC_014).

Card Text: Destroy ALL
odd-Attack minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()