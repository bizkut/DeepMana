"""Effect for Shadow Essence (CORE_ICC_235).

Card Text: Summon a 5/5 copy of a random minion in your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_235t")