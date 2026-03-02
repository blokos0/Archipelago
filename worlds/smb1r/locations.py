from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SMB1RWorld

LOCATION_NAME_TO_ID = {}

ind = 1
for i in range(8):
    for j in range(4):
        LOCATION_NAME_TO_ID[f"{i + 1}-{j + 1}"] = ind
        ind += 1

for z in range(3):
    LOCATION_NAME_TO_ID[f"-{z + 1}"] = ind
    ind += 1

class SMB1RLocation(Location):
    game = "Super Mario Bros. Remastered"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_locations(world: SMB1RWorld) -> None:
    for i in range(8):
        region = world.get_region(f"World {i + 1}")
        region.add_locations(get_location_names_with_ids([f"{i + 1}-1", f"{i + 1}-2", f"{i + 1}-3", f"{i + 1}-4"]))
        if i + 1 == 8:
            region.add_event(
                "Completed 8-4", "Victory", location_type=SMB1RLocation, item_type=items.SMB1RItem
            )

    worldminus1 = world.get_region("World -1")
    worldminus1.add_locations(get_location_names_with_ids(["-1", "-2", "-3"]))
