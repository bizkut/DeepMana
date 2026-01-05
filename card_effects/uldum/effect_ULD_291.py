"""Effect for Corrupt the Waters (ULD_291).

Card Text: [x]<b>Quest:</b> Play 6 <b>Battlecry</b>
cards.
<b>Reward:</b> Heart of Vir'naal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass