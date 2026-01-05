"""Effect for Tomb Warden (ULD_253).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Summon a copy of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_253t")