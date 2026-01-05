"""Effect for Wayward Probe (SC_500).

Card Text: Battlecry and Deathrattle: Get a random Starship Piece.
"""

import random

# Starship Pieces from The Great Dark Beyond
STARSHIP_PIECES = [
    'SC_401', 'SC_402', 'SC_403', 'SC_404', 'SC_405',
    'SC_406', 'SC_407', 'SC_408', 'SC_410', 'SC_411', 'SC_412'
]


def _get_starship_piece(game, player):
    """Add a random Starship Piece to hand."""
    from simulator.factory import create_card
    
    piece_id = random.choice(STARSHIP_PIECES)
    piece = create_card(piece_id, game)
    if piece:
        player.add_to_hand(piece)


def battlecry(game, source, target):
    player = source.controller
    _get_starship_piece(game, player)


def deathrattle(game, source):
    player = source.controller
    _get_starship_piece(game, player)