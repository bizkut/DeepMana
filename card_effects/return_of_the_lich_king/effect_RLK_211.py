"""Effect for Deal with a Devil (RLK_211).

Card Text: Summon two 3/3 Felfiends with <b>Lifesteal</b>.
If your deck has no minions, summon two more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_211t")