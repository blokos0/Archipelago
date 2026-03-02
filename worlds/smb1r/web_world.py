from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class SMB1RWebWorld(WebWorld):
    game = "Super Mario Bros. Remastered"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Super Mario Bros. Remastered for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["blokos"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
