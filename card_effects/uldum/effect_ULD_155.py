"""Effect for Unseal the Vault (ULD_155).

Card Text: <b>Quest:</b> Summon 20 minions.
<b>Reward:</b> Pharaoh's Warmask.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_155t")