"""Effect for Omega Defender (BOT_296).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you have
10 Mana Crystals,
gain +10 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 10
        target._max_health += 10