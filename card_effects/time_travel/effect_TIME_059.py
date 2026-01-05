"""Effect for Living Paradox (TIME_059).

Card Text: <b>Elusive</b>
<b>Battlecry:</b> Summon two
2/1 Living Paradoxes with <b>Elusive</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_059t")