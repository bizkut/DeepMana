"""Effect for Wretched Reclaimer (ULD_269).

Card Text: [x]<b>Battlecry:</b> Destroy a friendly
minion, then return it to life
with full Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()