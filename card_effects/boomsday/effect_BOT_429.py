"""Effect for Flark's Boom-Zooka (BOT_429).

Card Text: [x]Summon 3 minions from
your deck. They attack
enemy minions, then die.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_429t")