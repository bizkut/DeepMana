"""Effect for Scion of Ruin (DRG_019).

Card Text: <b>Rush</b>. <b>Battlecry:</b> If you've <b>Invoked</b> twice, summon 2 copies of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_019t")