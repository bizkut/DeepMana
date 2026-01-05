"""Effect for Infinite Amalgam (WON_143).

Card Text: [x]<b>Inspire, Frenzy, <b>Spellburst</b>,
Honorable Kill, and Overkill:</b>
Summon a random
1-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_143t")