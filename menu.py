import nuke
import emTools

if emTools:
    print("Imported emTools. Last update: 6th of October 2025")
else:
    print("Not imported emTools")

if nuke.NUKE_VERSION_MAJOR < 11:
    # PySide for Nuke up to 10 and other plugins
    from PySide.QtGui import QPushButton
    import KnobScripter
elif nuke.NUKE_VERSION_MAJOR < 16:
    # PySide2 for default Nuke 11
    from PySide2.QtWidgets import QPushButton
    import KnobScripter
else:
    # PySide6 for Nuke 16+
    from PySide6.QtWidgets import QPushButton
