literalincludeディレクティブの練習
========================================

.. highlight:: rest

ref: https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html#directive-literalinclude

::

    .. literalinclude:: included.py
        :language: python
        :linenos:
        :emphasize-lines: 2
        :caption:
        :start-after: [initialize]
        :end-before: [initialize]

.. literalinclude:: included.py
    :language: python
    :linenos:
    :emphasize-lines: 2
    :caption:
    :start-after: [initialize]
    :end-before: [initialize]

start-atやend-atオプションは指定したパターンの行を **含む**::

    .. literalinclude:: included.py
        :language: python
        :lineno-match:
        :start-at: [initialize]
        :end-before: [initialize]

.. literalinclude:: included.py
    :language: python
    :lineno-match:
    :start-at: [initialize]
    :end-before: [initialize]

::

    .. literalinclude:: included.py
        :language: python
        :lineno-match:
        :start-after: [initialize]
        :end-at: [initialize]

.. literalinclude:: included.py
    :language: python
    :lineno-match:
    :start-after: [initialize]
    :end-at: [initialize]

start-atとend-atで同じパターンを指定するとその行しか表示されない挙動だった::

    .. literalinclude:: included.py
        :language: python
        :lineno-match:
        :start-at: [initialize]
        :end-at: [initialize]

.. literalinclude:: included.py
    :language: python
    :lineno-match:
    :start-at: [initialize]
    :end-at: [initialize]
