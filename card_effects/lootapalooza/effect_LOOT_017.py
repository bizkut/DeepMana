"""Effect for Dark Pact (LOOT_017).

Card Text: Destroy a friendly minion. Restore #8 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()