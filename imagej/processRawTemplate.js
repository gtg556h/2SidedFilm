importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.ImageStack);


// Following line should be built by bash script:
stem = 


str1 = "open=./";
str2 = "/spool0000000000.dat image=[16-bit Unsigned] width=";
str3 = " height=";
str4 = " offset=0 number=1 gap=0 little-endian open";

str = str1 + stem + str2 + width + str3 + height + str4;

IJ.log(str);

IJ.run("Raw...", str);

//IJ.run("Raw...", "open=/home/brian/data3/projects/cardiac/20150217_bridgeExp/20150219_b3_CHS_528_10x_50fps_16bit/spool0000000000.dat image=[16-bit Unsigned] width=528 height=512 ofsset=0 number=1 gap=0 little-endian open");

imp = IJ.getImage();

IJ.log("Preparing to save");

IJ.saveAs("Tiff", "/mnt/ssd/output.tiff");
IJ.saveAs("Tiff", "./" + stem + ".tiff");

IJ.log("Video saved");



// Don't include following lines!!!
width="528";
height="512";
