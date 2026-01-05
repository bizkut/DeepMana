"""Effect for Blood Matriarch Liadrin (RLK_924).

Card Text: After you summon a minion with less Attack than this, give it <b>Divine Shield</b> and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_924t")