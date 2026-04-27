# 3_boolean_operations.py
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut, BRepAlgoAPI_Common
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Vec, gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Display.SimpleGui import init_display


def demonstrate_booleans():
    """Show UNION, SUBTRACTION, and INTERSECTION operations"""

    # Create two overlapping objects
    box1 = BRepPrimAPI_MakeBox(30, 30, 15).Shape()

    # Position box2 to overlap with box1
    transform = gp_Trsf()
    transform.SetTranslation(gp_Vec(15, 15, 0))
    box2 = BRepBuilderAPI_Transform(
        BRepPrimAPI_MakeBox(30, 30, 15).Shape(),
        transform
    ).Shape()

    shapes = []
    shapes.append(("Box 1", box1))
    shapes.append(("Box 2", box2))

    # 1. UNION (FUSE) - Combine both shapes
    print("🔗 Performing UNION operation...")
    fused = BRepAlgoAPI_Fuse(box1, box2)
    if fused.IsDone():
        union_shape = fused.Shape()
        shapes.append(("Union Result", union_shape))
        print("✅ Union completed: Two boxes merged")

    # 2. SUBTRACTION (CUT) - Remove one shape from another
    print("✂️ Performing SUBTRACTION operation...")

    # Create a cylinder to subtract
    cylinder = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(25, 25, 0), gp_Dir(0, 0, 1)),
        8, 25
    ).Shape()

    subtracted = BRepAlgoAPI_Cut(box1, cylinder)
    if subtracted.IsDone():
        cut_shape = subtracted.Shape()
        shapes.append(("Subtraction Result", cut_shape))
        print("✅ Subtraction completed: Hole drilled in box")

    # 3. INTERSECTION (COMMON) - Keep only overlapping part
    print("🔍 Performing INTERSECTION operation...")
    common = BRepAlgoAPI_Common(box1, box2)
    if common.IsDone():
        common_shape = common.Shape()
        shapes.append(("Intersection Result", common_shape))
        print("✅ Intersection completed: Only overlap kept")

    return shapes


# Display boolean operations
display, start_display, add_menu, add_function_to_menu = init_display()
shapes = demonstrate_booleans()

# Display with different colors
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
for i, (name, shape) in enumerate(shapes):
    display.DisplayShape(shape, color=colors[i % len(colors)], update=False)
    print(f"📊 Displaying: {name}")

display.FitAll()
start_display()