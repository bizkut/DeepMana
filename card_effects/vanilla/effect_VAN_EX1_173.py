"""Effect for Starfire (VAN_EX1_173).

Card Text: Deal $5 damage.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)