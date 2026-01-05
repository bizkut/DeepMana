"""Effect for Archdruid Naralex (WC_035).

Card Text: [x]<b>Dormant</b> for 2 turns.
While <b>Dormant</b>, add a
Dream card to your hand
  at the end of your turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass