import nuke

#Align Nodes Shortcuts
def align_selected_nodes_h_c():
    # Fetch all selected nodes in the Nuke environment
    selected_nodes = nuke.selectedNodes() 
    if not selected_nodes:
        # Display a message and exit if no nodes are selected
        nuke.message("No nodes selected.") 
        return 
    
    # Prompt the user to input custom spacing between nodes
    spacing_p = nuke.getInput('Enter custom Spacing', '250')
    
    if not spacing_p: 
        # Display a message and exit if no spacing value is entered
        nuke.message("No 'Spacing' units set")
        return    
    
    if spacing_p:
        # Convert the input spacing value from string to integer
        spacing = int(spacing_p) 
    
    # Sort selected nodes based on their x positions
    selected_nodes.sort(key=lambda x: x.xpos())
    first_node = selected_nodes[0]
    # Calculate initial x position for the first node, including custom spacing
    x_position = first_node.xpos() + first_node.screenWidth() + spacing
    y_position = first_node.ypos()

    # Align all other selected nodes based on the first node's position
    for node in selected_nodes[1:]:  # Skip the first node
        node.setYpos(y_position)  # Set y position to be the same as the first node
        node.setXpos(x_position)  # Update x position to the new aligned position
        # Increment x position for the next node in the list
        x_position += node.screenWidth() + spacing

def align_selected_nodes_v_c():
    # Fetch all selected nodes in the Nuke environment
    selected_nodes = nuke.selectedNodes() 
    if not selected_nodes:
        # Display a message and exit if no nodes are selected
        nuke.message("No nodes selected.") 
        return 

    # Prompt the user to input custom vertical spacing between nodes
    spacing_p = nuke.getInput('Enter custom spacing vertically', '250')
    
    if not spacing_p: 
        # Display a message and exit if no spacing value is entered
        nuke.message("No 'Spacing' units set")
        return    
    
    if spacing_p:
        # Convert the input spacing value from string to integer
        spacing = int(spacing_p) 
    
    # Sort selected nodes based on their y positions to prepare for vertical alignment
    selected_nodes.sort(key=lambda x: x.ypos())
    first_node = selected_nodes[0]
    # Set the initial x and y position for alignment based on the first node
    x_position = first_node.xpos()
    y_position = first_node.ypos() + first_node.screenHeight() + spacing

    # Align all other selected nodes based on the first node's position
    for node in selected_nodes[1:]:  # Skip the first node
        node.setYpos(y_position)  # Set y position for vertical alignment
        node.setXpos(x_position)  # Maintain x position as that of the first node
        # Increment y position for the next node in the list
        y_position += node.screenHeight() + spacing

def align_selected_nodes_h_100():
    # Fetch all selected nodes in the Nuke environment
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        # Display a message and exit if no nodes are selected
        nuke.message("No nodes selected to align horizontally.")
        return
    
    # Sort selected nodes by their X position to align from left to right
    selected_nodes.sort(key=lambda node: node.xpos())
    
    # Establish the base alignment using the first node as reference
    first_node = selected_nodes[0]
    x_position = first_node.xpos() + first_node.screenWidth() + 100  # Set initial x position
    y_position = first_node.ypos()  # Maintain a constant y position for all nodes

    # Align each subsequent node at the calculated x position
    for node in selected_nodes[1:]:  # Starting from the second node
        node.setYpos(y_position)  # Set the y position same as the first node
        node.setXpos(x_position)  # Move each node to the new x position
        x_position += node.screenWidth() + 100  # Update the x position for the next node

def align_selected_nodes_v_100():
    # Fetch all selected nodes in the Nuke environment
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        # Display a message and exit if no nodes are selected
        nuke.message("No nodes selected to align vertically.")
        return
    
    # Sort selected nodes by their Y position to align from top to bottom
    selected_nodes.sort(key=lambda node: node.ypos())
    
    # Establish the base alignment using the first node as reference
    first_node = selected_nodes[0]
    x_position = first_node.xpos()  # Maintain a constant x position for all nodes
    y_position = first_node.ypos() + first_node.screenHeight() + 100  # Set initial y position

    # Align each subsequent node at the calculated y position
    for node in selected_nodes[1:]:  # Starting from the second node
        node.setYpos(y_position)  # Move each node to the new y position
        node.setXpos(x_position)  # Set the x position same as the first node
        y_position += node.screenHeight() + 100  # Update the y position for the next node

### Nuke Menu
alignNodes_MenusLoaded = False
 
def menu_align():
    global alignNodes_MenusLoaded
    if not alignNodes_MenusLoaded:
        alignNodes_MenusLoaded = True
        mm = nuke.menu("Nuke")
        cm = mm.addMenu("emTools")
        sm = cm.addMenu("Align Nodes")
        sm.addCommand("Align Vertically", "em_alignnodes.align_selected_nodes_v_100()", "Shift+V")
        sm.addCommand("Align Vertically Custom", "em_alignnodes.align_selected_nodes_v_c()", "Shift+B")
        sm.addCommand("Align Horizontally", "em_alignnodes.align_selected_nodes_h_100()", "Shift+H")
        sm.addCommand("Align Horizontally Custom", "em_alignnodes.align_selected_nodes_h_c()", "Shift+J")
 
menu_align()