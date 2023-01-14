highlightディレクティブの練習
========================================

ref: https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html#directive-highlight

.. highlight:: rest
    :linenothreshold: 1

reSTのハイライトを指定（行番号付きで指定）

::

    Doctest blockの例
    ====================

    >>> 1 + 1
    2

.. code-block::

    Literal blockの例です::

        ここがLiteral block

.. highlight:: python

ここでpythonのハイライトに変更::

    >>> print("highlightディレクティブの練習です")
    highlightディレクティブの練習です
