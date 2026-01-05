"""Effect for Sorcerer's Gambit (SW_450).

Card Text: <b>Questline:</b> Cast a Fire, Frost, and Arcane spell. <b>Reward: </b>Draw a spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)