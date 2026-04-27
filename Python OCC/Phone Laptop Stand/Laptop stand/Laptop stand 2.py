from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_compliant_laptop_stand():
    """
    Create a simple foldable laptop stand with compliant hinges
    """

    # Base platform (where laptop sits)
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 200, 150, 5).Shape()

    # Front support leg
    front_leg = BRepPrimAPI_MakeBox(gp_Pnt(50, 0, 0), 100, 10, 80).Shape()

    # Back support leg
    back_leg = BRepPrimAPI_MakeBox(gp_Pnt(50, 140, 0), 100, 10, 120).Shape()

    # Combine all parts
    stand = BRepAlgoAPI_Fuse(base, front_leg).Shape()
    stand = BRepAlgoAPI_Fuse(stand, back_leg).Shape()

    # Cut slots for compliant hinges (these allow folding)
    # Front hinge slot
    front_hinge = BRepPrimAPI_MakeBox(gp_Pnt(60, 5, -1), 80, 2, 7).Shape()
    stand = BRepAlgoAPI_Cut(stand, front_hinge).Shape()

    # Back hinge slot
    back_hinge = BRepPrimAPI_MakeBox(gp_Pnt(60, 143, -1), 80, 2, 7).Shape()
    stand = BRepAlgoAPI_Cut(stand, back_hinge).Shape()

    # Cut finger holes for easy carrying
    finger_hole1 = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(30, 75, -1), gp_Dir(0, 0, 1)), 15, 7
    ).Shape()
    finger_hole2 = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(170, 75, -1), gp_Dir(0, 0, 1)), 15, 7
    ).Shape()

    stand = BRepAlgoAPI_Cut(stand, finger_hole1).Shape()
    stand = BRepAlgoAPI_Cut(stand, finger_hole2).Shape()

    return stand


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    laptop_stand = create_compliant_laptop_stand()
    display.DisplayShape(laptop_stand, update=True)

    print("COMPLIANT LAPTOP STAND")
    print("=" * 40)
    print("\nFEATURES:")
    print("- Foldable design with living hinges")
    print("- Raised platform for better ergonomics")
    print("- Finger holes for easy carrying")
    print("- One-piece construction")
    print("- No assembly required")

    print("\nHOW IT WORKS:")
    print("1. Thin hinge slots allow the legs to fold flat")
    print("2. Material flexibility provides spring action")
    print("3. Stands up when unfolded, folds for storage")
    print("4. Suitable for 3D printing")

    start_display()


if __name__ == "__main__":
    main()