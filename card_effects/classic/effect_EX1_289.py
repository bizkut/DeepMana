"""EX1_289 - Ice Barrier: When your hero is attacked, gain 8 Armor."""

def on_hero_attacked(game, owner, secret, attacker=None, defender=None):
    """
    Triggered when the secret owner's hero is attacked.
    Gain 8 Armor.
    """
    if defender and defender == owner.hero:
        owner.hero.armor += 8
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
