"""Effect for Double Cross (REV_825).

Card Text: <b>Secret:</b> When your opponent spends all their Mana, draw two cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)