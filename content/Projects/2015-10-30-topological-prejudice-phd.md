Title: Challenging Topological Prejudice - Automated Airframe Layout Design
Slug: topological-prejudice-phd
Date: 2015-10-30 14:33:17
Tags: Aircraft, Optimisation, Machine Learning
Category: Projects
Author: Paul Chambers


**PhD Candidate**: [Paul Chambers](../pages/about.html)

**Supervisor**: [Andras Sobester](http://www.southampton.ac.uk/engineering/about/staff/as7.page)

**Ending**: 30th September 2018

Overview
--------

Aircraft preliminary design scopes are drastically narrowed by topological prejudice. Modern aircraft have settled on the same 'tube plus wing and cruciform tail' type topology that has been adopted through their ancestry, with no scientific evidence that this layout is optimal. This research project poses the question:

*“Given a topologically flexible aircraft geometry that is free of prejudice or bias, would a sophisticated multi-disciplinary optimization process yield a conventional layout?”*

Background
----------

There is an obvious hierarchy in terms of the construction of the external geometry of an airframe. At the lowest level are the geometric primitives e.g. generic curves and surfaces, followed by aircraft-specific primitives e.g. airfoils, fuselage sections, and then major three-dimensional sub-components such as lifting surfaces and enclosure-type objects (fuselages, fairings, nacelles). The last decade has seen much progress in optimal design technology driven by high fidelity analysis codes up to this level. But there is another, higher level: the layout - or topology - of the overall airframe. This is a poorly understood aspect of aircraft design and there are many unanswered questions.

<div class="align-center">
	<img alt="Sobester GP tree" src="{filename}/images/Projects/GA-sobester.png"></img>
	<center>Figure 1: Genetic Programming is one of the techniques being considered as a potential search method through the space of airframe layout designs [1].</center>
</div>

Motivation
----------

* Challenge long standing prejudices in aircraft design: Can we do better?

* Widen design scopes for future air vehicles

* Combine conceptual design flexibility with preliminary design fidelity

The development of a 'self-designing' geometry, which is free of topological bias, lies at the heart of this project. Advances will be made through integration of a scripted geometry toolkit such as the [AirCONICS](https://aircraftgeometrycodes.wordpress.com/) environment [2, 3] with a higher level topology generation algorithm. Novel layout optimization procedures and tools based on aircraft mission-specific goals are the key outcomes of the work.

### References

[1] Sóbester, A., “Four Suggestions for Better Parametric Geometries,” *10th AIAA Multidisciplinary Design Optimization Conference*, AIAA SciTech, American In stitute of Aeronautics and Astronautics, jan 2014.

[2] Sóbester, A., Forrester, A. I. J., *Aircraft Aerodynamic Design – Geometry and Optimization*, Wiley, 2015.

[3] Sóbester, A., “Self-Designing Parametric Geometries”, AIAA 2015-0396.

Acknowledgements
----------------

This project is run through the EPSRC [Centre for Doctoral Training in Next Generation Computational Modelling](http://ngcm.soton.ac.uk), grant code EP/L015382/1.
