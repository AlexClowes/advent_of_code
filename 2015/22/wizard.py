import heapq


magic_missile_damage = 4
drain_damage = 2
shield_duration = 6
shield_strength = 7
poison_duration = 6
poison_damage = 3
recharge_duration = 5
recharge_strength = 101
spell_cost = {
    "magic missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}
boss_damage = 8


def apply_status_effects(state):
        # Shield
        if state["shield_turns"] > 0:
            state["player_armor"] = shield_strength
            state["shield_turns"] -= 1
        else:
            state["player_armor"] = 0
        # Poison
        if state["poison_turns"] > 0:
            state["boss_health"] -= poison_damage
            state["poison_turns"] -= 1
        # Recharge
        if state["recharge_turns"] > 0:
            state["player_mana"] += recharge_strength
            state["recharge_turns"] -= 1


def main():
    initial_state = {
        "player_health": 50,
        "player_mana": 500,
        "player_armor": 0,
        "boss_health": 55,
        "shield_turns": 0,
        "poison_turns": 0,
        "recharge_turns": 0,
    }

    print(min_mana_spent(initial_state))


def min_mana_spent(initial_state):
    entry_no = 0
    q = [(0, entry_no, initial_state)]
    while q:
        mana_spent, _, state = heapq.heappop(q)

        # Apply status effects
        apply_status_effects(state)
        if state["boss_health"] <= 0:
            return mana_spent

        available_spells = [
            (spell, cost) for spell, cost in spell_cost.items()
            if cost <= state["player_mana"]
        ]
        if not available_spells:
            continue
        for spell, cost in available_spells:
            # Player turn
            new_state = state.copy()
            new_state["player_mana"] -= cost
            new_mana_spent = mana_spent + cost
            if spell == "magic missile":
                new_state["boss_health"] -= magic_missile_damage
            elif spell == "drain":
                new_state["boss_health"] -= drain_damage
                new_state["player_health"] += drain_damage
            elif spell == "shield":
                if new_state["shield_turns"] > 0:
                    continue
                new_state["shield_turns"] = shield_duration
            elif spell == "poison":
                if new_state["poison_turns"] > 0:
                    continue
                new_state["poison_turns"] = poison_duration
            elif spell == "recharge":
                if new_state["recharge_turns"] > 0:
                    continue
                new_state["recharge_turns"] = recharge_duration
            else:
                raise ValueError(f"Unknown spell {spell}")
            if new_state["boss_health"] <= 0:
                return new_mana_spent

            # Boss turn
            apply_status_effects(new_state)
            if new_state["boss_health"] <= 0:
                return new_mana_spent
            new_state["player_health"] -= max(1, boss_damage - new_state["player_armor"])
            if new_state["player_health"] > 0:
                entry_no += 1
                heapq.heappush(q, (new_mana_spent, entry_no, new_state))


if __name__ == "__main__":
    main()
