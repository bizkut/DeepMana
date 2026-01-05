"""Effect for Troubled Double (TIME_710).

Card Text: <b>Stealth</b>
<b>Combo:</b> Summon a
copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_710t")