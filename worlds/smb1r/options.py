from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range, OptionSet

class StartingWorld(Range):
    """
    Which world will be unlocked by default. (You can use YAML randomization for extra randomness!)
    """

    display_name = "Starting World"

    range_start = 1
    range_end = 8

    default = 1

class Campaigns(OptionSet):
    """
    Which campaigns will be available for play. (doesnt do anything right now
    """

    display_name = "Campaigns"

    valid_keys = ["smb", "tll", "ann", "smbs"]
    default = ["smb"]
    
    valid_keys_casefold = True

@dataclass
class SMB1ROptions(PerGameCommonOptions):
    starting_world: StartingWorld
    campaigns: Campaigns

option_groups = [
    OptionGroup(
        "The Only Group:tm:",
        [StartingWorld, Campaigns],
    )
]

option_presets = {
    "The Only Preset:tm:": {
        "campaigns": ["SMB"],
        "starting_world": 1
    }
}
