"""Effect for The Boom Reaver (DAL_070).

Card Text: <b>Battlecry:</b> Summon a copy of a minion in your deck. Give it <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_070t")