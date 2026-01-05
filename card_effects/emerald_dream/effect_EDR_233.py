"""Effect for Spirits of the Forest (EDR_233).

Card Text: <b>Choose One -</b> Summon three 2/3 Wolves with <b>Taunt</b>; or Summon two 4/3 Falcons with <b>Windfury</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_233t")