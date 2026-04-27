import cadquery as cq


def create_compliant_gripper():
    """Create an adaptive parallel gripper with compliant flexures"""

    # Base parameters
    base_width = 60
    base_height = 40
    base_thickness = 8
    flexure_thickness = 1.5
    jaw_length = 25
    jaw_width = 15

    # Create base plate
    base = (cq.Workplane("XY")
            .box(base_width, base_height, base_thickness)
            .edges("|Z").fillet(2.0))

    # Create central mounting hole
    base = (base.faces(">Z")
            .workplane()
            .hole(6, depth=base_thickness / 2))

    # Create compliant flexure arms
    flexure_length = 20
    flexure_width = 4

    # Left flexure system
    left_flexure = (cq.Workplane("XY")
                    .workplane(offset=base_thickness / 2)
                    .transformed(offset=(-base_width / 4, 0, 0))
                    .rect(flexure_width, flexure_length)
                    .extrude(flexure_thickness)
                    .edges("|Z").fillet(0.5))

    # Right flexure system (mirror of left)
    right_flexure = (cq.Workplane("XY")
                     .workplane(offset=base_thickness / 2)
                     .transformed(offset=(base_width / 4, 0, 0))
                     .rect(flexure_width, flexure_length)
                     .extrude(flexure_thickness)
                     .edges("|Z").fillet(0.5))

    # Create gripper jaws
    jaw_thickness = 3

    # Left jaw
    left_jaw = (cq.Workplane("XY")
                .workplane(offset=base_thickness / 2 + flexure_thickness)
                .transformed(offset=(-base_width / 4, flexure_length / 2, 0))
                .box(jaw_width, jaw_length, jaw_thickness)
                .edges("|Z").fillet(1.0))

    # Add living hinge connection
    left_hinge = (cq.Workplane("XY")
                  .workplane(offset=base_thickness / 2 + flexure_thickness)
                  .transformed(offset=(-base_width / 4, flexure_length / 2 - jaw_length / 4, 0))
                  .rect(jaw_width / 3, 1.0)
                  .extrude(jaw_thickness)
                  .edges("|Z").fillet(0.3))

    left_jaw = left_jaw.union(left_hinge)

    # Right jaw with living hinge (mirror)
    right_jaw = (cq.Workplane("XY")
                 .workplane(offset=base_thickness / 2 + flexure_thickness)
                 .transformed(offset=(base_width / 4, flexure_length / 2, 0))
                 .box(jaw_width, jaw_length, jaw_thickness)
                 .edges("|Z").fillet(1.0))

    right_hinge = (cq.Workplane("XY")
                   .workplane(offset=base_thickness / 2 + flexure_thickness)
                   .transformed(offset=(base_width / 4, flexure_length / 2 - jaw_length / 4, 0))
                   .rect(jaw_width / 3, 1.0)
                   .extrude(jaw_thickness)
                   .edges("|Z").fillet(0.3))

    right_jaw = right_jaw.union(right_hinge)

    # Add gripper finger pads with texture
    pad_width = 8
    pad_height = 12

    left_pad = (cq.Workplane("XY")
                .workplane(offset=base_thickness / 2 + flexure_thickness + jaw_thickness / 2)
                .transformed(offset=(-base_width / 4, flexure_length / 2 + jaw_length / 2 - pad_height / 2, 0))
                .box(pad_width, pad_height, 2)
                .faces(">Z").workplane()
                .rarray(1.5, 1.5, 4, 6)
                .circle(0.3)
                .cutThruAll())

    right_pad = (cq.Workplane("XY")
                 .workplane(offset=base_thickness / 2 + flexure_thickness + jaw_thickness / 2)
                 .transformed(offset=(base_width / 4, flexure_length / 2 + jaw_length / 2 - pad_height / 2, 0))
                 .box(pad_width, pad_height, 2)
                 .faces(">Z").workplane()
                 .rarray(1.5, 1.5, 4, 6)
                 .circle(0.3)
                 .cutThruAll())

    # Combine all parts
    gripper = (base
               .union(left_flexure)
               .union(right_flexure)
               .union(left_jaw)
               .union(right_jaw)
               .union(left_pad)
               .union(right_pad))

    return gripper


def create_actuation_mechanism():
    """Create actuation mechanism for the gripper"""

    # Actuator mount
    actuator = (cq.Workplane("XY")
                .box(15, 10, 6)
                .faces(">Z").workplane()
                .hole(4, depth=3)
                .edges("|Z").fillet(1.0))

    # Push rod
    push_rod = (cq.Workplane("XY")
                .workplane(offset=3)
                .circle(1.5)
                .extrude(25))

    # Connection plate
    connector = (cq.Workplane("XY")
                 .workplane(offset=28)
                 .box(20, 5, 2)
                 .edges("|Z").fillet(0.5))

    actuation_mechanism = actuator.union(push_rod).union(connector)

    return actuation_mechanism


# Create the complete assembly
print("Creating compliant gripper...")
compliant_gripper = create_compliant_gripper()
print("Creating actuation mechanism...")
actuation_system = create_actuation_mechanism()

# Position actuation system relative to gripper
actuation_system = actuation_system.translate((0, -15, 4))

# Combine everything
final_assembly = compliant_gripper.union(actuation_system)

# Export to STEP file - CORRECTED EXPORT METHODS
print("Exporting to CAD.stp...")

# Method 1: Use STEP exporter explicitly
cq.exporters.export(final_assembly, "CAD.step", "STEP")

# Method 2: Or use the alias .stp with explicit type
cq.exporters.export(final_assembly, "CAD.stp", "STEP")

print("Export completed successfully!")

# Optional: Also export as STL for 3D printing visualization
cq.exporters.export(final_assembly, "CAD.stl", "STL")
print("STL export completed!")