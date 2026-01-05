"""Effect for Command the Elements (SW_031).

Card Text: [x]<b>Questline:</b> Play 3 cards
 with <b>Overload</b>.
<b>Reward:</b> Unlock your
<b>Overloaded</b> Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass