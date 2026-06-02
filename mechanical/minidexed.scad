// 6/1/26 PAW version 1.0  - All fits 
//
// Parameters
cube_x = 160;
cube_y = 40;
cube_z = 2;

opening_x = 73.0-.5;
opening_y = 25.6-.5;

peg_diameter = 6;
peg_height = 5;          
peg_hole_diameter = 2.6; 
peg_spacing_x = 76.5-1.4;
peg_spacing_y = 31.4;

//edge_hole_diameter = 7;   // New 7mm holes
edge_hole_diameter = 8;   // New 7mm holes
edge_hole_offset = 20;    // 20mm from the outer edges

$fn = 60; // Smooths out all round geometry

// Main Assembly
difference() {
    // 1. Solid structure (Base plate + solid pegs)
    union() {
        // Base plate with centered opening
        difference() {
            cube([cube_x, cube_y, cube_z], center = true);
            translate([0,0.5,0])
              cube([opening_x, opening_y, cube_z + 2], center = true);
        }

        // 4 Solid Pegs
        for (x = [ -1, 1 ]) {
            for (y = [ -1, 1 ]) {
                translate([x * (peg_spacing_x / 2), y * (peg_spacing_y / 2), cube_z / 2]) {
                    cylinder(h = peg_height, r = peg_diameter / 2, center = false);
                }
            }
        }
    }

    // 2. Peg Cutouts (Drill holes through the pegs and base)
    for (x = [ -1, 1 ]) {
        for (y = [ -1, 1 ]) {
            translate([x * (peg_spacing_x / 2), y * (peg_spacing_y / 2), -(cube_z / 2) - 1]) {
                cylinder(h = cube_z + peg_height + 2, r = peg_hole_diameter / 2, center = false);
            }
        }
    }

    // 3. New Edge Cutouts (Two 7mm holes along the centerline)
    // Calculated as: (Total Width / 2) - Offset from edge
    hole_x_pos = (cube_x / 2) - edge_hole_offset; 
    
    for (x = [ -1, 1 ]) {
        translate([x * hole_x_pos, 0, -(cube_z / 2) - 1]) {
            cylinder(h = cube_z + 2, r = edge_hole_diameter / 2, center = false);
            if (x == -1) 
               // Pot 
               translate ([7.4, -1.6, 0])
                  cube([1.8, 3.4, 20]); 
            else
               // Encoder knob 
               translate ([-1.4, 5.6, 0])
                  cube([2.6, 1.4, 20]); 
        }
    }
    
}
