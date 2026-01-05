"""Effect for Evasion (LOOT_214).

Card Text: <b>Secret:</b> After your hero takes damage, become <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass