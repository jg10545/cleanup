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
------------

1. Before you start
===================

* Set up a conda environment with ``jupyter``, ``notebook``, ``numpy``, ``pandas``, ``scikit-learn``, ``matplotlib``, ``pytest``, and ``pytest-cov``.
* I'd recommend using an IDE like ``spyder``, but if you want to do everything in ``vim`` like an absolute maniac I'm not about to dull your sparkle.


2. Run through the notebook
===========================

Run through the notebook ``your_crappy_jupyter_code.ipynb``. This is a simple example of some code that loads and preprocesses some data, fits a machine learning model to it and then produces a visualization.

Our notional task is to clean up this code to make it easier to reuse- we'll arrange the pieces into functions in a Python module, add unit tests and guardrails, and add a command-line interface.

3. Move Jupyter code into functions
===================================

To get you started, I used ``cookiecutter`` to set up a Python package, and added skeleton code for all the functions you'll need. There are three ``.py`` files inside the ``cleanup`` folder:

* ``load.py`` code for reading/preprocessing data will go here
* ``model.py`` code for fitting the ML model will go here
* ``plot.py`` code for generating the figure

You can fill those functions out however you like. I usually take code blocks in Jupyter that I see myself reusing, wrap them in functions and test them inside the notebook, the copy and paste into the ``.py`` files.

Note that we're not actually adding any new functionality or capabilities to the code. The benefits of spending a few minutes reorganizing code we've already written will come when we reuse it:

* **It's easier to test.** Breaking your code out into small pieces and testing them will help make sure you're not reusing typos.
* **It's easier to mix and match.** If, for example, your data comes in a different format next time, just add a function to ``load.py`` and reuse the rest.

4. Add some guardrails with ``logging``
=======================================

The ``logging`` package is built-in to Python and provides a standard way to keep track of what's happening inside your code. It has a hierarchy of built-in levels: ``debug()``, ``info()``, ``warning()``, ``error()``, ``critical()``. You can choose one of these levels as a threshold when you're running your code; for example, if you run this at the start of your code:

>>> logger = logging.getLogger()
logger.setLevel(logging.WARN)

Then it will print out messages at the ``warning``, ``error``, or ``critical`` level but ignore any messages at the  ``debug`` or ``info`` levels.

There's a lot you can do with ``logging`` but I want to flag a couple specific places to get started:

* **Don't use ``print()`` for debugging.** I'm really bad about this. I'll add `print()` statements to my code to check values or dimensions of arrays to make sure everything's doing what I expect it to. Then when it works, I comment them out or remove them all manually until I need them again. A better approach is to replace ``print("current value of myvar: %s"%myvar")`` with ``logging.debug("current value of myvar: %s"%myvar")``. That way you can turn them all off or on at once by setting the logging level to ``logging.DEBUG``.

* **Warn your user if they're doing something you didn't plan for.** Frequently you'll make assumptions about the data being passed around in your code (how big it is, data types, etc); if the user passes something different through it might not be *wrong* but it's probably worth leaving them a note to check.

Generally the dumbest user of my code is me, six months from now.



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
