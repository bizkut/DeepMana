"""Effect for Nablya, the Watcher (TLC_624).

Card Text: [x]<b>Battlecry:</b> Summon copies
 of your damaged minions.
Give the copies <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_624t")