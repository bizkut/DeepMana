"""Effect for Walking Dead (RLK_532).

Card Text: <b>Taunt</b>
If you discard this minion, summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_532t")