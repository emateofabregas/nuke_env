import nuke

def reload_nodes():
    for read in nuke.allNodes('Read'):
        read['reload'].execute()
        print(f"Successful update {r.name()}")


def unicorn_read():
    read = nuke.createNode('Read', inpanel=False)
    read.setName('Check_Renders')
    read['file'].setValue('[value Write1.file]')
    read['first'].setExpression('first_frame')
    read['last'].setExpression('last_frame')
    read['tile_color'].setValue(hex_color_to_rgb(0,1,0)) #Modify color of the node here.

    nuke.message("Successful created 'Check_Renders' node!")


def extraCleanCache():
    # Clear Cache
    def cacheClean():
        ram = nuke.clearRAMCache()
        cache = nuke.clearDiskCache()
        print('Successful clean RAM and Disk Cache')

    cacheClean()
    reload_nodes()


### Nuke Menu
utils_MenusLoaded = False
 
def menu_utils():
    global utils_MenusLoaded
    if not utils_MenusLoaded:
        utils_MenusLoaded = True
        mm = nuke.menu("Nuke")
        cm = mm.addMenu("emTools")
        sm = cm.addMenu("Utils")
        sm.addCommand("Reload Reads", "em_utils.reload_nodes()", "Shirt+R")
        sm.addCommand("Read to check Renders", "em_utils.unicorn_read()", "Shift+W")
        sm.addCommand("Extra Clean Cache", "em_utils.extraCleanCache()", "")


menu_utils()