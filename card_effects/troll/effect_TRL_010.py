"""Effect for Half-Time Scavenger (TRL_010).

Card Text: <b>Stealth</b>
<b>Overkill</b>: Gain 3 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(3)