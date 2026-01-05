"""Effect for Spiteful Summoner (LOOT_539).

Card Text: [x]<b>Battlecry:</b> Reveal a spell
from your deck. Summon
 a random minion with
the same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_539t")