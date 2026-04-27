from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_foldable_phone_stand():
    """
    Create a simple foldable phone stand like the Amazon product
    """

    # Main base plate
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 80, 60, 3).Shape()

    # Back support (foldable part)
    back_support = BRepPrimAPI_MakeBox(gp_Pnt(20, 45, 3), 40, 5, 80).Shape()

    # Phone rest ledge at bottom
    phone_ledge = BRepPrimAPI_MakeBox(gp_Pnt(15, 0, 3), 50, 10, 5).Shape()

    # Combine all parts
    stand = BRepAlgoAPI_Fuse(base, back_support).Shape()
    stand = BRepAlgoAPI_Fuse(stand, phone_ledge).Shape()

    # Cut the folding hinge (thin section that bends)
    hinge = BRepPrimAPI_MakeBox(gp_Pnt(25, 43, -1), 30, 1, 5).Shape()
    stand = BRepAlgoAPI_Cut(stand, hinge).Shape()

    # Cut slot for phone stability
    phone_slot = BRepPrimAPI_MakeBox(gp_Pnt(30, 0, 8), 20, 15, 5).Shape()
    stand = BRepAlgoAPI_Cut(stand, phone_slot).Shape()

    # Cut finger grip holes
    hole1 = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(20, 30, -1), gp_Dir(0, 0, 1)), 8, 5
    ).Shape()
    hole2 = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(60, 30, -1), gp_Dir(0, 0, 1)), 8, 5
    ).Shape()

    stand = BRepAlgoAPI_Cut(stand, hole1).Shape()
    stand = BRepAlgoAPI_Cut(stand, hole2).Shape()

    # Round the corners for better look
    corner1 = BRepPrimAPI_MakeBox(gp_Pnt(0, 55, -1), 10, 10, 5).Shape()
    corner2 = BRepPrimAPI_MakeBox(gp_Pnt(70, 55, -1), 10, 10, 5).Shape()
    stand = BRepAlgoAPI_Cut(stand, corner1).Shape()
    stand = BRepAlgoAPI_Cut(stand, corner2).Shape()

    return stand


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    phone_stand = create_foldable_phone_stand()
    display.DisplayShape(phone_stand, update=True)

    print("FOLDABLE PHONE STAND")
    print("=" * 40)
    print("\nDESIGN (Similar to Amazon Product):")
    print("┌─────────────────┐")
    print("│                 │ ← Back Support (Folds here)")
    print("│    📱 PHONE     │")
    print("│                 │")
    print("├─────────────────┤ ← Phone Slot")
    print("│      BASE       │ ← Foldable hinge at back")
    print("└─────────────────┘")

    print("\nFEATURES:")
    print("- Foldable design (stores flat)")
    print("- Phone slot for stability")
    print("- Finger holes for easy carrying")
    print("- Rounded corners for safety")
    print("- One-piece 3D printable")

    print("\nHOW TO USE:")
    print("1. Fold back support upright")
    print("2. Place phone in the slot")
    print("3. Phone leans against support")
    print("4. Fold flat when not in use")

    start_display()


if __name__ == "__main__":
    main()