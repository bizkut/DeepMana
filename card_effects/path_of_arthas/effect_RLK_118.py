"""Effect for Tomb Guardians (RLK_118).

Card Text: Summon two 2/2 Zombies with <b>Taunt</b>. Spend 4 <b>Corpses</b> to
give them <b>Reborn</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_118t")