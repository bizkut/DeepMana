"""Effect for Gilneas Brochure (WORK_017t).

Card Text: <b>Silence</b> a minion and give it -2/-2. <i>(Flips each turn.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
