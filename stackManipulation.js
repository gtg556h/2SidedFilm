importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.ImageStack);
importClass(Packages.ij.process.ImageProcessor);
importClass(Packages.ij.gui.Toolbar);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);
//importClass(Packages.ij.plugin.Plugin);


imp1 = IJ.getImage();
//var i0 = imp.getID();
i1 = WindowManager.getCurrentWindow();
IJ.log(i1);

stack1 = imp1.getStack();
d1 = stack1.getSize();
w1 = stack1.getWidth();
h1 = stack1.getHeight();

IJ.log(d1)

var d2 = 2;
var w2 = w1;
var h2 = h1;
var n = 1;

stack2 = ImageStack(w2, h2, stack1.getColorModel());
ip = stack1.getProcessor(n);

ip2 = ip.createProcessor(w2,h2);
ip2.insert(stack1.getProcessor(n),0,0);
stack2.addSlice(null, ip2);

ip2 = ip.createProcessor(w2,h2);
ip2.insert(stack1.getProcessor(n+1),0,0);
stack2.addSlice(null,ip2);

imp2 = ImagePlus("current pair", stack2);
imp2.show();

IJ.log("cool");

imp2.close();



// Temp mute:
// imp.createNewRoi();
// imp.getROI();

//var path = IJ.getDirectory("Select a folder to save PIV results");
/*
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
*/
