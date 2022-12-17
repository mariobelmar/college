How to create Pandas dataframe to test/play_with ?
====================================================

``pandas.util.testing`` has plenty makeXXXDataframeYYY
------------------------------------------------------

Genarate a random ``DataFrame`` with object columns:
.. code:: python

    from pandas.util.testing import makeCustomDataframe
    df = makeCustomDataframe(7, 3); df.reset_index(drop=True, inplace=True)
    df

That can be a good starting point, to add specific columns type with e.g. ``np.random.randint``.

Add a ``num`` column:
.. code:: python

    df.loc[:, 'num'] = np.random.randint(9, 99, 7); df
    df.dtypes

add a ``timeserie`` column:
.. code:: python

    from pandas.util.testing import makeTimeSeries
    makeTimeSeries(7, 'M')
    df.loc[:, 'ts'] = makeTimeSeries(7, 'M').index.to_list()
    df.dtypes

add some NaN values:
.. code:: python

    odd_filter = df.num%2 != 0
    df.loc[odd_filter, 'C_l0_g1'] = np.nan
    df

Get pandas sample:
.. code:: python

    from pandas.util.testing import makeMixedDataFrame
    df = makeMixedDataFrame()
    df
    #      A    B     C          D
    # 0  0.0  0.0  foo1 2009-01-01
    # 1  1.0  1.0  foo2 2009-01-02
    # 2  2.0  0.0  foo3 2009-01-05
    # 3  3.0  1.0  foo4 2009-01-06
    # 4  4.0  0.0  foo5 2009-01-07

Cast float as int:
.. code:: python

    df.loc[:, 'B'] = df.B.astype(int)
    df
    #      A  B     C          D
    # 0  0.0  0  foo1 2009-01-01
    # 1  1.0  1  foo2 2009-01-02
    # 2  2.0  0  foo3 2009-01-05
    # 3  3.0  1  foo4 2009-01-06
    # 4  4.0  0  foo5 2009-01-07

You can use list of list and ``columns=`` to create a sample dataframe
----------------------------------------------------------------------
Alternative to create the ``DataFrame``:

.. code:: python

  df = pd.DataFrame([
    'cat 5 M'.split(),
    ['dog', ' ', 'F'],
    ' 3 M'.split(sep=' '),
    'cow 7 M'.split()
  ], columns=list('abc'))

  df
  #      a  b  c
  # 0  cat  5  M
  # 1  dog     F
  # 2       3  M
  # 3  cow  7  M

The same using ``DataFrame(dict())``
------------------------------------
.. code:: python

    np.random.seed(42)
    df = pd.DataFrame(dict(
        n='bat cat caw dog fly ant'.split(),
        f=list('ynnnyn'),
        paw=[4,4,4,4,6,8],
        sex=list('FMFMFF'),
        date=pd.date_range(start='2022/08/01', freq='3w-MON', periods=6),
        cnt=np.random.randint(1, 99, 6),))

    df = df.astype(dict(n='category'))
    df
    #      n  f  paw sex       date  cnt
    # 0  bat  y    4   F 2022-08-01   52
    # 1  cat  n    4   M 2022-08-22   93
    # 2  caw  n    4   F 2022-09-12   15
    # 3  dog  n    4   M 2022-10-03   72
    # 4  fly  y    6   F 2022-10-24   61
    # 5  ant  n    8   F 2022-11-14   21

    df['year_w'] = df.date.dt.weekofyear
    df['Q'] = df.date.dt.quarter
    df
    #      n  f  paw sex       date  cnt  year_w  Q
    # 0  bat  y    4   F 2022-08-01   52      31  3
    # 1  cat  n    4   M 2022-08-22   93      34  3
    # 2  caw  n    4   F 2022-09-12   15      37  3
    # 3  dog  n    4   M 2022-10-03   72      40  4
    # 4  fly  y    6   F 2022-10-24   61      43  4
    # 5  ant  n    8   F 2022-11-14   21      46  4

We have in a few lines of code a Dataframe with all types of columns:

.. code:: python

    df.dtypes
    # n               category
    # f                 object
    # paw                int64
    # sex               object
    # date      datetime64[ns]
    # cnt                int64
    # year_w             int64
    # Q                  int64

Prefer the compact Dataframe creation with ``StringIO``
---------------------------------------------------------
To forge short dataframe to test something and/or submit a stackoverflow question use
``StringIO`` this allow to keep in 20 lines of python code the structure you need.

