"""Effect for Bolner Hammerbeak (SW_115).

Card Text: [x]After you play a <b>Battlecry</b>
minion, repeat the first
  <b>Battlecry</b> played this turn. 
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass