import nuke

def createInput(input, input_name, node, input_connected, x, y):
    """
    This function creates one input taking as a reference the input, their name, the node that will connected, which connection, and with xpos and ypos will connected.
      
    Args:
      input(node): Input node. Remember to use: "nuke.toNode('name of the input')" eg: nuke.toNode("InputUTILS")
      input_name(str): name of the input
      node(str): which node will be connected
      input_connected (int): which input will be connected in the node.
      x(int) = in which xpos will be connected
      y(int) = in which ypos will be connected
      
    Returns:
      New input created with specific name, connected in specific node and position (xy).
  
    Raises:
      None.
      """

    if not input:
        newInput = nuke.createNode('Input', f"name {input_name}", inpanel=False) # Create Input node 
        nodeConnected = nuke.toNode(node)

        if newInput:
            nodeConnected.setInput(input_connected, newInput)
            xpos = nodeConnected.xpos() + x
            ypos = nodeConnected.ypos() + y
            if xpos and ypos:
                newInput.setXpos(xpos)
                newInput.setYpos(ypos)
            else:
                print(f"{input} not connected to {node}")

"""
## KNOB CHANGED EXAMPLE:

import nuke # if it wasn't imported it

n = nuke.thisNode()
k = nuke.thisKnob()

checkCustom = nuke.toNode('InputCustom')

if k().name() == 'choice':
    if n['choice'].value() == 'Custom':
        createInput(checkCustom, 'InputCustom', 'SwitchMap', 1, +100, 0)
    else:
        print("Input wasn't created it")
else:
    if checkCustom:
        nuke.delete(checkCustom)
"""
