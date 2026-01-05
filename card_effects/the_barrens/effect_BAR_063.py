"""Effect for Lushwater Scout (BAR_063).

Card Text: After you summon a Murloc, give it +1 Attack and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_063t")