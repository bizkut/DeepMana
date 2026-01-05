"""Effect for Spirit of the Shark (TRL_092).

Card Text: [x]<b>Stealth</b> for 1 turn.
Your minions' <b>Battlecries</b>
  and <b>Combos</b> trigger twice. 
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass