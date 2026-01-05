"""Effect for Twin-fin Fin Twin (TSC_960).

Card Text: <b>Rush</b>. <b>Battlecry:</b> Summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_960t")