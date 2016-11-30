from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()

length = 6
width = 6
type = 18
height= 5
z = z-3
x = x-3
y = y-1

mc.setBlocks(x, y, z, x+length, y, z+width, type)

for j in range(1,height):
    
    for i in range(0,length+1):
        mc.setBlock(x+i, y+j, z, type)
        mc.setBlock(x+i, y+j, z+width, type)

    for i in range(0,width+1):
        mc.setBlock(x, y+j, z+i, type)
        mc.setBlock(x+length, y+j, z+i, type)

