import nuke
import nukescripts

## Add PluginPaths to tools and icons
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')
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
    print("Not imported OCIO setup nodes")
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
n = toolbar.addMenu("emTools", "emTools.png")
g = n.addMenu("Gizmos")
t = n.addMenu("Toolsets")

curDir = os.path.dirname(os.path.abspath(__file__))
curDir = curDir.replace('\\', '/')

# Custom gizmo creation with their menu
gizmos = ['emDepthFix', 'emGlow', 'emMatte', 'emSmartGrade'] # List of Gizmos , add a new gizmo between '' and ',''. Also, place them in 'gizmo' folder too.
for gizmo in gizmos :
  g.addCommand(gizmo, "nuke.createNode(\""+gizmo+"\")")

# Custom toolset creation with their menu
toolsets = ['CG_denoiser', 'CG_denoiser_per_AOV'] # List of ToolSets , add a new ToolSet between '' and placed in '.nk' folder.
for toolset in toolsets:
  t.addCommand(toolset, "with nuke.lastHitGroup():\n  nuke.loadToolset(\""+curDir+"/nk_files/"+toolset+".nk\")")
