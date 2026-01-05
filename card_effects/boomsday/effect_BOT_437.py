"""Effect for Goblin Prank (BOT_437).

Card Text: Give a friendly minion +3/+3 and <b>Rush</b>. It dies at end of turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3