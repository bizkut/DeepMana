"""Effect for Ritual of the New Moon (EDR_461).

Card Text: [x]Summon two
random 3-Cost minions.
<i>(Cast 3 spells to summon
6-Cost minions instead.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_461t")