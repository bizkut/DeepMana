"""EX1_287 - Counterspell: When your opponent casts a spell, Counter it."""

def on_spell_cast(game, owner, secret, spell=None, target=None):
    """
    Triggered when opponent casts a spell.
    Returns True if the secret should trigger (countering the spell).
    """
    if spell:
        # The spell is countered - handled in game.py
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
