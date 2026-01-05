"""Effect for Spirit of the Dead (TRL_502).

Card Text: [x]<b>Stealth</b> for 1 turn.
After a friendly minion dies,
shuffle a 1-Cost copy of it
into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass