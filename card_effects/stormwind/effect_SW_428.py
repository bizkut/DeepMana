"""Effect for Lost in the Park (SW_428).

Card Text: <b>Questline:</b> Gain 4 Attack with your hero. <b>Reward:</b> Gain 5 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(4)