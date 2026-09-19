from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has

if TYPE_CHECKING:
    from .world import SMB1RWorld

def set_all_rules(world: SMB1RWorld) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: SMB1RWorld) -> None:
    for i in range(8):
        entrance = world.get_entrance(f"Menu to World {i + 1}")
        world.set_rule(entrance, Has(f"World {i + 1} Item"))

    worldminus1entrance = world.get_entrance("World 1 to World -1")
    world.set_rule(worldminus1entrance, Has("World 1 Item"))

def set_completion_condition(world: SMB1RWorld) -> None:
    world.set_completion_rule(Has("Bowser Defeated", count=9))
