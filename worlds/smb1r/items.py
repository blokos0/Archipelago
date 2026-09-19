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

traps = ["Niconico Trap"]
for t in traps:
    ITEM_NAME_TO_ID[t] = ind
    ITEM_CLASSIFICATIONS[t] = ItemClassification.trap
    ind += 1

ITEM_NAME_TO_ID["NOTHING!"] = ind
ITEM_CLASSIFICATIONS["NOTHING!"] = ItemClassification.filler

class SMB1RItem(Item):
    game = "Super Mario Bros. Remastered"

def create_item_with_correct_classification(world: SMB1RWorld, name: str) -> SMB1RItem:
    classification = ITEM_CLASSIFICATIONS[name]
    return SMB1RItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def get_random_filler_item_name(world: SMB1RWorld) -> str:
    enabled_traps = []
    if world.options.niconico_trap.value:
        enabled_traps.append("Niconico Trap")

    if len(enabled_traps) > 0: # account for having >0 trap percentage but no enabled traps (lol
        if world.random.randint(0, 99) < world.options.trap_percentage.value:
            return world.random.choice(enabled_traps)
    return "NOTHING!"

def create_all_items(world: SMB1RWorld) -> None:
    itempool: list[Item] = []
    for i in range(8):
        item = world.create_item(f"World {i + 1} Item")
        if i + 1 == world.options.starting_world.value:
            world.push_precollected(item)
        else:
            itempool.append(item)

    empty_spots = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    itempool += [world.create_filler() for _ in range(empty_spots)]

    world.multiworld.itempool += itempool
