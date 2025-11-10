.. test_julia documentation master file, created by
   sphinx-quickstart on Tue Nov  4 16:37:18 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

test_julia documentation
========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

C API Documentation
========================

.. doxygenfunction:: sum
   :project: libadd

.. doxygenfunction:: sub
   :project: libadd

Julia API Documentation
========================
See the Julia wrapper function :ref:`julia:test_julia.testJuliaFunction` or
the Julia API docs for :external+julia:func:`test_julia.testJuliaFunction`.