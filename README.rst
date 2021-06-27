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

* **Warn your user if they're doing something you didn't plan for.** Frequently you'll make assumptions about the data being passed around in your code (how big it is, data types, etc); if the user passes something different through it might not be *wrong* but it's probably worth leaving them a note to check. Use ``logging.warn("warning message here")``.

Generally the dumbest user of my code is me, six months from now. I've saved myself a lot of time by adding warnings.

5. Simple unit tests
====================

Now let's start adding unit tests. The basic idea here is to write some simple test code for each of your functions to make sure they return the right answers. Running ``pytest`` from the command line to collect and run all the tests, and tell you if any failed. This way, whenever you make changes to your code, there's a **super easy** way to check whether you've accidentally broken something.

To get you started, I've added a ``tests`` folder to ``cleanup`` and added one Python file for each file in the repo: ``test_load.py``, ``test_model.py``, and ``test_plot.py``. And I've thrown some skeleton code in all of them.

For now, start with ``tests/test_model.py``. I wrote one unit test for you as an example; you write the other. 

6. Unit tests with fixtures
===========================

Parts of our code read from and write to file- ``pytest`` provides some tools to help test that stuff as well.

For testing the code in ``load.py``, we need to add a **fixture-** in this case, a small example data file that looks more-or-less like the kind of data we plan on loading in real life.

* Generate a CSV with a few lines of fake data but the same columns as our dataset.
* Save the file to ``cleanup/tests/fixtures/fakedata.csv``
* Set up the fixture inside ``cleanup/tests/conftest.py``. (I've already filled this part out for you).
* Now you can finally write the unit test for the ``load_and_preprocess()`` function in ``load.py``. When you write the test function, pass ``test_csv`` as an argument and ``pytest``will automatically fill in the location of ``fakedata.csv``.

**Why can't I just hard-code the path to ``fakedata.csv`` in my unit test?** You totally could, and it would work for you. But if you move your code to another machine and the path changes, the unit test will break. Same problem if someone else clones your repo, or if you set up continuous integration with Github actions or Jenkins.

**What about writing to file?** Testing the ability to save our figure to disk is a bit easier- ``pytest`` comes with a built-in fixture called ``tmpdir``. When you run ``pytest``, it will create a temporary directory within your system's default temp directory (e.g. ``/tmp`` on Linux), pass the location of that directory to the unit test, and then delete it all when the tests are done running. 

If you're not a full-time developer, adding fixtures to a repo might be something you do once or twice a year. I have to look up how every time. But when you have that you're reusing and you want to be sure you can rely on it, spending a few minutes on the ``pytest`` documentation page isn't a huge effort.

7. Build a simple command-line interface
========================================

Let's take what we've built

The ``argparse`` library comes with Python and is a really easy tool for building simple CLIs. If you want to build complex CLIs (for example, to make interfaces you can compose between different packages), the ``click`` package provides more functionality (but is also significantly more complicated).

I've built a simple CLI in the file ``cli.py``- it uses ``argparse`` to parse the user's inputs, then just runs through the code we built above (if you used different function names or inputs, you'll have to update them in this file).

If you run the following from the command line:

>>> python cli.py --help

`argparse` will print out documentation on how to use the interface. Using the CLI to actually build a figure would look like:

>>> python cli.py my_data.csv --outputfile my_figure.jpg --logging DEBUG

The ``parser.add_argument()`` lines in ``cli.py`` are how you'd add additional options to the interface. 

* Options with a ``--`` in front of the name are optional; use the ``default`` keyword argument to specify the default.
* The ``help`` keyword argument tells ``argparse`` what to print out when you run the CLI with the ``--help`` flag.
* The ``dtype`` keyword argument tells ``argparse`` what type of input to expect. Even though Python usually lets us play fast and loose with data types, I recommend always filling this in when you're using ``argparse``. 

*




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
