"""Effect for Entomologist Toru (TLC_841).

Card Text: [x]<b>Battlecry:</b> Put each minion
 in your hand into 0/1 Jars
 that cost (1). Break them
  to release the minions!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass