"""Effect for Blastmaster Boom (DAL_064).

Card Text: [x]<b>Battlecry:</b> Summon two 1/1
Boom Bots for each Bomb
in your opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_064t")