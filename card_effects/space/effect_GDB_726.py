"""Effect for Interstellar Starslicer (GDB_726).

Card Text: Battlecry and Deathrattle: Reduce the Cost of your Librams by (1) this game.
"""

LIBRAM_IDS = [
    'BT_011', 'BT_024', 'BT_025', 'BT_292', 'BT_293',  # Original Librams
    'SCH_149', 'SCH_545'  # Scholomance Librams
]

def _reduce_libram_costs(player):
    """Reduce cost of Librams in hand, deck, and future draws."""
    # In hand
    for card in player.hand:
        if card.card_id in LIBRAM_IDS:
            card._cost = max(0, card._cost - 1)
    
    # In deck
    for card in player.deck:
        if card.card_id in LIBRAM_IDS:
            card._cost = max(0, card._cost - 1)
    
    # Track permanent reduction (for future created Librams)
    if not hasattr(player, 'libram_reduction'):
        player.libram_reduction = 0
    player.libram_reduction += 1


def battlecry(game, source, target):
    player = source.controller
    _reduce_libram_costs(player)


def deathrattle(game, source):
    player = source.controller
    _reduce_libram_costs(player)