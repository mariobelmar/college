Advanced pandas series functionnality on strings
================================================
.. raw:: latex

   \etocsettocstyle{}{}\localtableofcontents

Creating a pandas series:

.. code:: python

  >>> import pandas as pd
  >>> s = pd.Series(['Dog', 'elePhant', 'TIGER  '])

Capitalize first letter and lowerize others letter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s.str.capitalize()
  0         Dog
  1    Elephant
  2     Tiger
  dtype: object

Concatenate all strings of a Serie into one or two series together elementwise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Signature: s.str.cat(others=None, sep=None, na_rep=None, join=None)
Docstring:
Concatenate strings in the Series/Index with given separator.

If `others` is specified, this function concatenates the Series/Index
and elements of `others` element-wise.
If `others` is not passed, then all values in the Series/Index are
concatenated into a single string with a given `sep`.

When not passing `others`, all values are concatenated into a single
string:

.. code:: python

  >>> s = pd.Series(['a', 'b', np.nan, 'd'])
  >>> s.str.cat(sep=' ')
  'a b d'

By default, NA values in the Series are ignored. Using `na_rep`, they
can be given a representation:

.. code:: python

  >>> s.str.cat(sep=' ', na_rep='?')
  'a b ? d'

If `others` is specified, corresponding values are concatenated with
the separator. Result will be a Series of strings.:

.. code:: python

  >>> s.str.cat(['A', 'B', 'C', 'D'], sep=',')
  0    a,A
  1    b,B
  2    NaN
  3    d,D
  dtype: object

Missing values will remain missing in the result, but can again be
represented using `na_rep`:

.. code:: python

  >>> s.str.cat(['A', 'B', 'C', 'D'], sep=',', na_rep='-')
  0    a,A
  1    b,B
  2    -,C
  3    d,D
  dtype: object

If `sep` is not specified, the values are concatenated without
separation.:

.. code:: python

  >>> s.str.cat(['A', 'B', 'C', 'D'], na_rep='-')
  0    aA
  1    bB
  2    -C
  3    dD
  dtype: object

Series with different indexes can be aligned before concatenation. The ``join`` -keyword
works as in other methods.:

.. code:: python

  >>> t = pd.Series(['d', 'a', 'e', 'c'], index=[3, 0, 4, 2])
  >>> s.str.cat(t, join=None, na_rep='-')
  0    ad
  1    ba
  2    -e
  3    dc
  dtype: object

  >>> s.str.cat(t, join='left', na_rep='-')
  0    aa
  1    b-
  2    -c
  3    dd
  dtype: object
  >>>
  >>> s.str.cat(t, join='outer', na_rep='-')
  0    aa
  1    b-
  2    -c
  3    dd
  4    -e
  dtype: object
  >>>
  >>> s.str.cat(t, join='inner', na_rep='-')
  0    aa
  2    -c
  3    dd
  dtype: object
  >>>
  >>> s.str.cat(t, join='right', na_rep='-')
  3    dd
  0    aa
  4    -e
  2    -c
  dtype: object

Check if string contains pattern (regex or no)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
  >>> s1.str.contains('og', regex=False)
  0    False
  1     True
  2    False
  3    False
  4      NaN
  dtype: object

Count number of times a pattern was found on every elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s = pd.Series(['A', 'B', 'Aaba', 'Baca', np.nan, 'CABA', 'cat'])
  >>> s.str.count('a')
  0    0.0
  1    0.0
  2    2.0
  3    2.0
  4    NaN
  5    0.0
  6    1.0
  dtype: float64

if elements endswith a given string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s = pd.Series(['bat', 'bear', 'caT', np.nan])
  >>> s
  0     bat
  1    bear
  2     caT
  3     NaN
  dtype: object
  >>> s.str.endswith('t')
  0     True
  1    False
  2    False
  3      NaN
  dtype: object

Extract group from a given regex into a DataFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s = Series(['a1', 'b2', 'c3'])
  >>> s.str.extract(r'([ab])(\d)')
       0    1
  0    a    1
  1    b    2
  2  NaN  NaN

Return lowest index of pattern found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: python


  >>> s
  0         Dog
  1    elePhant
  2     TIGER
  dtype: object
  >>> s.str.find('e')
  0   -1
  1    0
  2   -1
  dtype: int64

return all match found
~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s = pd.Series(['Lion', 'Monkey', 'Rabbit'])

The search for the pattern 'Monkey' returns one match:

.. code:: python

  >>> s.str.findall('Monkey')
  0          []
  1    [Monkey]
  2          []
  dtype: object

get ieme position of each element:

.. code:: python

  >>> s = pd.Series(["String",
             (1, 2, 3),
             ["a", "b", "c"],
             123, -456,
             {1:"Hello", "2":"World"}])
  >>> s
  0                        String
  1                     (1, 2, 3)
  2                     [a, b, c]
  3                           123
  4                          -456
  5    {1: 'Hello', '2': 'World'}
  dtype: object
  >>> s.str.get(1)
  0        t
  1        2
  2        b
  3      NaN
  4      NaN
  5    Hello
  dtype: object

Sum two series
~~~~~~~~~~~~~~
.. code:: python

  >>> a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
  >>> a
  a    1.0
  b    1.0
  c    1.0
  d    NaN
  dtype: float64
  >>> b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
  >>> b
  a    1.0
  b    NaN
  d    1.0
  e    NaN
  dtype: float64
  >>> a.add(b, fill_value=0)
  a    2.0
  b    1.0
  c    1.0
  d    1.0
  e    NaN
  dtype: float64

Drop elements by index
~~~~~~~~~~~~~~~~~~~~~~
.. code:: python

  >>> s = pd.Series(data=np.arange(3), index=['A','B','C'])
  >>> s
  A  0
  B  1
  C  2
  dtype: int64
  Drop labels B en C
  >>> s.drop(labels=['B','C'])
  A  0
  dtype: int64
