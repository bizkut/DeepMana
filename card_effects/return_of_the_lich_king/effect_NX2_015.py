"""Effect for Faithful Companions (NX2_015).

Card Text: [x]<b>Discover</b> a Beast from
your deck and summon it.
<b>Manathirst (10):</b> Also
summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_015t")