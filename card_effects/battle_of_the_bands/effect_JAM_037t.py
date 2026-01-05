"""Effect for Molten Pick of ROCK (JAM_037t).

Card Text: [x]At the end of turn, explode for 8 damage! <i>(Or spend all your Mana to give this to the opponent with +2 damage.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
