"""Effect for Carnival Clown (DMF_163).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Summon 2 copies
of this. <b>Corrupt:</b> Fill your
board with copies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_163t")