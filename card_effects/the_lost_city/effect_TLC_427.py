"""Effect for Rockskipper (TLC_427).

Card Text: <b>Battlecry:</b> Get a 1-Cost
Rock that deals $3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)