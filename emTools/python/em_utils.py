import nuke

def reload_nodes():
    for read in nuke.allNodes('Read'):
        read['reload'].execute()
        print(f"Successful update {read.name()}")


def read_write():
    write = nuke.selectedNodes('Write')

    if not write:
        nuke.message('No Write node selected. Please, try again selecting a Write Node.')
        return

    for w in write:
        write_name = w['name'].value()
        read = nuke.createNode('Read', inpanel=False)
        read.setName('Check_Renders')
        tcl_exp = "[value " + write_name + ".file]"
        read['file'].setValue(tcl_exp)
        read['first'].setExpression('first_frame')
        read['last'].setExpression('last_frame')
        read['tile_color'].setValue(0x7fff)


def extraCleanCache():
    # Clear Cache
    def cacheClean():
        ram = nuke.clearRAMCache()
        cache = nuke.clearDiskCache()
        print('Successful clean RAM and Disk Cache')

    cacheClean()
    reload_nodes()


def gui():  
    for n in nuke.selectedNodes():
        if n["disable"].hasExpression():
            n["disable"].clearAnimated()
            n["disable"].setValue(False)
        else:
            n["disable"].setExpression("$gui")


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
        sm.addCommand("Read to check Renders", "em_utils.read_write()", "Shift+W")
        sm.addCommand("Extra Clean Cache", "em_utils.extraCleanCache()", "")
        sm.addCommand("Set and remove $gui", "em_utils.gui()", "Shift+D", )


menu_utils()