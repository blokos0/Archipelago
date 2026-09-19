from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range, OptionSet, Toggle

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

    # valid_keys_casefold = True

class TrapPercentage(Range):
    """
    Replaces X% of filler items with traps.
    """
    
    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    default = 20

class NiconicoTrap(Toggle):
    """
    Enables the Niconico Trap: Comments fly accros the screen.
    """
    
    display_name = "Niconico Trap"
    
    default = True

@dataclass
class SMB1ROptions(PerGameCommonOptions):
    starting_world: StartingWorld
    campaigns: Campaigns
    trap_percentage: TrapPercentage
    niconico_trap: NiconicoTrap

option_groups = [
    OptionGroup(
        "Gameplay",
        [StartingWorld, Campaigns],
    ),
     OptionGroup(
        "Traps",
        [TrapPercentage, NiconicoTrap],
    )
]

option_presets = {
    "Default": {
        "campaigns": ["SMB1"],
        "starting_world": 1,
        "trap_percentage": 20,
        "niconico_trap": True
    }
}
