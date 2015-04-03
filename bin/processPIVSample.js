importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.ImageStack);
importClass(Packages.ij.process.ImageProcessor);
importClass(Packages.ij.gui.Toolbar);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);

side = 0;
piv1 = 64;
sw1 = 128;
vs1 = 32;
piv2 = 32;
sw2 = 64;
vs2 = 16;
piv3 = 0;
sw3 = 0;
vs3 = 0;
corr = 0.8;
path = "/home/brian/working/pivOutput/";

// Following line should be built by bash script:

imp = IJ.openImage("/home/brian/working/sampleStack.tif")
IJ.log("opened image");
imp.show();

//i0 = WindowManager.getCurrentWindow();
IJ.run("StackReg", "transformation=[Rigid Body]");
IJ.saveAs("Tiff", "/home/brian/working/sampleStack_bgs.tif");

IJ.log("Video saved");

var stackSize = imp.getImageStackSize();
IJ.log("Slices: " + stackSize);
changes = false;

stack = imp.getStack();
for(s=1;s<stackSize;s++){
    var ss = s+1;

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
    
    //IJ.run("iterative PIV(Advanced)...", " piv1="+piv1+" sw1="+sw1+" vs1="+vs1+" piv2="+piv2+" sw2="+sw2+"   vs2="+vs2+" piv3="+piv3+" sw3="+sw3+" vs3="+vs3+" correlation="+corr+" batch path=["+path+"]");

    IJ.run("iterative PIV(Advanced)...", " piv1=64 sw1=128 vs1=32 piv2=32 sw2=64 vs2=16 piv3=0 correlation=0.8 batch path=[/home/brian/working/pivOutput/]");


    
    imp2.changes = false;
    imp2.close();

}


imp.close();



