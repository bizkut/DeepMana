"""Effect for Jepetto Joybuzz (DAL_752).

Card Text: <b>Battlecry:</b> Draw 2 minions from your deck. Set their Attack, Health, and Cost to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)