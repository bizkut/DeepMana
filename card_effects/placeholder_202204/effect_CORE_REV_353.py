"""Effect for Huntsman Altimor (CORE_REV_353).

Card Text: [x]<b>Battlecry:</b> Summon a
Gargon Companion.
<b>Infuse ({0}):</b> Summon another.
 <b>Infuse ({1}):</b> And another!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_353t")