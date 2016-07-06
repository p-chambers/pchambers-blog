Title: Aircraft Geometry in Python
Slug: occ-airconics
Date: 2016-05-04 15:26:21
Tags: Geometry, Python-OCC
Category: Projects
Author: Paul Chambers

![occ-airconics Airliner Geometry]({filename}/images/Projects/occ-airconics_airliner.png){class=align-center}


As part of my research, I am interested in the use of computer code as a parameterized ‘recipe’ for constructing air vehicle preliminary designs. By defining the ‘bottom-up’ construction of the geometry in this way, a high level of flexibility and reproducibility can be achieved, both of which are desirable traits in the context of design optimisation. The [AirCONICS](https://aircraftgeometrycodes.wordpress.com/airconics/) plugin for [Rhinoceros](http://www.rhino3d.com/) [1, 2] is one such tool, containing generic and highly customizable recipes for creating aircraft components as Python/Rhino objects.

This project aims to port the aircraft geometry routines of AirCONICS to a Python standalone package through through a code called [occ_airconics](http://occ-airconics.readthedocs.io/en/latest/index.html). Instead of using the [OpenNURBS](http://www.rhino3d.com/opennurbs) framework through Rhinoceros, the package is powered by [Open CASCADE](http://www.opencascade.com/), an open source NURBS CAD kernel, and [PythonOCC](http://www.pythonocc.org/).

&nbsp;

**“So what makes this interesting?”**

&nbsp;

`occ_airconics` has no proprietary dependencies, thereby providing an immediately available and free platform for aircraft concept design with a similar API to AirCONICS. As it runs on a standard Python installation, occ_airconics is portable and available on all of the common platforms.

Current AirCONICS users working with Multidisciplinary Design Optimisation (MDO) may also benefit from `occ_airconics` due to the ease of integration with external scientific libraries such as `numpy` and `scipy` for mathematical operations, `scikit-learn` for machine-learning or `mpi4py` for parallel programming. These libraries are less readily integrated with Rhino due to its .NET Python kernel. It should be noted however that due to an absence of core functions previously used in Rhino, `occ_airconics` may produce different and potentially lower quality geometries than the Rhino version.

Key features of `occ_airconics`
-------------------------------

* Provides much of the same functionality as AirCONICS
* Totally open source and cross platform
* Native access to CPython packages, e.g. *numpy, scipy, scikit-learn*...
* Easy to install via the [conda package](http://occ-airconics.readthedocs.io/en/latest/installation.html#conda-packages)
* Readily Integrated with IPython, providing object introspection and PythonOCC’s [Notebook rendering](http://occ-airconics.readthedocs.io/en/latest/examples.html#transonic-airliner)

Development
-----------

Future development directions for occ_airconics are towards a topologically flexible aircraft concept parameterisation, and subsequent optimisation using machine learning algorithms. This will include integration with aerodynamic analysis.

Installation
------------
`occ_airconics` is available now, to get started simply visit the [installation instructions](http://occ-airconics.readthedocs.io/en/latest/installation.html).

References
----------
[1] Sóbester, A., Forrester, A. I. J., *Aircraft Aerodynamic Design – Geometry and Optimization*, Wiley, 2015.

[2] Sóbester, A., “Self-Designing Parametric Geometries”, AIAA 2015-0396.

*Note*: This project summary originates from a similar post on the [AirCONICS blog](https://aircraftgeometrycodes.wordpress.com/2016/05/04/standalone-airconics-for-python/), also written by P Chambers.