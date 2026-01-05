"""Effect for Deck of Lunacy (DMF_108).

Card Text: Transform spells in your deck into ones that cost (3) more. <i>(They keep their original Cost.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass