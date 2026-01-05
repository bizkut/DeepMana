"""Effect for Psychopomp (ULD_268).

Card Text: [x]<b>Battlecry:</b> Summon a
random friendly minion
that died this game.
Give it <b>Reborn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_268t")