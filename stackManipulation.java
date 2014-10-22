import ij.IJ;
import ij.ImagePlus;
import ij.ImageStack;

/*
import ij.WindowManager;
import ij.gui.GenericDialog;
import ij.gui.Toolbar;
import ij.plugin.PlugIn;
import ij.process.ImageProcessor;

/*
//ImagePlus imp1;
ImagePlus imp1 = WindowManager.getCurrentImage();
ImageStack stack1 = imp1.getStack();

int d1 = stack1.getSize();
int w1 = stack1.getWidth();
int h1 = stack1.getHeight();

/* int w3 = Math.max(w1, w2);
   ImageStack stack3 = new ImageStack(w3, h3, stack1.getColorModel());
*/

int d2 = 2;
int w2 = w1;
int h2 = h1;
int n = 1;

/*
ImageStack stack2 = new ImageStack(w2, h2, stack1.getColorModel());
ImageProcessor ip = stack1.getProcessor(n);
ImageProcessor ip2;

ip3 = ip.createProcessor(w3,h3);
ip3.insert(stack1.getProcessor(n),0,0);
stack3.addSlice(null, ip3);
ip3 = ip.createProcessor(w3,h3);
ip3.insert(stack1.getProcessor(n+1),0,0);
stack3.addSlice(null, ip3);

new ImagePlus("current pair", stack2).show();
*/
