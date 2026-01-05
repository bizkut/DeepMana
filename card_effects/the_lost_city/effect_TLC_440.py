"""Effect for Cryosleep (TLC_440).

Card Text: Deal $4 damage
and draw a card.
<b>Kindred: </b>Draw another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)