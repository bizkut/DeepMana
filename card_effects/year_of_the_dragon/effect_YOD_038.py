"""Effect for Sky Gen'ral Kragg (YOD_038).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you've played a
<b>Quest</b> this game, summon a
4/2 Parrot with <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_038t")