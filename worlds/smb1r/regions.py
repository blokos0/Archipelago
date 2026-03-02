from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SMB1RWorld

def create_and_connect_regions(world: SMB1RWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: SMB1RWorld) -> None:
    regions = []

    regions.append(Region("Level Select", world.player, world.multiworld))
    for i in range(8):
        regions.append(Region(f"World {i + 1}", world.player, world.multiworld))

    regions.append(Region("World -1", world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: SMB1RWorld) -> None:
    level_select = world.get_region("Level Select")

    for i in range(8):
        region = world.get_region(f"World {i + 1}")
        level_select.connect(region, f"Level Select to World {i + 1}")
    
    world1 = world.get_region("World 1")
    worldminus1 = world.get_region("World -1")

    world1.connect(worldminus1, "World 1 to World -1")
