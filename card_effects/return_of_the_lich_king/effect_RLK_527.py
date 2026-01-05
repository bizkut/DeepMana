"""Effect for Timewarden (RLK_527).

Card Text: [x]<b>Battlecry:</b> Until the end
of your next turn, Dragons
you summon gain <b>Taunt</b>
and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_527t")