.. code:: python

  from io import StringIO
  data = StringIO("""
  n,f,paw,sex,cnt
  bat,y,4,F,52
  cat,n,4,M,93
  caw,n,4,F,15
  dog,n,4,M,72
  fly,y,6,F,61
  ant,n,8,F,21""")
  df = pd.read_csv(data, dtype=str)
  df
  #      n  f paw sex cnt
  # 0  bat  y   4   F  52
  # 1  cat  n   4   M  93
  # 2  caw  n   4   F  15
  # 3  dog  n   4   M  72
  # 4  fly  y   6   F  61
  # 5  ant  n   8   F  21

.. note::

  use ``data.seek(0)`` to be able to reuse ``StringIO`` data

.. code:: python

  # make name categories
  df['n'] = df.n.str.strip().astype('category')

  # allow to do arithmetics on numbers
  df = df.astype(dict(paw='int', cnt='int'))
  df.dtypes
  # n      category
  # f        object
  # paw       int64
  # sex      object
  # cnt       int64
  # dtype: object

.. important::

  To have an "automatic" type cast we could use ``read_csv(date)`` without the
  ``dtype=str`` option, this can be usefull in a toy sample, but is "forbiden" in real
  life data loading, where we need to keep a very explicit control on every column
  type/Nas, ...

Use StringIO to play with NaN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from io import StringIO
    data = StringIO("""
    a  ,n,s
    cat,5,M
    dog, ,F
       ,3,M
    cow,7,M""")
    df = pd.read_csv(data, dtype=str)

    df.isna()
         a        n      s
    0  False  False  False
    1  False  False  False
    2  False  False  False
    3  False  False  False

We notice that ``a`` column has spaces and line 2 is non empty:

.. code:: python

    df.to_records()
    rec.array([(0, 'cat', '5', 'M'), (1, 'dog', ' ', 'F'),
               (2, '   ', '3', 'M'), (3, 'cow', '7', 'M')],
              dtype=[('index', '<i8'), ('a  ', 'O'), ('n', 'O'), ('s', 'O')])

So e.g. ``df.a[0]`` will trigger an Error.

.. code:: python

    df.columns
    # Index(['a  ', 'n', 's'], dtype='object')
    #          ^^ warning trailing spaces

not very good fix:

.. code:: python

    df.columns = [c.strip() for c in df.columns]  # not good
    df.columns
    # Index(['a', 'n', 's'], dtype='object')

Good fix (use Pandas ``str`` API):

.. code:: python

    df.columns = df.columns.str.strip()
    df.columns
    # Index(['a', 'n', 's'], dtype='object')

So back to our stuff, we want to have real NAs:

.. code:: python

    from io import StringIO
    data = StringIO("""
    a  ,n,s
    cat,4,M
    dog, ,F
       ,3,M
    cow,7,M""")
    df = pd.read_csv(data, dtype=str)
    df.columns = df.columns.str.strip()

In case what we want is ``[' ', '', '\s*']`` to be NaNs:

.. code:: python

    df.isna()
    #      a        n      s
    # 0  False  False  False
    # 1  False  False  False
    # 2  False  False  False
    # 3  False  False  False

    df
    #      a  n  s
    # 0  cat  5  M
    # 1  dog     F
    # 2       3  M
    # 3  cow  7  M

    df.a.to_list()
    # ['cat', 'dog', '  ', 'cow']

    df.a.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df.a.to_list()
    # ['cat', 'dog', nan, 'cow']

    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df
    #      a    n  s
    # 0  cat    5  M
    # 1  dog  NaN  F
    # 2  NaN    3  M
    # 3  cow    7  M

To see ``df.n`` as an ``Int64`` column with Nas:

.. code:: python

    # We used to have a TypeError when converting from object to Int64.
    # Since recently, it now possible to use it
    df.n.astype('Int64')
    # 0       5
    # 1    <NA>
    # 2       3
    # 3       7
    # Name: n, dtype: Int64


    # As not every pandas library is up-to-date, here is the old way 
    df.n.astype('Int64')
    # TypeError      Traceback ...
    # TypeError: object cannot be converted to an IntegerDtype

    df.n.to_list()
    # ['4', nan, '3', '7']

We need to first convert ``strings`` as ``float`` and then as ``Int64``:

