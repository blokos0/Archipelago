from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import SMB1RWorld

def set_all_rules(world: SMB1RWorld) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: SMB1RWorld) -> None:
    for i in range(8):
        entrance = world.get_entrance(f"Level Select to World {i + 1}")
        set_rule(entrance, lambda state: state.has(f"World {i + 1} Item", world.player))

    worldminus1entrance = world.get_entrance("World 1 to World -1")
    set_rule(worldminus1entrance, lambda state: state.has("World 1 Item", world.player))

def set_completion_condition(world: SMB1RWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
