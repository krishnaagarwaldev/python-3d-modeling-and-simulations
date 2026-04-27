from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display

from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static
from OCC.Core.IFSelect import IFSelect_RetDone

def create_foldable_phone_stand():

    #Main base
    base = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 80, 60, 3).Shape()

    # Back support (foldable part)
    back_support = BRepPrimAPI_MakeBox(gp_Pnt(20, 45, 3), 40, 5, 80).Shape()

    # Phone rest at bottom
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


def export_to_step(shape, filename):
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP203")

    step_writer.Transfer(shape, STEPControl_AsIs)
    status = step_writer.Write(filename)

    if status == IFSelect_RetDone:
        print(f"✓ Successfully exported to {filename}")
        return True
    else:
        print(f"Failed to export to {filename}")
        return False


def main():
    display, start_display, add_menu, add_function_to_menu = init_display()

    phone_stand = create_foldable_phone_stand()
    display.DisplayShape(phone_stand, update=True)

    export_to_step(phone_stand, "CAD_Phone_stand.stp")

    print("FOLDABLE PHONE STAND")
    print("\n\nFEATURES:")
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



"""
124ad0026 - Krishna Agarwal 

Smart Manufacturing - Compliant Design Report :-
What This Compliant Mechanism Is Useful For
This phone stand is a compliant mechanism that serves several practical purposes:

Primary Function:
Phone/Tablet Stand: Holds your smartphone at an optimal viewing angle for hands-free use
Foldable Design: Can be folded flat for easy storage and portability

Key Applications:
Desktop Viewing: Watch videos, make video calls, or follow recipes while cooking
Workstation Aid: Keep your phone upright for notifications during work
Travel Companion: Lightweight and compact for carrying in bags
Bedside Stand: Use as a nightstand phone holder
Presentation Tool: Display content during meetings or demonstrations

Advantages:
No Assembly Required: One-piece design means no loose parts
Durable: No hinges or joints that can wear out over time
Cost-Effective: Simple manufacturing, often 3D printable
Reliable: Fewer failure points than traditional mechanisms
"""