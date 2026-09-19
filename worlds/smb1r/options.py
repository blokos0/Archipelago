from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range, OptionSet

class StartingWorld(Range):
    """
    Which world will be unlocked by default? (You can use YAML randomization for extra randomness!)
    """

    display_name = "Starting World"

    range_start = 1
    range_end = 8

    default = 1

class Campaigns(OptionSet):
    """
    Which campaigns will be available and accounted for in randomization?
    """

    display_name = "Campaigns"

    valid_keys = ["SMB1", "SMBLL", "SMBS", "SMBANN"]
    default = ["SMB1"]
    
    valid_keys_casefold = True

@dataclass
class SMB1ROptions(PerGameCommonOptions):
    starting_world: StartingWorld
    campaigns: Campaigns

option_groups = [
    OptionGroup(
        "Gameplay",
        [StartingWorld, Campaigns],
    )
]

option_presets = {
    "Default": {
        "campaigns": ["SMB1"],
        "starting_world": 1
    }
}
