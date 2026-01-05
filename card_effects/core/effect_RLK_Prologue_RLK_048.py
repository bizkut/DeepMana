"""Effect for Anti-Magic Shell (RLK_Prologue_RLK_048).

Card Text: Give your minions +1/+1 and <b>Elusive</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
