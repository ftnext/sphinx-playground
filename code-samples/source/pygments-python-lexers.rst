Python使い向けPygments lexers
========================================

PythonLexer
----------------------------

https://pygments.org/docs/lexers/#pygments.lexers.python.PythonLexer

``language`` を ``python`` や ``py`` のように指定

.. code-block:: python

    import this

.. code-block:: py

    print(1 / 0)

PythonConsoleLexer
----------------------------

https://pygments.org/docs/lexers/#pygments.lexers.python.PythonConsoleLexer

``language`` を ``python-console`` や ``pycon`` と指定

.. code-block:: python-console

    >>> message = "Hello, World!"
    >>> print(message)
    Hello, World!

.. code-block:: pycon

    >>> 1 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

PythonTracebackLexer
----------------------------

https://pygments.org/docs/lexers/#pygments.lexers.python.PythonTracebackLexer

``language`` を ``pytb`` や ``py3tb`` と指定

.. code-block:: pytb

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
