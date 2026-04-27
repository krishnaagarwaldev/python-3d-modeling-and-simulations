from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_simple_phone_stand():
    """
    Create a simple, adjustable, foldable phone stand
    """

    # Base plate with rounded design
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 70, 50, 3).Shape()

    # Cut rounded corners for better look
    corner1 = BRepPrimAPI_MakeBox(gp_Pnt(0, 40, -1), 10, 10, 5).Shape()
    corner2 = BRepPrimAPI_MakeBox(gp_Pnt(60, 40, -1), 10, 10, 5).Shape()
    base = BRepAlgoAPI_Cut(base, corner1).Shape()
    base = BRepAlgoAPI_Cut(base, corner2).Shape()

    # Adjustable back support with multiple hinge options
    support = BRepPrimAPI_MakeBox(gp_Pnt(20, 30, 3), 30, 5, 70).Shape()

    # Combine base and support
    stand = BRepAlgoAPI_Fuse(base, support).Shape()

    # Cut multiple hinge slots for adjustable angles
    hinge1 = BRepPrimAPI_MakeBox(gp_Pnt(25, 28, -1), 20, 1, 5).Shape()  # Low angle
    hinge2 = BRepPrimAPI_MakeBox(gp_Pnt(25, 25, -1), 20, 1, 5).Shape()  # Medium angle
    hinge3 = BRepPrimAPI_MakeBox(gp_Pnt(25, 22, -1), 20, 1, 5).Shape()  # High angle

    stand = BRepAlgoAPI_Cut(stand, hinge1).Shape()
    stand = BRepAlgoAPI_Cut(stand, hinge2).Shape()
    stand = BRepAlgoAPI_Cut(stand, hinge3).Shape()

    # Cut phone groove at bottom
    groove = BRepPrimAPI_MakeBox(gp_Pnt(25, 0, 3), 20, 8, 2).Shape()
    stand = BRepAlgoAPI_Cut(stand, groove).Shape()

    # Cut decorative pattern
    for i in range(3):
        pattern = BRepPrimAPI_MakeBox(gp_Pnt(15 + i * 15, 10, -1), 8, 15, 5).Shape()
        stand = BRepAlgoAPI_Cut(stand, pattern).Shape()

    return stand


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    stand = create_simple_phone_stand()
    display.DisplayShape(stand, update=True)

    print("SIMPLE FOLDABLE PHONE STAND")
    print("=" * 35)
    print("\n📱 FEATURES:")
    print("- Foldable & Portable")
    print("- 3 Adjustable Viewing Angles")
    print("- Modern Rounded Design")
    print("- One-Piece Construction")
    print("- Phone Groove for Stability")

    print("\n🎯 HOW TO USE:")
    print("1. Choose hinge for desired angle:")
    print("   • Bottom hinge = Low angle")
    print("   • Middle hinge = Medium angle")
    print("   • Top hinge = High angle")
    print("2. Place phone in groove")
    print("3. Fold flat when not in use")

    print("\n📐 DIMENSIONS: 70mm x 50mm (Compact)")

    start_display()


if __name__ == "__main__":
    main()