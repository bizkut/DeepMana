"""Effect for Spirit of the Lynx (TRL_901).

Card Text: [x]<b>Stealth</b> for 1 turn.
Whenever you summon a 
Beast, give it +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_901t")