"""Effect for Willful Watcher (TLC_621).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Destroy the
 top 3 cards of your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()