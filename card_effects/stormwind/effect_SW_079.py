"""Effect for Flightmaster Dungar (SW_079).

Card Text: [x]<b>Battlecry:</b> Choose a
flightpath and go <b>Dormant.
</b> Awaken with a bonus
  when you complete it!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass