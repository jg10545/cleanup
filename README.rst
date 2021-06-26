===================
code_cleanup_clinic
===================


.. image:: https://img.shields.io/pypi/v/code_cleanup_clinic.svg
        :target: https://pypi.python.org/pypi/code_cleanup_clinic

.. image:: https://img.shields.io/travis/jg10545/code_cleanup_clinic.svg
        :target: https://travis-ci.org/jg10545/code_cleanup_clinic

.. image:: https://readthedocs.org/projects/code-cleanup-clinic/badge/?version=latest
        :target: https://code-cleanup-clinic.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Hands-on example for cleaning up Jupyter notebook code into something more reusable

Goals
-----

At the end of this clinic you should be able to:

* Move code from a Jupyter notebook into a Python module
* Write basic unit tests and run them with ``pytest``
* Add fixtures to test your ability to read and write files
* Add checks and guardrails with ``logging``
* Implement a simple CLI

I'm assuming you already know
-----------------------------

* Basic Python (writing functions)
* Common scientific Python tools (``jupyter``, ``pandas``, etc)




Instructions
============

1. Before you start
-------------------

* Set up a conda environment with ``jupyter``, ``notebook``, ``numpy``, ``pandas``, ``scikit-learn``, ``matplotlib``, ``pytest``, and ``pytest-cov``.
* I'd recommend using an IDE like ``spyder``, but if you want to do everything in ``vim`` like an absolute maniac I'm not about to dull your sparkle.


2. Run through the notebook
---------------------------

Run through the notebook ``your_crappy_jupyter_code.ipynb``. This is a simple example of some code that loads and preprocesses some data





* Free software: MIT license
* Documentation: https://code-cleanup-clinic.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
