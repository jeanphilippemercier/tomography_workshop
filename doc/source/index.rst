.. ESTUARY workshop documentation master file, created by
   sphinx-quickstart on Mon Mar 30 20:58:51 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ESTUARY workshop's documentation!
============================================

Contents:

.. toctree::
   :maxdepth: 2

Software setup
==============================

1. Unzip estuary.tar.gz into the directory of your choice (e.g., $HOME/bin/.)

2. Add the follwing lines into your .bashrc

.. code-block:: bash
    :linenos:

    # AGSIS ESTUARY software
    export AGSIS_HOME="${HOME}/PATH/TO/ESTUARY"
    export PATH="${PATH}:${AGSIS_HOME}/src/eikonal-ng/bin"

    export PATH="${PATH}:${AGSIS_HOME}/bin"
    export PLATFORM="linux-x86_64-2.7"

    export EIKONAL_LIB="${AGSIS_HOME}/src/eikonal-ng/build/lib.${PLATFORM}"
    export AGSTD_LIB="${AGSIS_HOME}/src/agstd"
    export SCONS_HORRIBLE_REGRESSION_TEST_HACK=1
    export PYTHONPATH="${PYTHONPATH}:${CYCL_LIB}:${EIKONAL_LIB}:${AGSTD_LIB}"

    export SITE_DIR="${AGSIS_HOME}/src/estuaire/site_scons"

replace *$HOME/PATH/TO/ESTUARY* by the location of the where ESTUARY was unziped

for mac users replace "linux-x86_64-2.7" by "macosx-10.10-intel-2.7" in line 6

3. Install the required packages and software

.. code-block:: bash
    :linenos:

    sudo apt-get install make
    sudo apt-get install cython
    sudo apt-get install scons
    sudo apt-get install ipython
    sudo apt-get install python-numpy
    sudo apt-get install python-scipy
    sudo apt-get install python-matplotlib
    sudo apt-get install sqlite3
    sudo apt-get install python-mako
    sudo apt-get install python-tables

4. Install paraview for result visualization

.. code-block:: bash
   sudo apt-get install paraview

or download from the web

Paraview_
.. _Paraview: http://www.paraview.org/download/ 

5. Build the eikonal_ng package

.. code-block:: bash
    :linenos:
    
    cd $HOME/PATH/TO/ESTUARY/src/eikonal_ng
    make clean
    make


Running the example
==============================

1. Go to the example directory

.. code-block:: bash

    cd $HOME/PATH/TO/WORKSHOP/DIRECTORY
    cd example

2. Build the velocity model and generate a set of event station and traveltimes by typing "make"

3. Edit the second line of the Makefile so the path points to your estuary installation

.. code-block:: bash
    
    site_dir = $AGSIS_HOME/src/estuaire/site_scons

4. Edit the SConstruct file.

5. type "make"


Visualizing the results
==============================

1. Visualizing velocity model (EKImageData):

   The velocity models produced by the tomography software need to be converted 
   to VTK. To convert the model into VTK the script "EKImageData2VTK" is used.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

