"""Effect for Hedra the Heretic (TSC_658).

Card Text: [x]<b>Battlecry:</b> For each spell
you've cast while holding
this, summon a minion
of that spell's Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_658t")