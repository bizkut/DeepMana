"""Effect for Wings of Hate (Rank 1) (ONY_016).

Card Text: Summon two 1/1
Felwings. <i>(Upgrades
when you have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_016t")