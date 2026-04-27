from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Trsf, gp_Ax1
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Display.SimpleGui import init_display
import math


def create_compliant_scissor():
    """
    Create a simple compliant scissor mechanism
    Uses a central flexure joint instead of traditional pivot
    """

    # Create left handle (30mm long, 8mm wide, 3mm thick)
    left_handle = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 30, 8, 3).Shape()

    # Create right handle (starts from center)
    right_handle = BRepPrimAPI_MakeBox(gp_Pnt(2, 0, 0), 30, 8, 3).Shape()

    # Create central flexure joint - thin section that bends
    flexure = BRepPrimAPI_MakeBox(gp_Pnt(-1, 8, 0), 4, 10, 3).Shape()

    # Create left jaw (simple straight jaw)
    left_jaw = BRepPrimAPI_MakeBox(gp_Pnt(0, 18, 0), 25, 6, 3).Shape()

    # Create right jaw (simple straight jaw)
    right_jaw = BRepPrimAPI_MakeBox(gp_Pnt(2, 18, 0), 25, 6, 3).Shape()

    # Combine all parts
    scissor = BRepAlgoAPI_Fuse(left_handle, right_handle).Shape()
    scissor = BRepAlgoAPI_Fuse(scissor, flexure).Shape()
    scissor = BRepAlgoAPI_Fuse(scissor, left_jaw).Shape()
    scissor = BRepAlgoAPI_Fuse(scissor, right_jaw).Shape()

    # Cut slots in flexure to make it more flexible
    slot1 = BRepPrimAPI_MakeBox(gp_Pnt(-1, 10, -1), 4, 2, 5).Shape()
    slot2 = BRepPrimAPI_MakeBox(gp_Pnt(-1, 13, -1), 4, 2, 5).Shape()

    scissor = BRepAlgoAPI_Cut(scissor, slot1).Shape()
    scissor = BRepAlgoAPI_Cut(scissor, slot2).Shape()

    # Cut triangle shape between jaws to create scissor effect
    triangle_cut = BRepPrimAPI_MakeBox(gp_Pnt(1, 18, -1), 2, 10, 5).Shape()
    scissor = BRepAlgoAPI_Cut(scissor, triangle_cut).Shape()

    return scissor


def main():
    """
    Main function to create and display the compliant scissor
    """
    print("Creating Compliant Scissor Mechanism")
    print("=" * 40)

    # Create the scissor
    scissor = create_compliant_scissor()

    # Display it
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(scissor, update=True)

    print("\nDESIGN EXPLANATION:")
    print("1. CENTRAL FLEXURE: The thin section with slots acts as a spring")
    print("2. OPERATION: Squeeze handles → flexure bends → jaws move together")
    print("3. RETURN: Release handles → flexure springs back → jaws open")
    print("4. USES: Picking small objects, laboratory tools, robotic grippers")

    print("\nHOW IT WORKS VISUALLY:")
    print("      [HANDLE 1]    [HANDLE 2]")
    print("           |            |")
    print("           |    FLEX    |   ← Flexible joint with slots")
    print("           |    JOINT   |")
    print("           |            |")
    print("        [JAW 1]      [JAW 2]")
    print("\nSqueeze handles → jaws close for gripping!")

    start_display()


if __name__ == "__main__":
    main()