from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as smb1roptions

from BaseClasses import Region

class SMB1RWorld(World):
    """
    Super Mario Bros. Remastered is a fanmade celebration of the original Super Mario Bros. series.
    This randomizer is (placeholder text make sure to update it
    """

    game = "Super Mario Bros. Remastered"

    web = web_world.SMB1RWebWorld()

    options_dataclass = smb1roptions.SMB1ROptions
    options: smb1roptions.SMB1ROptions

    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)
        #self.multiworld.local_early_items[self.player][f"World {self.options.starting_world} Item"] = 1
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def create_item(self, name: str) -> items.SMB1RItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return "NOTHING!"

    def fill_slot_data(self) -> Mapping[str, Any]:
        levelorder = {}
        for i in range(8):
            levels = [1, 2, 3, 4]
            self.random.shuffle(levels)
            levelorder[i + 1] = levels
        opts = self.options.as_dict(
            "starting_world", "campaigns"
        )
        return opts | {"levelorder": levelorder}
