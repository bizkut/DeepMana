"""Effect for Feast and Famine (RLK_923).

Card Text: Give your hero +3 Attack
this turn. <b>Manathirst (4):</b> And <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3