"""Effect for Rime Sculptor (RLK_Prologue_RLK_752).

Card Text: Battlecry: Summon two 2/1 Rime Elementals with "Deathrattle: Deal 2 damage to a random enemy."
"""

def battlecry(game, source, target):
    player = source.controller
    
    # Summon two Rime Elementals
    for _ in range(2):
        game.summon_token(player, "RLK_Prologue_RLK_752t")