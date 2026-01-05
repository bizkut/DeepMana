"""Effect for Spirit of the Raptor (TRL_223).

Card Text: [x]<b>Stealth</b> for 1 turn.
After your hero attacks and
  kills a minion, draw a card.  
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)