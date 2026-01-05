"""Effect for Big-Time Racketeer (CFM_648).

Card Text: <b>Battlecry:</b> Summon a 6/6 Ogre.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_648t")