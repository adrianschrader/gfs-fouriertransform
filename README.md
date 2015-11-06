# gfs-fouriertransform
Presentation and project documentation about the basics of integral transformation and Fourier spectral analysis.

## Building instructions
This projects uses a central Makefile for all building activities, that depends on your command line LaTeX distribution.

```bash
cd gfs-fouriertransform

make all # Make all projects
make doc # Only build the written documentation
make beamer # Only build the beamer presentation

make clean # Delete all temporary build files, will preserve your PDF output
```

All projects share the same resources via symlinks. Should those not work on your workstation, update them like this:

```bash
sudo chmod +x symlinks.sh
./symlinks.sh
```

## Dependencies
Make sure you have following software installed and updated on your workstation:

* LaTeX distribution for your operating system (e.g [MacTeX](https://tug.org/mactex/))
* [mtheme](matze/mtheme) beamer theme
* Python 2.7 or 3.0
  + [NumPy](http://www.numpy.org)
  + [SciPy](http://www.scipy.org/scipylib/index.html)
  + [matplotlib](http://matplotlib.org)
* Xcode command line tools for make

Use this bash snipped to install the python dependencies via pip

```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

pip install numpy scipy matplotlib
```
