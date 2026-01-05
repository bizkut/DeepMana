"""Effect for Seeds of Destruction (AV_277).

Card Text: [x]Shuffle four Rifts
into your deck. They
summon a 3/3 Dread
Imp when drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)