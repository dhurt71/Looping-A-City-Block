# CSUF CPSC 305
# Mini-Project 10
#
# Group Members:
#   Devon Hurt
#   

import maya.cmds as cmds
zmove = 0
inputz = 6
inputx = 5

cmds.displayRGBColor(list=True)
#Street color
streetshade = cmds.shadingNode('lambert', n='streetcolor',asShader=True)
cmds.setAttr((streetshade + '.color'), 0.0,0.0,0.0, type = 'double3')
#Tall building color
tallshade = cmds.shadingNode('lambert', n='tallcolor',asShader=True)
cmds.setAttr((tallshade + '.color'), 0.2,0.3,0.5, type = 'double3')
#Medium building color
mediumshade = cmds.shadingNode('lambert', n='mediumcolor',asShader=True)
cmds.setAttr((mediumshade + '.color'), 0.2,0.1,0.0, type = 'double3')
#Short building color
shortshade = cmds.shadingNode('lambert', n='shortcolor',asShader=True)
cmds.setAttr((shortshade + '.color'), 0.5,0.1,0.1, type = 'double3')
#Small building color
smallshade = cmds.shadingNode('lambert', n='smallcolor',asShader=True)
cmds.setAttr((smallshade + '.color'), 0.6,0.5,0.5, type = 'double3')
#Median color
medianshade = cmds.shadingNode('lambert', n='mediancolor',asShader=True)
cmds.setAttr((medianshade + '.color'), 0.8,0.8,0.0, type = 'double3')


