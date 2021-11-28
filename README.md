[![Documentation Status](https://readthedocs.org/projects/simpa/badge/?version=latest)](https://simpa.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://ci.mitk.org/buildStatus/icon?job=SIMPA%2FUnit+Tests+master)](https://ci.mitk.org/job/SIMPA/job/Unit%20Tests%20master/)

# README

The Simulation and Image Processing for Photoacoustic Imaging (SIMPA) toolkit.

**(!) Alpha Version 0.4.0 (!)** 

The toolkit is still under development and is thus not fully tested and may contain bugs. 
Please report any issues that you find in our Issue Tracker: https://github.com/CAMI-DKFZ/simpa/issues. 
Also make sure to double check all value ranges of the optical and acoustic tissue properties 
and to assess all simulation results for plausibility.

## SIMPA Install Instructions

The recommended way to install simpa is a manual installation from the GitHub repository, please follow steps 1 - 3:

1. `git clone https://github.com/CAMI-DKFZ/simpa.git`
2. `cd simpa`
3. `git checkout master`
4. `git pull`

Now open a python instance in the 'simpa' folder that you have just downloaded. Make sure that you have your preferred
virtual environment activated
1. `pip install -r requirements.txt`
2. `python setup.py install` (for developement: `python setup.py develop`)
3. Test if the installation worked by using `python` followed by `import simpa` then `exit()`

If no error messages arise, you are now setup to use simpa in your project.

You can also install simpa with pip. Simply run:

`pip install simpa`

You also need to manually install the pytorch library to use all features of SIMPA.
To this end, use the pytorch website tool to figure out which version to install:
`https://pytorch.org/get-started/locally/`

## Building the documentation

When the installation succeeded, and you want to make sure that you have the latest documentation
you should do the following steps in a command line:

1. Navigate to the `simpa/docs` directory
2. Execute the command `sphinx-apidoc -EfTM -o ./source/ ../simpa`
3. Execute the command `python source/clean_up_rst_files.py`
4. Type `make html`
5. Open the `index.html` file in the `simpa/docs/build/html` directory with your favourite browser. 

## External Tools installation instructions

### mcx (Optical Forward Model)

Either download suitable executables or build yourself from the following sources:

http://mcx.space/

In order to obtain access to all custom sources that we implemented, please build mcx yourself from the
following mcx Github fork:
https://www.github.com/jgroehl/mcx

For the installation, please follow the instructions from the original repository.
Please note that there might be compatiblity issues using mcx-cl with the MCX Adapter as this use case is not 
being tested and supported by the SIMPA developers.

### k-Wave (Acoustic Forward Model)

Please follow the following steps and use the k-Wave install instructions 
for further (and much better) guidance under:

http://www.k-wave.org/

1. Install MATLAB with the core and parallel computing toolboxes activated at the minimum.
2. Download the kWave toolbox
3. Add the kWave toolbox base path to the toolbox paths in MATLAB
4. Download the kWaveArray addition from the link given in this user forum post http://www.k-wave.org/forum/topic/alpha-version-of-kwavearray-off-grid-sources
5. Add the kWaveArray folder to the toolbox paths in MATLAB as well
6. If wanted: Download the CPP and CUDA binary files and place them inthe k-Wave/binaries folder
7. Note down the system path to the `matlab` executable file.

## Overview

The main use case for the simpa framework is the simulation of photoacoustic images.
However, it can also be used for image processing.

### Simulating photoacoustic images

A basic example on how to use simpa in your project to run an optical forward simulation is given in the 
samples/minimal_optical_simulation.py file.

### Path Management

As a pipelining tool that serves as a communication layer between different numerical forward models and
processing tools, SIMPA needs to be configured with the paths to these tools on your local hard drive.
To this end, we have implemented the `PathManager` class that you can import to your project using
`from simpa.utils import PathManager`. The PathManager looks for a `path_config.env` file (just like the
one we provided in the `simpa_examples`) in the following places in this order:
1. The optional path you give the PathManager
2. Your $HOME$ directory
3. The current working directory
4. The SIMPA home directory path

## How to contribute

Please find a more detailed description of how to contribute as well as code style references in **CONTRIBUTING.md**

To contribute to SIMPA, please fork the SIMPA github repository and create a pull request with a branch containing your 
suggested changes. The core developers will then review the suggested changes and integrate these into the code 
base.

Please make sure that you have included unit tests for your code and that all previous tests still run through.

There is a regular SIMPA status meeting every Friday on even calendar weeks at 10:00 CET/CEST and you are very welcome to participate and
raise any issues or suggest new features. If you want to join this meeting, write one of the core developers.

Please see the github guidelines for creating pull requests: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests


## Performance profiling

Do you wish to know which parts of the simulation pipeline cost the most amount of time? 
If that is the case then you can use the following commands to profile the execution of your simulation script.
You simply need to replace the `myscript` name with your script name.

`python -m cProfile -o myscript.cprof myscript.py`

`pyprof2calltree -k -i myscript.cprof`

## Troubleshooting

In this section, known problems are listed with their solutions (if available):

### 1. Error reading hdf5-files when using k-Wave binaries:
   
If you encounter an error similar to:

    Error using h5readc
    The filename specified was either not found on the MATLAB path or it contains unsupported characters.

Look up the solution in [this thread of the k-Wave forum](http://www.k-wave.org/forum/topic/error-reading-h5-files-when-using-binaries).  
      