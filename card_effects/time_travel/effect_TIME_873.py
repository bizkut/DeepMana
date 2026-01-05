"""Effect for Unleash the Crocolisks (TIME_873).

Card Text: Gain 10 Armor.
Summon two 2/3 Beasts for your opponent.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_873t")