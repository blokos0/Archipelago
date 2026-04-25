from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SMB1RWorld

ITEM_NAME_TO_ID = {}
ITEM_CLASSIFICATIONS = {}

ind = 1
for i in range(8):
    ITEM_NAME_TO_ID[f"World {i + 1} Item"] = ind
    ITEM_CLASSIFICATIONS[f"World {i + 1} Item"] = ItemClassification.progression
    ind += 1

ITEM_NAME_TO_ID["NOTHING!"] = ind
ITEM_CLASSIFICATIONS["NOTHING!"] = ItemClassification.filler

class SMB1RItem(Item):
    game = "Super Mario Bros. Remastered"

def create_item_with_correct_classification(world: SMB1RWorld, name: str) -> SMB1RItem:
    classification = ITEM_CLASSIFICATIONS[name]
    return SMB1RItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SMB1RWorld) -> None:
    itempool: list[Item] = []
    for i in range(8):
        item = world.create_item(f"World {i + 1} Item")
        if i + 1 == world.options.starting_world.value:
            world.push_precollected(item)
        else:
            itempool.append(item)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
