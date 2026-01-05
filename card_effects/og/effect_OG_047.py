"""Effect for Feral Rage (OG_047).

Card Text: <b>Choose One -</b> Give your hero +4 Attack this turn; or Gain 8 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4