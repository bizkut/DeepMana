"""Effect for Snowblind Harpy (AV_112).

Card Text: <b>Battlecry:</b> If you're holding
a Frost spell, gain 5 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)