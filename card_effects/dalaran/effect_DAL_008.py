"""Effect for Dr. Boom's Scheme (DAL_008).

Card Text: Gain 1 Armor.
<i>(Upgrades each turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)