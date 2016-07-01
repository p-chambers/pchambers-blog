Title: Intermediate Python Tutorial
Slug: intermediate_python
Date: 2016-06-28 12:49:46
Tags: Python, Jupyter Notebook
Category: Tutorials
Author: Paul Chambers
Summary: ![Python Logo]({filename}/images/Python-logo-notext.png){width=100} Structuring data with Python: basics review, Tuples, Dictionaries and Classes

<!-- The contents box (auto generation with [TOC] mdextension didn't extract ipython notebook headings) -->
<div class="toc" markdown="1">
Contents
--------
0. [Introduction](#intro)
0. Prerequisites
	- [Software Requirements](http://ngcm.github.io/summer-academy-2016-basics/indexpages/prerequisites.html)
	- [Material Download](https://github.com/p-chambers/Intermediate_Python/archive/master.zip)
1. [Basics refresher](#Basics-Refresher)
	- [Lists](#Lists)
	- [For loops](#For-Loops)
    - [Functions](#Functions)
    - [Numpy](#Numpy)
    - [Matplotlib](#Matplotlib)
    - [Exercise](#Exercise:-Basics-Refresher)
2. [Tuples](#Tuples)
3. [Dictionaries](#Dictionaries)
	[Exercise](#Exercise:-Tuples-and-Dictionaries)
4. [Numpy dtypes](#Structured-data:-Numpy-dtypes)
	- [Exercise](#Exercise:-Numpy-dtypes)
5. [Object-oriented programming (OOP)](#Intro-to-Python-OOP)
	- [Classes basics](#Classes:-Basics)
	- [Initialisation and self](#Classes:-Initialisation-and-self)
		* [Classes Exercise 1](#Exercise:-Basics-and-Initialisation)
	- [Encapsulation](#Classes:-Encapsulation)
	- [Inheritance](#Classes:-Inheritance)
	- [Magic Methods](#Classes:-Magic-Methods)
		* [Classes Exercise 2](#Exercise:-Inheritance-and-Magic-Methods)
6. [Extras](#Python-2-vs-3)
	- [Python 2 vs 3](#Python-2-vs-3)
	- [Additional exercise](#Extra-Material)
7. [Summary](#Summary)

</div>
<!-- End contents box -->

Introduction   {#intro}
------------

This tutorial was presented at the [NGCM Summer Academy 2016 Basics B](http://www.ngcm.soton.ac.uk/summer-academy/basics.html) course, and is created for the purpose of teaching Python programming concepts to extend that of the [Software Carpentry style basics course](https://github.com/softwaresaved/NGCMGSoton-2015-06-21). **The material is taught in Python 3, and code outputs displayed are the result from a Python 3.5 Jupyter notebook.**

The concepts of OOP are often covered lightly in undergraduate and basics courses. Despite this, Large amounts of scientific Python packages are written in an object oriented manner. The skills learned in this workshop should therefore enable scientists to write (and more importantly, read) the packages they are using, and also serve as a starting platform for those wanting to learn more advanced OOP languages such as C++ or Java.

![Summer academy teaching]({filename}/images/28-06-16_summer_academy_python.jpg){width="850"}

Software Requirements
---------------------

Setup instructions for a range of users are available [here](http://ngcm.github.io/summer-academy-2016-basics/indexpages/prerequisites.html). Click [here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) for more info on how to start a live Jupyter notebook.

# Getting Started

** Teaching material is largely in Jupyter Notebook format, and should be [downloaded](https://github.com/p-chambers/Intermediate_Python/archive/master.zip) or [cloned from GitHub](https://github.com/p-chambers/Intermediate_Python) - data included in the links will be necessary for completing the exercises.**

{% notebook Intermediate_Python/index.ipynb %}
