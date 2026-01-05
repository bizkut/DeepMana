"""Effect for Power Word: Feast (SCH_136).

Card Text: Give a minion +2/+2. Restore it to full Health at the end of this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)