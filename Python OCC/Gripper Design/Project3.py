"""
SIMPLE COMPLIANT GRIPPER DESIGN
Easy-to-understand version for beginners
"""

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Trsf
from OCC.Core.STEPControl import STEPControl_Writer
from OCC.Display.SimpleGui import init_display


def create_box(length, width, height, x=0, y=0, z=0):
    """Create a simple box at position (x,y,z)"""
    box = BRepPrimAPI_MakeBox(length, width, height).Shape()

    # Move box to desired position
    if x != 0 or y != 0 or z != 0:
        move = gp_Trsf()
        move.SetTranslation(gp_Vec(x, y, z))
        from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
        box = BRepBuilderAPI_Transform(box, move, False).Shape()

    return box


def create_cylinder(radius, height, x=0, y=0, z=0):
    """Create a simple cylinder"""
    from OCC.Core.gp import gp_Ax2, gp_Dir
    cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), radius, height).Shape()

    # Move cylinder
    if x != 0 or y != 0 or z != 0:
        move = gp_Trsf()
        move.SetTranslation(gp_Vec(x, y, z))
        from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
        cylinder = BRepBuilderAPI_Transform(cylinder, move, False).Shape()

    return cylinder


def design_simple_gripper():
    """Design a very simple compliant gripper"""
    print("Designing Simple Compliant Gripper...")

    # 1. Create base plate
    base = create_box(80, 40, 5)
    print("✓ Created base plate")

    # 2. Create left arm (thin and flexible)
    left_arm = create_box(50, 6, 3, 20, 10, 5)
    print("✓ Created left arm")

    # 3. Create right arm
    right_arm = create_box(50, 6, 3, 20, 24, 5)
    print("✓ Created right arm")

    # 4. Create left jaw
    left_jaw = create_box(15, 8, 3, 70, 10, 5)
    print("✓ Created left jaw")

    # 5. Create right jaw
    right_jaw = create_box(15, 8, 3, 70, 22, 5)
    print("✓ Created right jaw")

    # 6. Combine all parts
    gripper = base
    gripper = BRepAlgoAPI_Fuse(gripper, left_arm).Shape()
    gripper = BRepAlgoAPI_Fuse(gripper, right_arm).Shape()
    gripper = BRepAlgoAPI_Fuse(gripper, left_jaw).Shape()
    gripper = BRepAlgoAPI_Fuse(gripper, right_jaw).Shape()

    print("✓ Combined all parts")
    return gripper


def export_step(shape, filename="simple_gripper.stp"):
    """Export to STEP file"""
    writer = STEPControl_Writer()
    writer.Transfer(shape, 0)  # 0 = AsIs
    writer.Write(filename)
    print(f"✓ Exported to {filename}")


def show_3d(shape):
    """Show 3D model"""
    display, start, add_menu, add_func = init_display()
    display.DisplayShape(shape, update=True)
    print("3D Viewer opened! Close window to continue.")
    start()


def main():
    """Main function"""
    print("=" * 50)
    print("SIMPLE COMPLIANT GRIPPER DESIGN")
    print("=" * 50)

    # Design the gripper
    gripper = design_simple_gripper()

    # Export to file
    export_step(gripper)

    # Show 3D model
    show_3d(gripper)

    print("\n🎉 DESIGN COMPLETED!")
    print("This gripper will bend at the thin arms when force is applied.")
    print("No assembly needed - 3D print as one piece!")


if __name__ == "__main__":
    main()