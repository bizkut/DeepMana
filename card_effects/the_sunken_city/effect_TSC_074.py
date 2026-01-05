"""Effect for Kotori Lightblade (TSC_074).

Card Text: [x]After you cast a Holy spell
on this, cast it again on
  another friendly minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass