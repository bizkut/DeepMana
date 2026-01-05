"""Effect for Witchwood Imp (GIL_608).

Card Text: [x]<b>Stealth</b>
<b>Deathrattle:</b> Give a random
  friendly minion +2 Health.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)