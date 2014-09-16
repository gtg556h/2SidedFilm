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

// Original Values:
//gd = new GenericDialog("Options");
//gd.addMessage("PIV Parameters");
//gd.addNumericField("Side (1,2)", 0, 0);
//gd.addNumericField("Interrogation window 1", 128, 0);
//gd.addNumericField("search window 1", 256, 0);
//gd.addNumericField("vector spacing 1", 64, 0);
//gd.addNumericField("Interrogation window 2", 64, 0);
//gd.addNumericField("search window 2", 128, 0);
//gd.addNumericField("vector spacing 2", 32, 0);
//gd.addNumericField("Interrogation window 3", 48, 0);
//gd.addNumericField("search window 3", 96, 0);
//gd.addNumericField("vector spacing 3", 24, 0);
//gd.addNumericField("correlation threshold", 0.8, 2);

gd = new GenericDialog("Options");
gd.addMessage("PIV Parameters");
gd.addNumericField("Side (1,2)", 0, 0);
gd.addNumericField("Interrogation window 1", 64, 0);
gd.addNumericField("search window 1", 128, 0);
gd.addNumericField("vector spacing 1", 32, 0);
gd.addNumericField("Interrogation window 2", 32, 0);
gd.addNumericField("search window 2", 64, 0);
gd.addNumericField("vector spacing 2", 16, 0);
gd.addNumericField("Interrogation window 3", 24, 0);
gd.addNumericField("search window 3", 48, 0);
gd.addNumericField("vector spacing 3", 12, 0);
gd.addNumericField("correlation threshold", 0.8, 2);


gd.showDialog();

//if (gd.wasCancelled()) {
//    return;
//}

var side = gd.getNextNumber();
var piv1 = gd.getNextNumber();
var sw1 = gd.getNextNumber();
var vs1 = gd.getNextNumber();
var piv2 = gd.getNextNumber();
var sw2 = gd.getNextNumber();
var vs2 = gd.getNextNumber();
var piv3 = gd.getNextNumber();
var sw3 = gd.getNextNumber();
var vs3 = gd.getNextNumber();
var corr = gd.getNextNumber();


// Temp mute:
// imp.createNewRoi();
// imp.getROI();

//var path = IJ.getDirectory("Select a folder to save PIV results");
path = ["/Users/brian/working/"]


var stackSize = imp.getImageStackSize();
IJ.log("Slices: " + stackSize);

changes = false;
//setBatchMode(true);
for(s=1;s<stackSize;s++){
	var ss = s + 1;
	// Incorporate ROI selection in next step
	IJ.run("Duplicate...", "title=[seq_"+s+"_"+side+"] duplicate range="+s+"-"+ss+"");
	IJ.log("s = " + s);
	IJ.log("s+1 = " + ss);
    IJ.run("iterative PIV(Advanced)...", " piv1="+piv1+" sw1="+sw1+" vs1="+vs1+" piv2="+piv2+" sw2="+sw2+" vs2="+vs2+" piv3="+piv3+" sw3="+sw3+" vs3="+vs3+" correlation="+corr+" batch path=["+path+"]");
    while(imp2 = WindowManager.getImage(WindowManager.getNthImageID(2))) {
    	// Put save command here...
    	IJ.log(path + imp2.getTitle());
    	IJ.save(imp2, path + imp2.getTitle() + ".tif");
        imp2.close();
    }
}

