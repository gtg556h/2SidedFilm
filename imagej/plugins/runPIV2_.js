importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.ImageStack);
importClass(Packages.ij.process.ImageProcessor);
importClass(Packages.ij.gui.Toolbar);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);


//////////////////////////////////////////////////////////
// Initialization

IJ.log('hello!');




//////////////////////////////////////////////////////////
// Open stack

imp = IJ.open('/Users/brian/working/2imageStack.tif');
imp = IJ.getImage();
imp.show();



//////////////////////////////////////////////////////////
// Set PIV parameterrs
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

ide = gd.getNextNumber();
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

//var path = IJ.getDirectory("Select a folder to save PIV results");
path = ["/Users/brian/working/"]


///////////////////////////////////////////////////////////
// Set ROI:
// Temp mute:
// imp.createNewRoi();
// imp.getROI();


///////////////////////////////////////////////////////////
// PIV
var stackSize = imp.getImageStackSize();
IJ.log("Slices: " + stackSize);

changes = false;
//setBatchMode(true);

stack = imp.getStack();

for(s=1;s<stackSize;s++){
    var ss = s + 1;
    // Incorporate ROI selection in next step
    // IJ.run("Duplicate...", "title=[seq_"+s+"_"+side+"] duplicate range="+s+"-"+ss+"");

    stack2 = ImageStack(stack.getWidth(), stack.getHeight(), stack.getColorModel());
    ip = stack.getProcessor(s);

    ip2 = ip.createProcessor(stack.getWidth(), stack.getHeight());
    ip2.insert(stack.getProcessor(s),0,0);
    stack2.addSlice(null, ip2);

    ip2 = ip.createProcessor(stack.getWidth(), stack.getHeight());
    ip2.insert(stack.getProcessor(ss),0,0);
    stack2.addSlice(null, ip2);

    imp2 = ImagePlus("current", stack2);
    imp2.show();

    IJ.log("s = " + s);
    IJ.log("s+1 = " + ss);
    IJ.run("iterative PIV(Advanced)...", " piv1="+piv1+" sw1="+sw1+" vs1="+vs1+" piv2="+piv2+" sw2="+sw2+" vs2="+vs2+" piv3="+piv3+" sw3="+sw3+" vs3="+vs3+" correlation="+corr+" batch path=["+path+"]");

    imp2.close();
}


///////////////////////////////////////////////////////////////

