"""Effect for Spirit of the Bat (TRL_251).

Card Text: <b>Stealth</b> for 1 turn.
After a friendly minion dies, give a minion in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1