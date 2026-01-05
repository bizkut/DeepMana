"""Effect for Autodefense Matrix (BOT_908).

Card Text: <b>Secret:</b> When one of your minions is attacked, give it <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1