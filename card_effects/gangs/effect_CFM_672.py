"""Effect for Madam Goya (CFM_672).

Card Text: <b>Battlecry:</b> Choose a friendly
minion. Summon any copies
of it in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_672t")