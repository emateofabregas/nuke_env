import os
import nuke
import nukescripts

## Add PluginPaths to tools and icons
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./nk_files')
nuke.pluginAddPath('./python')


## Nuke Menu for Python Scripts
# Python Scripts
try:
    import em_alignnodes
except:
    print("Not imported Align Nodes shortcut")
    pass

try:
    import em_ocioSetUp
except:
    print("Not imported Knob Default nodes")
    pass

try:
    import em_startUpNodes
except:
    print("Not imported Knob Default nodes")
    pass

try:
    import em_utils
except:
    print("Not  imported Utilities")
    pass


## Create emTools Menu and submenus
toolbar = nuke.menu("Nodes")
menu = toolbar.addMenu("emTools", "emTools.png")
g = menu.addMenu("Gizmos")
t = menu.addMenu("Toolsets")

curDir = os.path.dirname(os.path.abspath(__file__))
curDir = curDir.replace('\\', '/')
print(curDir)

# Custom gizmo creation with their menu
gizmos = ['emArtisticLens', 'emBokehPlus', 'emBrush', 'emChromatic', 'emDepthFix', 'emEdgeSatCorrect', 'emFog' , 'emGlow', 'emKeyChannelMix', 'emLightWrap','emMatte', 'emSimpleRelight', 'emSmartUpscale', 'emUnpremultAlpha', 'emVignette'] # List of Gizmos , add a new gizmo between '' and placed in 'gizmo' folder too.
for gizmo in gizmos :
    g.addCommand(gizmo, "nuke.createNode(\""+gizmo+"\")")

# Adding new Merge nodes in the Merge Menu
merge_nodes = ['From', 'Geometric', 'Plus', 'Stencil', 'Under']
for node in merge_nodes:
    toolbar.addCommand("Merge/Merges/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Adding new Channel Merge nodes in the Channel Merge Menu
channel_merge_nodes = ['CMFrom', 'CMMax', 'CMMultiply', 'CMPlus']
for node in channel_merge_nodes:
    toolbar.addCommand("Channel/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Adding new Keyer nodes in the Keyer Menu
keyers = ['CryptomatteP', 'CryptomatteUnP']
for node in keyers:
    toolbar.addCommand("Keyer/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Adding new Filter nodes in the Filter Menu
filters = ['DepthEdges']
for node in filters:
    toolbar.addCommand("Filter/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Adding new Maths nodes in the Maths Menu
maths = ['BlackRange']
for node in maths:
    toolbar.addCommand("Color/Math/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Adding new Maths nodes in the Maths Menu
other = ['BlinkScript']
for node in other:
    toolbar.addCommand("Other/" + node,f"nuke.loadToolset('{curDir}/nk_files/{node}.nk')", icon=f"{node}.png")

# Custom toolset creation with their menu
toolsets = ['DenoiseAndHold' ,'emDepthFog', 'emLoadReference', 'FilterBlue', 'GlowNonSaturated', 'HighDenoisePerObject', 'CG_Template', 'NtoUV', 'Relight', 'RestToUV'] # List of ToolSets , add a new ToolSet between '' and placed in '.nk' folder.
for toolset in toolsets:
  t.addCommand(toolset, "with nuke.lastHitGroup():\n  nuke.loadToolset(\""+curDir+"/nk_files/"+toolset+".nk\")")
