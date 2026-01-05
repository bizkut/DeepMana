"""Effect for Felscale Evoker (NX2_026).

Card Text: [x]<b>Battlecry:</b> If you've cast three
spells while holding this,
summon a different Demon
from your deck.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_026t")