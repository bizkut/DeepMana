"""Effect for Prismatic Lens (BOT_436).

Card Text: Draw a minion and a spell from your deck. Swap their Costs.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)