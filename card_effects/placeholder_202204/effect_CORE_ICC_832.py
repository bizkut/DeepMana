"""Effect for Malfurion the Pestilent (CORE_ICC_832).

Card Text: [x]<b>Choose One -</b>
Summon 2 <b>Poisonous</b>
Spiders; or 2 Scarabs
with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_832t")