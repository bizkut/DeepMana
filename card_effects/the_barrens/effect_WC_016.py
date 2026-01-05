"""Effect for Shroud of Concealment (WC_016).

Card Text: Draw 2 minions. Any played this turn gain <b>Stealth</b> for 1 turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)