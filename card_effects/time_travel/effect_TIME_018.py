"""Effect for Mend the Timeline (TIME_018).

Card Text: <b>Rewind</b>
Get 2 random Holy spells. Restore Health to your hero equal to their Costs.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)