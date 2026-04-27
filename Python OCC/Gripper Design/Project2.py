from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Display.SimpleGui import init_display

# ✅ Step 1: Create main cylindrical body
body = BRepPrimAPI_MakeCylinder(20, 50).Shape()   # radius=20mm, height=50mm

# ✅ Step 2: Create a conical cleaning head
head = BRepPrimAPI_MakeCone(20, 5, 15).Shape()   # top radius=5mm, bottom=20mm, height=15mm

# ✅ Step 3: Fuse both (combine)
tool = BRepAlgoAPI_Fuse(body, head).Shape()

# ✅ Step 4: Add fillets (rounded corners)
fillet = BRepFilletAPI_MakeFillet(tool)

# Explore edges (no topods_Edge used)
edge_explorer = TopExp_Explorer(tool, TopAbs_EDGE)
while edge_explorer.More():
    edge = edge_explorer.Current()  # Directly use the edge handle
    fillet.Add(1.5, edge)  # 1.5mm radius
    edge_explorer.Next()

# Get final smooth shape
smooth_tool = fillet.Shape()

# ✅ Step 5: Display model
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(smooth_tool, update=True)
display.FitAll()
start_display()
