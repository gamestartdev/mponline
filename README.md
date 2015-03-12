# mponline

Today's Minecraft server URL

    ec2-54-164-208-168.compute-1.amazonaws.com

Write your Python spells with the [online code editor](http://ec2-54-164-208-168.compute-1.amazonaws.com).

    from mcapi import *
    
    setblock(0, 80, 0, BlockType.GoldBlock)
    cube(0, 90, 0, BlockType.DiamondBlock, 6)
    
    player = getplayer('heyandy889')
    explosion( player.x, player.y, player.z, 10 )
    
    for i in range(5):
        bolt( player.x, player.y, player.z )
        sleep(1)

