"""Effect for Azsharan Ritual (TSC_775).

Card Text: <b>Silence</b> a minion and summon a copy of it. Put a 'Sunken Ritual' on the bottom of your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_775t")