"""Effect for Keeper of Flame (FIR_928).

Card Text: [x]<b>Battlecry:</b> Give all minions
in your hand +3/+3. They
are destroyed in 3 turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()