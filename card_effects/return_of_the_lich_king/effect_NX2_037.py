"""Effect for Frost Queen Sindragosa (NX2_037).

Card Text: <b>Colossal +2</b>
After an enemy minion is <b>Frozen</b>, destroy it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()