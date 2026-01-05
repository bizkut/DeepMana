"""Effect for Mountainfire Armor (CORE_ICC_062).

Card Text: <b>Deathrattle:</b> If it's your opponent's turn,
gain 6 Armor.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(6)