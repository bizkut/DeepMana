"""Effect for Blood Boil (RLK_730).

Card Text: <b>Lifesteal</b>
Infect all enemy minions. At the end of your turns, they take 2 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass