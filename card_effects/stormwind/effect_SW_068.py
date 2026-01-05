"""Effect for Mo'arg Forgefiend (SW_068).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Gain 8 Armor.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(8)