importClass(Packages.ij.IJ);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);




imp = IJ.getImage();
//var i0 = imp.getID();
i0 = WindowManager.getCurrentWindow();
IJ.log(i0);


 
IJ.run("StackReg", "transformation=[Rigid Body]");

