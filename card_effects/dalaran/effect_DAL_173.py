"""Effect for Darkest Hour (DAL_173).

Card Text: Destroy all friendly minions. For each one, summon a random minion from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_173t")