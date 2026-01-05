"""Effect for Proving Grounds (DED_508).

Card Text: Summon two minions from your deck.
They fight!
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DED_508t")