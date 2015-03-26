# mponline

Today's Minecraft server URL

    ec2-54-164-208-168.compute-1.amazonaws.com

Write your Python spells with the <a href="http://ec2-54-164-208-168.compute-1.amazonaws.com" target="_blank">online code editor</a>. See the example code below!

    from mcapi import *
    
    setblock(0, 80, 0, GOLD_BLOCK)
    cube(0, 90, 0, DIAMOND_BLOCK, 6)
    
    player = getplayer('heyandy889')
    explosion( player.x, player.y, player.z, 10 )
    
    for i in range(5):
        bolt( player.x, player.y, player.z )
        sleep(1)
    
    targetblock = lookingat(player)
    cube(targetblock.x, targetblock.y, targetblock.z, ICE, 4)
    
