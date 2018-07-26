Pull Request Guidelines
=======================

**Only Edit Relevant Files**


- Focus your pull request on a single feature or issue.
- Please do not change files unrelated to that specific issue or feature.

 
**Submit Clean Code**


- Style you're code using PEP8_ conventions.
- Include docstrings_ for any new modules, classes, or functions that are recognizable to sphinx-apidoc_.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/?
.. _docstrings: https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
.. _sphinx-apidoc: http://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html

**Write Tests**


This project uses pytest_ for unit tests.

- If you're adding a feature please write tests to support it.
- If you're fixing a bug please add tests to reproduce it.

.. _pytest: https://docs.pytest.org/en/latest

**Make Sure Your Tests Pass**


All of this project's tests can be ran by typing: 

.. code-block:: bash

   pytest

in the root directory.

**Keep Commit History Short and Clean**


Please make one commit per feature or bug.
Short histories aid in finding bugs and helping to identify the best fixes.

**Be Descriptive**

State a convincing case why your PR should be accepted.
For tips on writing pull requests see this article_

.. _article: https://blog.github.com/2015-01-21-how-to-write-the-perfect-pull-request

