import nuke

def set_ocio():
    if nuke.root()['colorManagement'].value() == 'Nuke':
        nuke.root()['colorManagement'].setValue('OCIO')

def modify_ocio():
    ocio = nuke.usingOcio()

    if ocio:
        nuke.root()['int8Lut'].setValue('Output - sRGB')
        nuke.root()['int16Lut'].setValue('Output - sRGB')
    else:
        nuke.root()['int8Lut'].setValue('sRGB')
        nuke.root()['int16Lut'].setValue('sRGB')

nuke.addOnCreate(set_ocio, nodeClass='Root')
nuke.addOnCreate(modify_ocio, nodeClass='Root')