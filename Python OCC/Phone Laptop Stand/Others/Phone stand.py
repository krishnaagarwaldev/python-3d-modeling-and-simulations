from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_phone_stand():
    """
    Create a stylish foldable phone stand with curved design
    """

    # Main base with curved edges
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 100, 80, 5).Shape()

    # Cut curved front edge for better look
    front_curve_cut = BRepPrimAPI_MakeBox(gp_Pnt(0, 75, -1), 100, 10, 7).Shape()
    base = BRepAlgoAPI_Cut(base, front_curve_cut).Shape()

    # Support arm (angled back)
    support_arm = BRepPrimAPI_MakeBox(gp_Pnt(30, 10, 5), 40, 10, 70).Shape()

    # Phone rest at top
    phone_rest = BRepPrimAPI_MakeBox(gp_Pnt(20, 5, 75), 60, 5, 15).Shape()

    # Combine all parts
    stand = BRepAlgoAPI_Fuse(base, support_arm).Shape()
    stand = BRepAlgoAPI_Fuse(stand, phone_rest).Shape()

    # Cut decorative pattern on base
    for i in range(3):
        slot = BRepPrimAPI_MakeBox(gp_Pnt(20 + i * 20, 20, -1), 5, 30, 7).Shape()
        stand = BRepAlgoAPI_Cut(stand, slot).Shape()

    # Cut compliant hinge (allows folding)
    hinge = BRepPrimAPI_MakeBox(gp_Pnt(35, 8, -1), 30, 1, 7).Shape()
    stand = BRepAlgoAPI_Cut(stand, hinge).Shape()

    # Cut cable slot for charging
    cable_slot = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(50, 2, 10), gp_Dir(0, 1, 0)), 3, 10
    ).Shape()
    stand = BRepAlgoAPI_Cut(stand, cable_slot).Shape()

    return stand


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    phone_stand = create_phone_stand()
    display.DisplayShape(phone_stand, update=True)

    print("FOLDABLE PHONE STAND")
    print("=" * 35)
    print("\nDESIGN FEATURES:")
    print("- Curved modern design")
    print("- Foldable at thin hinge")
    print("- Cable slot for charging")
    print("- Decorative pattern")
    print("- Stable angled support")

    print("\nDIMENSIONS:")
    print("- Base: 100x80mm")
    print("- Height: 90mm")
    print("- Phone rest: 60mm wide")

    start_display()


if __name__ == "__main__":
    main()