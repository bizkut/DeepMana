"""Effect for Subject 9 (BOT_573).

Card Text: <b>Battlecry:</b> Draw 5 different <b>Secrets</b> from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)