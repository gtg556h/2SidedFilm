cardiac
=======

Code for analysis of cardiac myocyte mechanical coupling

* 20150131: Discovered that set of libraries installed on 'Wilson' function appropriatel (on 64-bit Linux).  Will debup more later, but, for now, these are the libraries to use!!!  Put in directory 'libWilson'

* 20141107: Starting recently, javacv library load fails on OSX.  Reinstalled in Linux, current versions of everything, and it works!  PIV lib is system independent, therefore problem likely lies in javacv.  Try installing git repo version, not cached copy from PIV website!
* 20150403 status:
** raw PIV data now in /dat
** Restructured scripts so all processing automation code is in cardiac/bin
** Wrote Python scripts
** Need to test and debug!!!

* Status:
** Everything works!
** Now, instead of writing PIV to PIV directory, write it to "<filename>_PIV/dat"
** Then, gen python scripts to make npz arrays, saved in "<filename>_PIV"
** Then, remove all unnecessary imagej generated images!



* Currently working on automating PIV output
* My (almost) functional script is processPIVTemplate.js
* Unfortunately, it is writing the SAME output filename everytime.
* Need to fix and incorporate as template!!!x
