"""Effect for Derailed Coaster (DMF_202).

Card Text: <b>Battlecry:</b> Summon a 1/1 Rider with <b>Rush</b> for each minion in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_202t")