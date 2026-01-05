"""Effect for Hollow Direhorn (DINO_416).

Card Text: <b>Rush</b>
After a friendly minion dies, spend 3 <b>Corpses</b> to gain <b>Reborn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass