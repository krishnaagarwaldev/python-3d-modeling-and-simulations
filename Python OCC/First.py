# test_installation.py
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display

print("✅ PythonOCC installed successfully!")

# Initialize display
display, start_display, add_menu, add_function_to_menu = init_display()

# Create a simple box
box = BRepPrimAPI_MakeBox(10, 10, 10).Shape()
display.DisplayShape(box, update=True)
print("✅ Basic 3D display working!")

start_display()