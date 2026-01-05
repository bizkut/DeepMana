"""Effect for Zerek's Cloning Gallery (BOT_567).

Card Text: Summon a 1/1 copy of each minion in your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_567t")