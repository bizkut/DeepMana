"""Effect for Hack the System (ULD_711).

Card Text: [x]<b>Quest:</b> Attack 5 times
with your hero.
<b>Reward:</b> Anraphet's Core.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass