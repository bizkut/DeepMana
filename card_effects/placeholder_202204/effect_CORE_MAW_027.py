"""Effect for Call to the Stand (CORE_MAW_027).

Card Text: Your opponent summons a random minion from their hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_MAW_027t")