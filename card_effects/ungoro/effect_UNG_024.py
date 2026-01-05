"""Effect for Mana Bind (UNG_024).

Card Text: <b>Secret:</b> When your opponent casts a spell, add a copy to your hand that costs (0).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass