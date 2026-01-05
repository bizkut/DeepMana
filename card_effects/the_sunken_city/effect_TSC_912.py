"""Effect for Azsharan Vessel (TSC_912).

Card Text: Summon two 3/3 Pirates with <b>Stealth</b>. Put a 'Sunken Vessel' on the bottom of your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_912t")