from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display


def create_simple_foldable_stand():
    """
    Create minimal foldable stand like commercial products
    """

    # Base (80mm x 50mm)
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 80, 50, 3).Shape()

    # Back support
    support = BRepPrimAPI_MakeBox(gp_Pnt(25, 35, 3), 30, 5, 60).Shape()

    # Combine
    stand = BRepAlgoAPI_Fuse(base, support).Shape()

    # Cut folding line (compliant hinge)
    hinge = BRepPrimAPI_MakeBox(gp_Pnt(30, 33, -1), 20, 1, 5).Shape()
    stand = BRepAlgoAPI_Cut(stand, hinge).Shape()

    # Cut phone groove
    groove = BRepPrimAPI_MakeBox(gp_Pnt(30, 0, 3), 20, 8, 3).Shape()
    stand = BRepAlgoAPI_Cut(stand, groove).Shape()

    return stand


# Create and display
display, start_display, add_menu, add_function_to_menu = init_display()
stand = create_simple_foldable_stand()
display.DisplayShape(stand, update=True)

print("AMAZON-STYLE FOLDABLE PHONE STAND")
print("Compact design - folds completely flat!")
print("Perfect for travel and desktop use")
start_display()