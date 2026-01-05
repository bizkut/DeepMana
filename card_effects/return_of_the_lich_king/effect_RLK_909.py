"""Effect for Deathweaver Aura (RLK_909).

Card Text: Give a minion "<b>Deathrattle:</b> Summon two 3/2 Zombies." <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_909t")