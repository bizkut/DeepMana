"""Effect for Terrorscale Stalker (CORE_UNG_800).

Card Text: Battlecry: Trigger a friendly minion's Deathrattle.
"""

def battlecry(game, source, target):
    player = source.controller
    
    # Trigger a friendly minion's Deathrattle
    if target and target in player.board and target != source:
        if target.data.deathrattle:
            game._trigger_deathrattle(target)