"""Effect for Kun the Forgotten King (CFM_308).

Card Text: <b>Choose One -</b> Gain 10 Armor; or Refresh your Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(10)