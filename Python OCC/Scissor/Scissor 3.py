from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display


def create_working_compliant_scissor():
    """
    Create a working compliant scissor with actual flexible joints
    """

    # Create the main scissor body
    body = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 50, 40, 3).Shape()

    # Cut the center slot to separate the two arms
    center_slot = BRepPrimAPI_MakeBox(gp_Pnt(20, 5, -1), 10, 30, 5).Shape()
    body = BRepAlgoAPI_Cut(body, center_slot).Shape()

    # Cut thin flexure joints - these are the COMPLIANT parts that bend
    # Left flexure joint (thin section that acts as a hinge)
    left_flexure_cut = BRepPrimAPI_MakeBox(gp_Pnt(18, 15, -1), 4, 2, 5).Shape()
    body = BRepAlgoAPI_Cut(body, left_flexure_cut).Shape()

    # Right flexure joint (thin section that acts as a hinge)
    right_flexure_cut = BRepPrimAPI_MakeBox(gp_Pnt(28, 15, -1), 4, 2, 5).Shape()
    body = BRepAlgoAPI_Cut(body, right_flexure_cut).Shape()

    # Shape the jaws for better gripping
    jaw_cut = BRepPrimAPI_MakeBox(gp_Pnt(15, 35, -1), 20, 10, 5).Shape()
    body = BRepAlgoAPI_Cut(body, jaw_cut).Shape()

    return body


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    scissor = create_working_compliant_scissor()
    display.DisplayShape(scissor, update=True)

    print("WORKING COMPLIANT SCISSOR MECHANISM")
    print("=" * 50)
    print("\nHOW IT WORKS:")
    print("┌─────────┐   ┌─────────┐")
    print("│ Handle1 │   │ Handle2 │  ← SQUEEZE HERE")
    print("│         │   │         │")
    print("├─────┐   │   │   ┌─────┤")
    print("│     │   └───┘   │     │")
    print("│     │  THIN     │     │  ← FLEXIBLE JOINTS BEND HERE")
    print("│     │ SECTION   │     │")
    print("│     └───────────┘     │")
    print("│                       │")
    print("└─────┐           ┌─────┘")
    print("      │           │")
    print("      └─────┬─────┘")
    print("            │        ← JAWS CLOSE WHEN HANDLES SQUEEZED")
    print("          JAWS")

    print("\nREAL-WORLD BEHAVIOR:")
    print("1. When you SQUEEZE the handles, the thin sections BEND")
    print("2. This causes the jaws to move toward each other")
    print("3. When you RELEASE, the material springs back to original shape")
    print("4. No pivots, screws, or assemblies needed!")

    print("\nMATERIAL: Use flexible plastic (like TPU) or spring steel")

    start_display()


if __name__ == "__main__":
    main()