importClass(Packages.ij.IJ);
importClass(Packages.ij.WindowManager);
importClass(Packages.ij.plugin.frame.RoiManager);
importClass(Packages.ij.gui.GenericDialog);


// Get class information:
// ob = ...
// IJ.log(ob.getClass());

// View fields:
// s=""; for (a in imp) {s += " " + a; }
// for (a in gd) {
//    IJ.log(a);
// }


IJ.log("");
IJ.log("");
IJ.log("");
IJ.log("");

openPath="/Users/brian/local/cardiac/3imageFilm.tif";
imp = IJ.openImage(openPath);

imp.show();

i0 = WindowManager.getCurrentWindow();
IJ.log("Current window: " + i0);
IJ.log("Class of 'getCurrentWindow'" + i0.getClass());
IJ.log("First image ID " + WindowManager.getNthImageID(1));

s=0;
ss = s+2;
IJ.run("Duplicate...", "title=[seq] duplicate range="+s+"-"+ss+"");
IJ.run("Duplicate...", "title=[seq2] duplicate");

//WindowManager.getImage("seq");
//WindowManager.setWindow(i0);
IJ.log("Number of windows: " + WindowManager.getWindowCount());
IJ.log("Last image ID: " + WindowManager.getNthImageID(3));

// Works!!!!       ------>
//imp2 = WindowManager.getImage(WindowManager.getNthImageID(2));
//imp2.close();
//imp2 = WindowManager.getImage(WindowManager.getNthImageID(2));
//imp2.close();

while(imp2 = WindowManager.getImage(WindowManager.getNthImageID(2))) {
	imp2.close();
}








//imp = IJ.getImage();
//var i0 = imp.getID();
//i0 = WindowManager.getCurrentWindow();
//IJ.log(i0);



// imp.createNewRoi();
// imp.getROI();
//var path = IJ.getDirectory("Select a folder to save PIV results");
//path = ["/Users/brian/working/"]

//var stackSize = imp.getImageStackSize();
//IJ.log("Slices: " + stackSize);


//setBatchMode(true);
//for(s=0;s<stackSize;s++){
//	ss = s + 2;
	// Incorporate ROI selection in next step
//	IJ.run("Duplicate...", "title=[seq_"+s+"] duplicate range="+s+"-"+ss+"");
//	IJ.log("s = " + s);
//	IJ.log("s+1 = " + ss);
	//IJ.selectWindow(i0);
	//WindowManager.setCurrentWindow(i0);
	//flushWindows();
//}



function flushWindows() {
	var imageCount = WindowManager.getImageCount();
	IJ.log(imageCount);
    for(s=1;s<imageCount+1;s++){
	
    	if(WindowManager.getCurrentWindow()!=i0){
	    	IJ.run("Close");
	    	//IJ.log("Closing time!!!");
	    }

	    else{
	    WindowManager.putBehind();
	    }
    }
    return;
}

