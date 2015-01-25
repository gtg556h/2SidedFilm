importClass(Packages.ij.IJ);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);


// View fields:
// s=""; for (a in imp) {s += " " + a; }
// for (a in gd) {
//    IJ.log(a);
// }


// To run PIV (different versions!!!):
// run("iterative PIV(Advanced)..."," piv1=128 sw1=256 vs1=64 piv2=64 sw2=128 vs2=32 piv3=50 sw3=100 vs3=50 correlation=0.6 batch path=[/Users/brian/directory/] ");

// IJ.run(imp, "iterative PIV(Cross-Correlation)...", "piv1=128 piv2=64 piv3=0 what=[Accept this PIV and output] noise=0.20 threshold=5 c1=3 c2=1 save=D:\20110819b\out\segmented_89.tif.txt batch");

// Use "save" instead of "path" if writing javascript!!!!

// piv1, sw1, vs1 are interrogation window, search window, and vector spacing for 1st pass...
// correlation is threshold value of the correlation peak
// batch specifies the batch mode
// path is the location that results will be saved


// To use output data:
// x |   y  |  ux1  |  uy1  |  mag1  |  ang1  |  p1  |  ux2  |  uy2  |  mag2  |  ang2  |  p2  |  ux0  |  uy0  |  mag0  |  flag

// (x,y) is the position of the vector (center of the interrogation window).
// ux1, uy1 are the x and y component of the vector (displacement) obtained from the 1st correlation peak.
// mag1 is the magnitude (norm) of the vector.
// ang1, is the angle between the current vector and the vector interpolated from previous PIV iteration.
// p1 is the correlation value of the 1st peak.
// ux2,uy2,mag2,ang2,p2 are the values for the vector obtained from the 2nd correlation peak.
// ux0, uy0, mag0 are the vector value at (x,y) interpolated from previous PIV iteration.
// flag is a column used for mark whether this vector value is interpolated (marked as 999) or switched between 1st and 2nd peak (marked as 21), or invalid (-1).

// Only the first 5 columns are used for vector plot. 

imp = IJ.getImage();
//var i0 = imp.getID();
i0 = WindowManager.getCurrentWindow();
IJ.log(i0);


 
IJ.run("StackReg", "transformation=[Rigid Body]");

