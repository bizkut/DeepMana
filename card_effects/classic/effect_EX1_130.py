"""EX1_130 - Noble Sacrifice: When an enemy attacks, summon a 2/1 Defender as the new target."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    """
    Triggered when an enemy attacks.
    Summon a 2/1 Defender and redirect the attack.
    """
    if attacker and attacker.controller != owner and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        # Create a 2/1 Defender (using Wisp as base, modify stats)
        defender_card = create_card("CS2_231", game)  # Wisp
        if defender_card:
            defender_minion = Minion(defender_card.data, game)
            defender_minion.attack = 2
            defender_minion.health = 1
            defender_minion.max_health = 1
            defender_minion.name = "Defender"
            defender_minion.controller = owner
            owner.summon(defender_minion)
            # Note: attack redirection would require more complex logic
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
