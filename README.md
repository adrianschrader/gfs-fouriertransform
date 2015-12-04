# gfs-fouriertransform
Presentation and project documentation about the basics of integral transformation and Fourier spectral analysis.

## Abstract from the documentation (german)
In allen Wissenschaftsfeldern ist die Interferenz von Signalen ein Problem für Analytik und Verarbeitung. Die Fourieranalyse und ihre Varianten bilden bis heute ein mächtiges Werkzeug, um zeitabhängige Signale in ihr Frequenzsprektrum aufzuspalten und zu analysieren. Dieses Paper bietet ausführlichere Beschreibungen zu den Beispielen und mathematische Hintergründe zum Vortrag \glqq Fourieranalyse - Hintergründe und Anwendungen von Frequenzanalysen\grqq.


## Building instructions
This projects uses a central Makefile for all building activities that depends on your command line LaTeX distribution.

```bash
cd gfs-fouriertransform

make all # Make all projects
make doc # Only build the written documentation
make beamer # Only build the beamer presentation

make clean # Delete all temporary build files, will preserve your PDF output
```

All projects share the same resources via symlinks. Should those not work on your workstation update them like this:

```bash
sudo chmod +x configure.sh
./configure.sh
```

## Dependencies
Make sure you have following software installed and updated on your workstation:

* LaTeX distribution for your operating system (e.g [MacTeX](https://tug.org/mactex/))
* [mtheme](matze/mtheme) beamer theme
* Xcode command line tools for make