.. code:: python

    df.n.astype(float)
    # 0    4.0
    # 1    NaN
    # 2    3.0
    # 3    7.0
    # Name: n, dtype: float64

    df.n.astype(float).astype('Int64')
    # 0       4
    # 1    <NA>
    # 2       3
    # 3       7
    # Name: n, dtype: Int64

    # Bingo !!

One more exemple with NAs
--------------------------

.. code:: python

    from io import StringIO
    data = StringIO("""
      n, f, paw, sex, cnt
    bat, y,   4,   F,  52
    cat, n,   4,   M,  93
    caw, n,   4,   F,  15
    dog, n,   4,   M,  72
    fly, y,   6,   F,  61
    ant, n,   8,   F,  21""")
    df = pd.read_csv(data, dtype=str)
    df['paw'] = df.paw.astype('int')

    df.to_records()         # we need to strip
    # rec.array([(0, 'bat', ' y', 4, '   F', '  52'),
    #            (1, 'cat', ' n', 4, '   M', '  93'),
    #            (2, 'caw', ' n', 4, '   F', '  15'),
    #            (3, 'dog', ' n', 4, '   M', '  72'),
    #            (4, 'fly', ' y', 6, '   F', '  61'),
    #            (5, 'ant', ' n', 8, '   F', '  21')],
    #           dtype=[('index', '<i8'), ('n', 'O'), ('f', 'O'), ('paw', '<i8'),
    #                  ('sex', 'O'), ('cnt', 'O')])

    df.columns = df.columns.str.strip()  # to strip columns names first

To strip all the cells:

.. code:: python

    cols_obj = df.select_dtypes('object').columns
    df[cols_obj] = df[cols_obj].apply(lambda x: x.str.strip())
    df.to_records()  # fixed no more spaces to strip
    # rec.array([(0, 'bat', 'y', 4, 'F', '52'),
    #            (1, 'cat', 'n', 4, 'M', '93'),
    #            (2, 'caw', 'n', 4, 'F', '15'),
    #            (3, 'dog', 'n', 4, 'M', '72'),
    #            (4, 'fly', 'y', 6, 'F', '61'),
    #            (5, 'ant', 'n', 8, 'F', '21')],
    #       dtype=[('index', '<i8'), ('n', 'O'), ('f', 'O'),
    #              ('paw', '<i8'), ('sex', 'O'), ('cnt', 'O')])

fillna for int, float, ...
==========================
.. code:: python

  from io import StringIO
  data = StringIO("""
  i,fff
  1,3.2
  2,3.3
  3,3.4
  4,3.5
  5,3.6
  6,3.7""")
  df = pd.read_csv(data)
  df
  df.dtypes

Now let's put some NAs in both this int and float column:

.. code:: python

  from io import StringIO
  data = StringIO("""
  i,fff
  1,3.2
  2,
  ,
  4,3.5
  5,3.6
  6,3.7""")
  df = pd.read_csv(data)
  df
  #      i  fff
  # 0  1.0  3.2
  # 1  2.0  NaN
  # 2  NaN  NaN
  # 3  4.0  3.5
  # 4  5.0  3.6
  # 5  6.0  3.7

  df.dtypes
  # i      float64
  # fff    float64
  # dtype: object

.. Warning::

   Pandas convert as ``float`` an ``int`` column with NAs !


If we try to convert to ``int`` that will fail:

.. code:: python

  df.i.astype(int)
  # IntCastingNaNError ...
  # IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer

But using the very last Pandas 1.x.x ``Int64Dtype()`` that will work::

  df.i.astype(pd.Int64Dtype())
  # 0       1
  # 1       2
  # 2    <NA>
  # 3       4
  # 4       5
  # 5       6
  # Name: i, dtype: Int64

Let's make this persistant:

.. code:: python

  df.loc[:, 'i'] = df.i.astype(pd.Int64Dtype())
  df
  #       i  fff
  # 0     1  3.2
  # 1     2  NaN
  # 2  <NA>  NaN
  # 3     4  3.5
  # 4     5  3.6
  # 5     6  3.7

  df.dtypes
  # i        Int64
  # fff    float64
  # dtype: object

.. Note::

  You can use the shortcut ``Int64`` to replace ``pd.Int64Dtype()``

  .. code:: 

    df.loc[:, 'i'] = df.i.astype('Int64')

