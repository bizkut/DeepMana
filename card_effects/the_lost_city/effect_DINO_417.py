"""Effect for Soulrest Ceremony (DINO_417).

Card Text: [x]Give your minions
+1 Attack and <b>Rush</b>. They
die at the end of your turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1