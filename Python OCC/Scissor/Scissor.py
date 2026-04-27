from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display


def create_simple_compliant_scissor():
    """
    Create the simplest possible compliant scissor
    Only uses boxes and Boolean operations
    """

    # Create main body (one big rectangle)
    body = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 60, 30, 3).Shape()

    # Cut slot to separate the two handles
    handle_slot = BRepPrimAPI_MakeBox(gp_Pnt(25, 0, -1), 4, 15, 5).Shape()
    body = BRepAlgoAPI_Cut(body, handle_slot).Shape()

    # Cut flexure slots to create bending points
    flex_slot1 = BRepPrimAPI_MakeBox(gp_Pnt(20, 15, -1), 10, 2, 5).Shape()
    flex_slot2 = BRepPrimAPI_MakeBox(gp_Pnt(20, 18, -1), 10, 2, 5).Shape()

    body = BRepAlgoAPI_Cut(body, flex_slot1).Shape()
    body = BRepAlgoAPI_Cut(body, flex_slot2).Shape()

    # Cut V-shape at the end to create jaws
    v_cut = BRepPrimAPI_MakeBox(gp_Pnt(15, 25, -1), 20, 10, 5).Shape()
    body = BRepAlgoAPI_Cut(body, v_cut).Shape()

    return body


# Create and display
display, start_display, add_menu, add_function_to_menu = init_display()
scissor = create_simple_compliant_scissor()
display.DisplayShape(scissor, update=True)

print("SIMPLE COMPLIANT SCISSOR CREATED!")
print("\nDESIGN BREAKDOWN:")
print("1. Single piece of material")
print("2. Handle slot separates left and right handles")
print("3. Flexure slots create bending points")
print("4. V-cut forms the gripping jaws")
print("\nACTION: Squeeze the bottom handles → top jaws close together")

start_display()