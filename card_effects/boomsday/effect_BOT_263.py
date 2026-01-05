"""Effect for Soul Infusion (BOT_263).

Card Text: Give the
left-most minion in your hand +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2