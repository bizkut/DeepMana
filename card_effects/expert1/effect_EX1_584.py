"""Effect for Ancient Mage (EX1_584).

Card Text: <b>Battlecry:</b> Give adjacent minions <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1