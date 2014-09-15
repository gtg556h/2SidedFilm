importClass(Packages.ij.IJ);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);

s = 2;
ss = 4;
IJ.run("Duplicate...", "title=[seq_"+s+"] duplicate range="+s+"-"+ss+"");