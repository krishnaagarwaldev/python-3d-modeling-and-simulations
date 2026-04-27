# 1_basic_shapes.py
from OCC.Core.BRepPrimAPI import (
    BRepPrimAPI_MakeBox,
    BRepPrimAPI_MakeCylinder,
    BRepPrimAPI_MakeSphere,
    BRepPrimAPI_MakeCone
)
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display


def create_all_primitives():
    """Create all basic primitive shapes"""

    # 1. BOX - Most common primitive
    # Parameters: width (X), depth (Y), height (Z)
    box = BRepPrimAPI_MakeBox(30, 20, 10).Shape()
    print("📦 Box created: 30x20x10mm")

    # 2. CYLINDER - Need axis definition
    # gp_Ax2(center_point, direction)
    cylinder_axis = gp_Ax2(gp_Pnt(50, 0, 0), gp_Dir(0, 0, 1))
    cylinder = BRepPrimAPI_MakeCylinder(cylinder_axis, 15, 25).Shape()
    print("🛢️ Cylinder created: radius=15mm, height=25mm")

    # 3. SPHERE - Center point + radius
    sphere = BRepPrimAPI_MakeSphere(gp_Pnt(100, 0, 0), 20).Shape()
    print("🔮 Sphere created: radius=20mm")

    # 4. CONE - Axis + two radii + height
    cone_axis = gp_Ax2(gp_Pnt(150, 0, 0), gp_Dir(0, 0, 1))
    cone = BRepPrimAPI_MakeCone(cone_axis, 10, 5, 25).Shape()
    print("🎯 Cone created: bottom_radius=10mm, top_radius=5mm, height=25mm")

    return [box, cylinder, sphere, cone]


# Display all shapes
display, start_display, add_menu, add_function_to_menu = init_display()
shapes = create_all_primitives()

colors = ['red', 'blue', 'green', 'yellow']
for i, shape in enumerate(shapes):
    display.DisplayShape(shape, color=colors[i], update=False)

display.FitAll()
start_display()