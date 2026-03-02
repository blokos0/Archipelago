from test.bases import WorldTestBase

from ..world import SMB1RWorld

class SMB1RTestBase(WorldTestBase):
    game = "Super Mario Bros. Remastered"
    world: SMB1RWorld