for i in range(0,inputz):
    xmove = 2
    #Veritcal streets
    cmds.polyCube(w=2,h=.01,d=.3)
    cmds.move(0,0,1 + zmove)
    cmds.hyperShade(assign = streetshade)
    
    #Medians
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.move(.5,.01,1 + zmove)
    cmds.hyperShade(assign = medianshade)
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.move(-.5,.01,1 + zmove)
    cmds.hyperShade(assign = medianshade)
    
    #Vertical streets
    cmds.polyCube(w=2,h=.01,d=.3)
    cmds.move(0,0,-1 + zmove)
    cmds.hyperShade(assign = streetshade)
    
    #Medians
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.move(.5,.01,-1 + zmove)
    cmds.hyperShade(assign = medianshade)
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.move(-.5,.01,-1 + zmove)
    cmds.hyperShade(assign = medianshade)

    #Horizontal streets
    cmds.polyCube(w=2,h=.01,d=.3)
    cmds.rotate(0,'90deg',0)
    cmds.move(-1,0,0 + zmove)
    cmds.hyperShade(assign = streetshade)
    
    #Medians
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.rotate(0,'90deg',0)
    cmds.move(-1,.01,.5 + zmove)
    cmds.hyperShade(assign = medianshade)
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.rotate(0,'90deg',0)
    cmds.move(-1,.01,-.5+ zmove)
    cmds.hyperShade(assign = medianshade)
    
    #Horizontal streets
    cmds.polyCube(w=2,h=.01,d=.3)
    cmds.rotate(0,'90deg',0)
    cmds.move(1,0,0 + zmove)
    cmds.hyperShade(assign = streetshade)
    
    #Medians
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.rotate(0,'90deg',0)
    cmds.move(1,.01,.5 + zmove)
    cmds.hyperShade(assign = medianshade)
    cmds.polyCube(w=.25,h=.01,d=.04)
    cmds.rotate(0,'90deg',0)
    cmds.move(1,.01,-.5+ zmove)
    cmds.hyperShade(assign = medianshade)
    
    #Medium Buildings
    cmds.polyCube(w=.4,h=.5,d=.8)
    cmds.move(.6,.25,.4 + zmove)
    cmds.hyperShade(assign = mediumshade)

    cmds.polyCube(w=.4,h=.5,d=.8)
    cmds.rotate(0,'90deg',0)
    cmds.move(-.4,.25,-.6 + zmove)
    cmds.hyperShade(assign = mediumshade)

    #Tall Buildings
    cmds.polyCube(w=.4,h=1,d=.4)
    cmds.move(-.6,.5,.6 + zmove)
    cmds.hyperShade(assign = tallshade)

    cmds.polyCube(w=.4,h=1,d=.4)
    cmds.move(.6,.5,-.6 + zmove)
    cmds.hyperShade(assign = tallshade)

    #Short Buildings
    cmds.polyCube(w=.4,h=.25,d=.8)
    cmds.move(-.6,.125,0 + zmove)
    cmds.hyperShade(assign = shortshade)

    cmds.polyCube(w=.4,h=.25,d=.8)
    cmds.rotate(0,'90deg',0)
    cmds.move(0,.125,.6 + zmove)
    cmds.hyperShade(assign = shortshade)

    #Small Buildings
    cmds.polyCube(w=.4,h=.3,d=.4)
    cmds.move(.6,.15,-.2 + zmove)
    cmds.hyperShade(assign = smallshade)

    cmds.polyCube(w=.4,h=.3,d=.4)
    cmds.rotate(0,'90deg',0)
    cmds.move(.2,.15,-.6 + zmove)
    cmds.hyperShade(assign = smallshade)
    
    for i in range(0,inputx - 1):
        #Veritcal streets
        cmds.polyCube(w=2,h=.01,d=.3)
        cmds.move(0 + xmove,0,-1 + zmove)
        cmds.hyperShade(assign = streetshade)
        
        #Medians
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.move(-.5 + xmove,.01,-1 + zmove)
        cmds.hyperShade(assign = medianshade) 
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.move(.5 + xmove,.01,-1 + zmove)
        cmds.hyperShade(assign = medianshade)
        
        #Vertical streets
        cmds.polyCube(w=2,h=.01,d=.3)
        cmds.move(0 + xmove,0,1 + zmove)
        cmds.hyperShade(assign = streetshade)
        
        #Medians
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.move(-.5 + xmove,.01,1 + zmove)
        cmds.hyperShade(assign = medianshade)
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.move(.5 + xmove,.01,1 + zmove)
        cmds.hyperShade(assign = medianshade)

        #Horizontal streets
        cmds.polyCube(w=2,h=.01,d=.3)
        cmds.rotate(0,'90deg',0)
        cmds.move(-1 + xmove,0,0 + zmove)
        cmds.hyperShade(assign = streetshade)
        
        #Medians
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.rotate(0,'90deg',0)
        cmds.move(-1 + xmove,.01,.5 + zmove)
        cmds.hyperShade(assign = medianshade)
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.rotate(0,'90deg',0)
        cmds.move(-1 + xmove,.01,-.5 + zmove)
        cmds.hyperShade(assign = medianshade)
        
        #Horizontal streets
        cmds.polyCube(w=2,h=.01,d=.3)
        cmds.rotate(0,'90deg',0)
        cmds.move(1 + xmove,0,0 + zmove)
        cmds.hyperShade(assign = streetshade)
        
        #Medians
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.rotate(0,'90deg',0)
        cmds.move(1 + xmove,.01,-.5 + zmove)
        cmds.hyperShade(assign = medianshade)
        cmds.polyCube(w=.25,h=.01,d=.04)
        cmds.rotate(0,'90deg',0)
        cmds.move(1 + xmove,.01,.5 + zmove)
        cmds.hyperShade(assign = medianshade)
        
        #Medium Buildings
        cmds.polyCube(w=.4,h=.5,d=.8)
        cmds.move(.6 + xmove,.25,.4 + zmove)
        cmds.hyperShade(assign = mediumshade)

        cmds.polyCube(w=.4,h=.5,d=.8)
        cmds.rotate(0,'90deg',0)
        cmds.move(-.4 + xmove,.25,-.6 + zmove)
        cmds.hyperShade(assign = mediumshade)

        #Tall Buildings
        cmds.polyCube(w=.4,h=1,d=.4)
        cmds.move(-.6 + xmove,.5,.6 + zmove)
        cmds.hyperShade(assign = tallshade)

        cmds.polyCube(w=.4,h=1,d=.4)
        cmds.move(.6 + xmove,.5,-.6 + zmove)
        cmds.hyperShade(assign = tallshade)

        #Short Buildings
        cmds.polyCube(w=.4,h=.25,d=.8)
        cmds.move(-.6 + xmove,.125,0 + zmove)
        cmds.hyperShade(assign = shortshade)

        cmds.polyCube(w=.4,h=.25,d=.8)
        cmds.rotate(0,'90deg',0)
        cmds.move(0 + xmove,.125,.6 + zmove)
        cmds.hyperShade(assign = shortshade)

        #Small Building
        cmds.polyCube(w=.4,h=.3,d=.4)
        cmds.move(.6 + xmove,.15,-.2 + zmove)
        cmds.hyperShade(assign = smallshade)

        cmds.polyCube(w=.4,h=.3,d=.4)
        cmds.rotate(0,'90deg',0)
        cmds.move(.2 + xmove,.15,-.6 + zmove)
        cmds.hyperShade(assign = smallshade)
    
        xmove = xmove + 2

    zmove = zmove + 2