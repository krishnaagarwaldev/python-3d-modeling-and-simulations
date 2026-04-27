"""
ULTRA SIMPLE COMPLIANT MECHANISM
Most basic version possible
"""

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.STEPControl import STEPControl_Writer
from OCC.Display.SimpleGui import init_display

# Create basic parts
base = BRepPrimAPI_MakeBox(60, 30, 5).Shape()
arm1 = BRepPrimAPI_MakeBox(40, 5, 3).Shape()
arm2 = BRepPrimAPI_MakeBox(40, 5, 3).Shape()

# Combine everything
gripper = BRepAlgoAPI_Fuse(base, arm1).Shape()
gripper = BRepAlgoAPI_Fuse(gripper, arm2).Shape()

# Save file
writer = STEPControl_Writer()
writer.Transfer(gripper, 0)
writer.Write("ultra_simple_gripper.stp")

# Show 3D
display, start, menu, func = init_display()
display.DisplayShape(gripper, update=True)
print("Simple compliant gripper created!")
start()