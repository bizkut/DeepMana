"""Effect for Gold Road Grunt (BAR_021).

Card Text: [x]<b>Taunt</b>
<b>Frenzy:</b> Gain Armor equal
to the damage taken.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)