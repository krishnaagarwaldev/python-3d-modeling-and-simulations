from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_laptop_stand():
    """
    Create a simple foldable laptop stand
    """

    # Main platform (where laptop sits)
    platform = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 250, 180, 5).Shape()

    # Front support leg
    front_leg = BRepPrimAPI_MakeBox(gp_Pnt(75, 0, 5), 100, 15, 40).Shape()

    # Back support leg (taller for tilt)
    back_leg = BRepPrimAPI_MakeBox(gp_Pnt(75, 165, 5), 100, 15, 80).Shape()

    # Combine all parts
    stand = BRepAlgoAPI_Fuse(platform, front_leg).Shape()
    stand = BRepAlgoAPI_Fuse(stand, back_leg).Shape()

    # Cut folding hinges
    front_hinge = BRepPrimAPI_MakeBox(gp_Pnt(80, 12, -1), 90, 2, 7).Shape()
    back_hinge = BRepPrimAPI_MakeBox(gp_Pnt(80, 163, -1), 90, 2, 7).Shape()

    stand = BRepAlgoAPI_Cut(stand, front_hinge).Shape()
    stand = BRepAlgoAPI_Cut(stand, back_hinge).Shape()

    # Cut ventilation holes for laptop cooling
    for i in range(5):
        for j in range(3):
            hole = BRepPrimAPI_MakeCylinder(
                gp_Ax2(gp_Pnt(40 + i * 35, 40 + j * 35, -1), gp_Dir(0, 0, 1)),
                8, 7
            ).Shape()
            stand = BRepAlgoAPI_Cut(stand, hole).Shape()

    # Cut finger grips for carrying
    grip1 = BRepPrimAPI_MakeBox(gp_Pnt(100, 170, -1), 50, 15, 7).Shape()
    grip2 = BRepPrimAPI_MakeBox(gp_Pnt(100, 0, -1), 50, 15, 7).Shape()

    stand = BRepAlgoAPI_Cut(stand, grip1).Shape()
    stand = BRepAlgoAPI_Cut(stand, grip2).Shape()

    return stand


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    laptop_stand = create_laptop_stand()
    display.DisplayShape(laptop_stand, update=True)

    print("FOLDABLE LAPTOP STAND")
    print("=" * 40)
    print("\nDESIGN FEATURES:")
    print("- Ergonomic tilt (80mm back, 40mm front)")
    print("- Ventilation holes for cooling")
    print("- Foldable for easy storage")
    print("- Finger grips for carrying")
    print("- Stable wide base")

    print("\nSPECIFICATIONS:")
    print("- Platform: 250mm x 180mm")
    print("- Height: 80mm at back, 40mm at front")
    print("- Material: 3D printable plastic")

    start_display()


if __name__ == "__main__":
    main()