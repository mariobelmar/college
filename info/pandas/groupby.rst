.. use rst2html5 to create Slides
.. w|!clear; rst2html5 --deck-js --pretty-print-code --embed-content python_toolkit.rst> python_toolkit_slides.html

==========================================================
Python Pandas groupby a *split-apply-combine* strategy
==========================================================

:Authors:
    Luis Belmar-Letelier <lbelmarletelier@zettafox.com>,
:Version: 1.0 (2020/09)

:Training reviewer:
    Gilles Cuyaubère <gilles.cuyaubere@mazarsusa.com>,
    Nathali <nathali.paz-del-castillo@mazars.fr>,

.. raw:: latex

   \etocsettocstyle{}{}\localtableofcontents


.. _python_pandas_groupby:

- Groupby provide a **split-apply-combine** strategy
- By “group by” we are referring to a process involving one or more of the following steps:

    - Splitting the data into groups based on some criteria.
    - Applying a function to each group independently.
    - Combining the results into a data structure.


Some data
==========
Advanced introspection with groupby and pivot_table

.. code:: python

  import pandas as pd
  import numpy as np
  df = pd.DataFrame({'animal': 'cat dog fish fish dog cat cat'.split(),
                     'Size': list('SSMMMLL'),
                     'weight': [8, 10, 11, 1, 20, 12, 12]})
  df.loc[:, 'age'] = range(3, 10, 1)
  df.loc[:, 'length'] = np.linspace(30, 130, 7)
  df.columns = ['animal', 'Size', 'weight', 'age', 'length']
  df.loc[4, 'animal'] = None
  df.loc[2, 'Size'] = None
  df.loc[4, 'age'] = None
  df
  #     animal  Size  weight  age   length
  #  0     cat     S       8  3.0   30.000
  #  1     dog     S      10  4.0   46.667
  #  2    fish  None      11  5.0   63.333
  #  3    fish     M       1  6.0   80.000
  #  4    None     M      20  NaN   96.667
  #  5     cat     L      12  8.0  113.333
  #  6     cat     L      12  9.0  130.000

Housekeeping
-------------
.. code:: python

  # Use 3 decimal places in output display
  pd.set_option("display.precision", 3)

  # Don't wrap repr(DataFrame) across additional lines
  pd.set_option("display.expand_frame_repr", False)

  # Set max rows displayed in output to 25
  pd.set_option("display.max_rows", 25)

The fantastic ``Groupby``
============================
- ``groupby()`` method produce a ``DataFrameGroupBy`` instance:

.. code:: python

  df
  #     animal  Size  weight  age   length
  #  0     cat     S       8  3.0   30.000
  #  1     dog     S      10  4.0   46.667
  #  2    fish  None      11  5.0   63.333
  #  3    fish     M       1  6.0   80.000
  #  4    None     M      20  NaN   96.667
  #  5     cat     L      12  8.0  113.333
  #  6     cat     L      12  9.0  130.000

  gg = df.groupby('animal')
  gg
  # <pandas.core.groupby.DataFrameGroupBy object at 0x7fb9b2332190>

  df.groupby('animal').sum()
  #         weight   age   length
  # animal
  # cat         32  20.0  273.333
  # dog         10   4.0   46.666
  # fish        12  11.0  143.333

- ``DataFrameGroupBy`` provide numerical aggregation ``gg.mean()``, ``gg.sum()``, ...
  shortcuts to ``gg.agg('mean')``, ``gg.agg('sum')``, ...

.. code:: python

  df.groupby('animal').sum()
  #         weight   age   length
  # animal
  # cat         32  20.0  273.333
  # dog         10   4.0   46.666
  # fish        12  11.0  143.333

  df.groupby('animal').agg('sum')
  #         weight   age   length
  # animal
  # cat         32  20.0  273.333
  # dog         10   4.0   46.666
  # fish        12  11.0  143.333

  df.groupby('animal').agg(np.sum)
  #         weight   age   length
  # animal
  # cat         32  20.0  273.333
  # dog         10   4.0   46.666
  # fish        12  11.0  143.333

Multi-index groupby
--------------------
First argument can be a list of labels, then we get multi-indexes:

.. code:: python

  df.groupby(['animal', 'Size']).sum()

  #              weight   age   length
  # animal Size
  # cat    L         24  17.0  243.333
  #        S          8   3.0   30.000
  # dog    S         10   4.0   46.666
  # fish   M          1   6.0   80.000

Or real columns with ``as_index=False``:

.. code:: python

  df.groupby(['animal', 'Size'], as_index=False).sum()
  #   animal Size  weight   age   length
  # 0    cat    L      24  17.0  243.333
  # 1    cat    S       8   3.0   30.000
  # 2    dog    S      10   4.0   46.667
  # 3   fish    M       1   6.0   80.000

Note: ``as_index`` is equivalent ``reset_index`` on result:

.. code:: python

  df.groupby(['animal', 'Size']).sum().reset_index()

  #   animal Size  weight   age   length
  # 0    cat    L      24  17.0  243.333
  # 1    cat    S       8   3.0   30.000
  # 2    dog    S      10   4.0   46.667
  # 3   fish    M       1   6.0   80.000

Compare to ``crosstab`` and ``value_counts``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's compare to ``crosstab``:

.. code:: python

  pd.crosstab(index=df['animal'], columns=df['Size'])
  # Size    L  M  S
  # animal
  # cat     2  0  1
  # dog     0  0  1
  # fish    0  1  0

Let's compare to ``value_counts``:

.. code:: python

  df.Size.value_counts()
  # S    2
  # M    2
  # L    2
  # Name: Size, dtype: int64

  df.animal.value_counts()
  # cat     3
  # fish    2
  # dog     1
  # Name: animal, dtype: int64

  df.groupby('animal').size()
  # animal
  # cat     3
  # dog     1
  # fish    2
  # dtype: int64

Usually we want to rename agg columns
---------------------------------------
.. code:: python

  gg = df.groupby('animal', as_index=0)['age']
  gg.mean()  # here we would like the column be named `age_mean` not `age`
  #   animal Size  age
  # 0    cat    L  8.5
  # 1    cat    S  3.0
  # 2    dog    S  4.0
  # 3   fish    M  6.0

``gg.mean()`` return a DataFrame so we can just use ``rename``,

.. code:: python

  gg.mean().rename(columns=dict(age='age_mean'))
  #   animal Size  age_mean
  # 0    cat    L       8.5
  # 1    cat    S       3.0
  # 2    dog    S       4.0
  # 3   fish    M       6.0

But it's better to call ``.agg`` with a mapping:

.. code:: python

  gg.agg({"age_mean":np.mean})
  #   animal Size  age_mean
  # 0    cat    L       8.5
  # 1    cat    S       3.0
  # 2    dog    S       4.0
  # 3   fish    M       6.0

  gg.agg(dict(age_mean=np.mean))
  #   animal Size  age_mean
  # 0    cat    L       8.5
  # 1    cat    S       3.0
  # 2    dog    S       4.0
  # 3   fish    M       6.0

With ``agg`` we can create multiple aggregated named columns in one opperation:

.. code:: python

  gg.agg({'age_sum':np.sum, 'age_mean': np.mean})

  #   animal  age_sum  age_mean
  # 0    cat     20.0  6.666667
  # 1    dog      4.0  4.000000
  # 2   fish     11.0  5.500000


Applied functions
-----------------
.. code:: python

  gb = df.groupby('animal')
  gb.<tab>
  # gb.agg        gb.boxplot    gb.describe    gb.head     gb.mean
  # gb.aggregate  gb.corr       gb.diff        gb.hist     gb.median
  # gb.all        gb.corrwith   gb.dtypes      gb.idxmax   gb.min
  # gb.any        gb.count      gb.expanding   gb.idxmin   gb.name
  # gb.apply      gb.cov        gb.ffill       gb.indices  gb.ndim
  # gb.backfill   gb.cumcount   gb.fillna      gb.irow     gb.ngroups
  # gb.bfill      gb.cummax     gb.filter      gb.last     gb.nth
  # gb.cumsum     gb.cummin     gb.first       gb.length   gb.ohlc
  # gb.cumprod    gb.get_group  gb.mad         gb.pad      gb.size
  # gb.groups     gb.max        gb.pct_change  gb.skew
  # gb.plot       gb.std
  # gb.prod       gb.sum
  # gb.quantile   gb.tail
  # gb.rank       gb.take
  # gb.resample   gb.transform
  # gb.rolling    gb.tshift
  # gb.sem        gb.var
  # gb.shift      gb.weight


- ``skew``: For normally distributed data, the skewness should be about 0. A
  skewness value > 0 means that there is more weight in the left tail of the
  distribution
- ``quantile``: Default quantile is 0.5
- ``sem``: Calculates the standard error of the mean


Split-apply-combine pattern with ``transform``
================================================
While aggregation must return a reduced version of the data, we usualy have
then to merge to the original DataFrame, ``transform`` can return some
transformed version of the full data to recombine. For such a transformation,
the output is the same shape as the input.

Typical workflow: group by a category, compute a statistic on each group and
merge result to the original dataframe:

.. code:: python

  animals = ['cat', 'dog', 'fish', 'fish', "mouse", "cat", "cat"]
  df = pd.DataFrame({'animal': animals,
                     'Size': list('SSMMMLL'),
                     'weight': [8, 10, 11, 1, 5, 12, 10]})
  #     animal Size  weight
  # 0    cat    S       8
  # 1    dog    S      10
  # 2   fish    M      11
  # 3   fish    M       1
  # 4  mouse    M       5
  # 5    cat    L      12
  # 6    cat    L      10

Let's answer to the question "Is each animal heavier than the **average** in it's
**size** category".

We want to compute average weight in each Size category, merge it back into
orignal dataframe and compare weight to average weight for each animal

.. code:: python

  swa = df.groupby('Size', as_index=0)['weight'].agg({'s_weight_avg': np.mean})
  swa
  #   Size  s_weight_avg
  # 0    L        11.000
  # 1    M         5.667
  # 2    S         9.000

  df_avg = df.merge(swa, how="left", on="Size")
  df_avg
  #   animal Size  weight  s_weight_avg
  # 0    cat    S       8         9.000
  # 1    dog    S      10         9.000
  # 2   fish    M      11         5.667
  # 3   fish    M       1         5.667
  # 4  mouse    M       5         5.667
  # 5    cat    L      12        11.000
  # 6    cat    L      10        11.000

  df_avg.loc[:, "more_than_s_avg"] = df_avg.weight > df_avg.s_weight_avg
  df_avg
  #   animal Size  weight  s_weight_avg  more_than_s_avg
  # 0    cat    S       8         9.000            False
  # 1    dog    S      10         9.000             True
  # 2   fish    M      11         5.667             True
  # 3   fish    M       1         5.667            False
  # 4  mouse    M       5         5.667            False
  # 5    cat    L      12        11.000             True
  # 6    cat    L      10        11.000            False

Use ``transform`` to directIn a **more concise** way thanks to ``transform`` (avoid the ``df.merge`` with the
``groupby.mean``):

.. code:: python

  df
  #   animal Size  weight
  # 0    cat    S       8
  # 1    dog    S      10
  # 2   fish    M      11
  # 3   fish    M       1
  # 4  mouse    M       5
  # 5    cat    L      12
  # 6    cat    L      10

  df.loc[:, "s_weight_avg"] = df.groupby("Size")['weight'].transform("mean")
  df
  #     animal Size  weight  s_weight_avg
  # 0    cat    S       8         9.000
  # 1    dog    S      10         9.000
  # 2   fish    M      11         5.667
  # 3   fish    M       1         5.667
  # 4  mouse    M       5         5.667
  # 5    cat    L      12        11.000
  # 6    cat    L      10        11.000

  df_avg2 = df.copy()
  df_avg2.loc[:, "more_than_s_avg"] = df_avg2.weight > df_avg2.s_weight_avg
  df_avg2

  #   animal Size  weight  s_weight_avg  more_than_s_avg
  # 0    cat    S       8         9.000            False
  # 1    dog    S      10         9.000             True
  # 2   fish    M      11         5.667             True
  # 3   fish    M       1         5.667            False
  # 4  mouse    M       5         5.667            False
  # 5    cat    L      12        11.000             True
  # 6    cat    L      10        11.000            False

Note_1: The below forms are equivalent.

.. code:: python

  df.groupby('Size', as_index=0)['weight'].agg({'s_weight_avg': np.mean})

  #   Size  s_weight_avg
  # 0    L        11.000
  # 1    M         5.667
  # 2    S         9.000

  df.groupby('Size')['weight'].agg('mean').reset_index().rename(columns=dict(weight='s_weight_avg'))

  #   Size  s_weight_avg
  # 0    L        11.000
  # 1    M         5.667
  # 2    S         9.000

Note_2: you can use the **chained operation** notation like this:

.. code:: python

  (df.groupby('Size')['weight']
     .agg('mean')
     .reset_index()
     .rename(columns=dict(weight='s_weight_avg'))
  )

  #   Size  s_weight_avg
  # 0    L        11.000
  # 1    M         5.667
  # 2    S         9.000

Playing with Dates
===================
- The main idea here is to do groupby on timeseries data.
- The trivial way is to "manualy" create from the datetime columns, years,
  month, quaters, ... columns

  - it is much more efficient to use datetime type for date data present in
    your dateframe, to do that use at loading time:

      - ``pd.read_csv(infer_datetime_format=True``, # if dataframe is small
      - ``pd.read_csv(parse_dates=...``             # the one to use !
         * boolean. If True -> try parsing the index.
         * list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2,
           3 each as a separate date column.
         * list of lists. e.g.  If [[1, 3]] -> combine columns 1 and 3 and
           parse as a single date column.
         * dict, e.g. {'foo' : [1, 3]} -> parse columns 1, 3 as date and call
           result 'foo'
  - or after the initial load if you cast one or more columns as datetime with
    ``pd.to_datetime``
- The reason way it is the way to go is to take benefit of the very powerfull
  ``pd.Grouper(freq=...``

    =============== =============
    Freq String     Description
    =============== =============
    None            Generic offset class         defaults to absolute 24 hours
    'B'             business day (weekday)
    'C'             custom business day
    'W'             one week         optionally anchored on a day of the week
    'WOM'           the x-th day of the y-th week of each month
    'LWOM'          the x-th day of the last week of each month
    'M'             calendar month end
    'MS'            alendar month begin
    'BM'            usiness month end
    'BMS'           business month begin
    'CBM'           custom business month end
    'CBMS'          custom business month begin
    'SM'            5th (or other day_of_month) and calendar month end
    'SMS'           15th (or other day_of_month) and calendar month begin
    'Q'             calendar quarter end
    'QS'            alendar quarter begin
    'BQ             business quarter end
    'BQS'           business quarter begin
    'REQ'           retail (aka 52-53 week) quarter
    'A'             calendar year end
    'AS' or 'BYS    alendar year begin
    'BA'            usiness year end
    'BAS'           business year begin
    'RE'            etail (aka 52-53 week) year
    None            aster holiday
    'BH'            usiness hour
    'CBH'           custom business hour
    'D'             one absolute day
    'H'             one hour
    'T' or 'min'    ne minute
    'S'             one second
    'L' or 'ms'     one millisecond
    'U' or 'us'     one microsecond
    'N'             one nanosecond
    =============== =============

Cf. https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

Data with datetime columns
---------------------------
.. code:: python

  nb_rows = 100
  np.random.seed(0)

  Client = [f'c{i}' for i in np.random.randint(1, 10, size=nb_rows)]
  OrderDate = (pd.Series(pd.date_range('20210101',periods=365))
                 .sample(nb_rows, random_state=0).values)
  df = pd.DataFrame(dict(Client=Client,
                         Value=np.random.randint(10, 250, size=nb_rows),
                         OrderDate=OrderDate),
                    index=OrderDate)

  df.sort_values(['Client', 'OrderDate'], inplace=True)
  df
  #            Client  Value  OrderDate
  # 2021-01-06     c1    194 2021-01-06
  # 2021-01-08     c1     14 2021-01-08
  # 2021-01-21     c1    104 2021-01-21
  # 2021-02-19     c1    199 2021-02-19
  # 2021-03-10     c1     90 2021-03-10
  # ...           ...    ...        ...
  # 2021-05-23     c9     96 2021-05-23
  # 2021-06-23     c9     82 2021-06-23
  # 2021-07-11     c9    138 2021-07-11
  # 2021-09-21     c9     60 2021-09-21
  # 2021-10-23     c9    162 2021-10-23
  #
  # [100 rows x 3 columns]

Let's add, just to easy the visualisation, months indicators:

.. code:: python

  df.loc[:, 'month'] = df.OrderDate.dt.month.astype(str).str.zfill(2)
  df.loc[:, 'mth'] = df.OrderDate.dt.month_name().str.slice(0, 3)
  df.loc[:, ['mth', 'month', 'Client', 'Value']].head(4)

  #             mth month Client  Value
  # 2021-01-06  Jan    01     c1    194
  # 2021-01-08  Jan    01     c1     14
  # 2021-01-21  Jan    01     c1    104
  # 2021-02-19  Feb    02     c1    199
  df.shape
  # (100, 5)

It's easy to get sales per day:

.. code:: python

  df.groupby('OrderDate').sum().head(3)
  #               Value
  # OrderDate
  # 2021-01-06    194
  # 2021-01-07    237
  # 2021-01-08     14

But if we want **Value sales aggregated per month** ?

Use ``pd.Grouper()`` as ``groupby`` argument
------------------------------------------------
The modern way to answer the above question is:

1. check that we have a Date object as Index
2. give to ``groupby`` a ``pd.Grouper()`` instance

.. code:: python

  grouper = df.groupby(['Client', pd.Grouper(freq='M')])
  df.loc[:, 'sum_cN_month'] = grouper['Value'].transform(np.sum)
  df.loc[df.Client=='c5', :]
  #            Client  Value  OrderDate   sum_cN_month month  mth
  # 2021-02-26     c5     96 2021-02-26             96    02  Feb
  # 2021-03-05     c5    167 2021-03-05            167    03  Mar
  # 2021-04-25     c5     26 2021-04-25             26    04  Apr
  # 2021-06-09     c5    119 2021-06-09            395    06  Jun
  # 2021-06-14     c5     82 2021-06-14            395    06  Jun
  # 2021-06-20     c5    194 2021-06-20            395    06  Jun
  # 2021-07-19     c5     53 2021-07-19             53    07  Jul
  # 2021-08-02     c5    117 2021-08-02            461    08  Aug  # <=
  # 2021-08-08     c5    131 2021-08-08            461    08  Aug
  # 2021-08-09     c5     29 2021-08-09            461    08  Aug
  # 2021-08-28     c5    184 2021-08-28            461    08  Aug  # <=
  # 2021-09-22     c5     87 2021-09-22            325    09  Sep
  # 2021-09-27     c5    238 2021-09-27            325    09  Sep
  # 2021-12-09     c5    149 2021-12-09            149    12  Dec

  117+131+29+184
  # 461  # Bingo !

If we only need a groupby on one single Date column it is possible to use
``resample`` instead of ``groupby``.

e.g. let's sum on all months (cumulative on Client):

``df.resample`` a ``df.groupby`` for timeseries
-------------------------------------------------
We want to sum on Values by Month (no groupby on Client here).
Let's call it ``sum_month``

- We use ``df.resample`` to get the ``['Value'].sum()`` on ``OrderDate`` groupby.
- ``df.resample`` work like ``groupby`` but take from a DateTime ``df.index``
  timeseries abilities (the ``Freq String``) that's pretty cool.

.. code:: python

  sum_perM = df.resample('M', on='OrderDate')['Value'].agg(sum_month=np.sum)
  sum_perM
  #                  sum_month
  # OrderDate
  # 2021-01-31            1288
  # 2021-02-28             938
  # 2021-03-31            1382
  # 2021-04-30            1317
  # 2021-05-31            1575
  # 2021-06-30             477
  # 2021-07-31             568
  # 2021-08-31             951
  # 2021-09-30             891
  # 2021-10-31             798
  # 2021-11-30            1108
  # 2021-12-31             546

- To enrich the main ``df`` DataFrame we can do what we do with ``groupby``, use ``transform``.
   - So we avoid to have to create a join column (e.g. ``month``) and then to
     ``merge`` sum_perM with the initial ``df``.

   .. code:: python

      df.loc[:, 'sum_month'] = (df.resample('M', on='OrderDate')['Value']
                                  .transform(np.sum))

Limitations: no mix tuples -> use groupby with pd.Grouper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use ``df.groupby(['Client', pd.Grouper(freq='M')])`` to group on a mix of
timeseries and none timeseries columns.

Play with both, interest of ``cumcount``
------------------------------------------
Let's check that if we sum all Client values for a month ``sum_cN_month`` we get
back ``sum_month`` for the same month. e.g. ``df.month=='05``

.. code:: python

  df.loc[(df.month=='05')]
  #            Client  Value  OrderDate month  mth  sum_cN_month  sum_month
  # 2021-05-13     c1    242 2021-05-13    05  May           242       1575
  # 2021-05-05     c2     48 2021-05-05    05  May            48       1575
  # 2021-05-27     c4    127 2021-05-27    05  May           127       1575
  # 2021-05-17     c6    194 2021-05-17    05  May           342       1575
  # 2021-05-21     c6     20 2021-05-21    05  May           342       1575
  # 2021-05-25     c6    128 2021-05-25    05  May           342       1575
  # 2021-05-01     c7    158 2021-05-01    05  May           373       1575
  # 2021-05-03     c7    215 2021-05-03    05  May           373       1575
  # 2021-05-15     c8     51 2021-05-15    05  May           128       1575
  # 2021-05-16     c8     77 2021-05-16    05  May           128       1575
  # 2021-05-22     c9    219 2021-05-22    05  May           315       1575
  # 2021-05-23     c9     96 2021-05-23    05  May           315       1575

  df.loc[(df.month=='05')].sum_cN_month.to_list()
  # [242, 48, 127, 342, 342, 342, 373, 373, 128, 128, 315, 315]
  sum(_)
  # 3075   # not good we expect 1575  ;(

We need to take only one for each ``Client`` repetition, ``cumcount`` here is our
friend

.. code:: python

  df.loc[:, 'mC'] = df.groupby(['month', 'Client']).cumcount()

  (df.loc[(df.month=='05')]
     .loc[:, ['month', 'Value', 'sum_cN_month', 'sum_month', 'Client', 'mC']])
  #            month  Value  sum_cN_month  sum_month Client  mC
  # 2021-05-13    05    242           242       1575     c1   0
  # 2021-05-05    05     48            48       1575     c2   0
  # 2021-05-27    05    127           127       1575     c4   0
  # 2021-05-17    05    194           342       1575     c6   0
  # 2021-05-21    05     20           342       1575     c6   1
  # 2021-05-25    05    128           342       1575     c6   2
  # 2021-05-01    05    158           373       1575     c7   0
  # 2021-05-03    05    215           373       1575     c7   1
  # 2021-05-15    05     51           128       1575     c8   0
  # 2021-05-16    05     77           128       1575     c8   1
  # 2021-05-22    05    219           315       1575     c9   0
  # 2021-05-23    05     96           315       1575     c9   1

  df.loc[(df.month=='05') & (df.mC==0)].sum_cN_month.to_list()
  # [242, 48, 127, 342, 373, 128, 315]

  sum([242, 48, 127, 342, 373, 128, 315])
  # 1575  # Bingo !

Exercises
=========
Please commit your code in a separate file
``<your_name>_Python_pandas_groupby.rst`` in the Python_pandas directory of your
training repository.

The data:

.. code:: python

  emp = pd.DataFrame({'Code': [1232, 4234, 4213, 3123, 4221, 5123, 1233,
                               2231, 4320, 3322],
                      'Role': ['Engineer', 'Engineer', 'Engineer', 'Engineer',
                               'Artist', 'Artist', 'Artist',
                               'Manager', 'Manager', 'Manager'],
                      'Name': ['Becky', 'Dan', 'Sharon', 'Scott', 'Daria', 'Jacob',
                               'Tylar', 'Brandon', 'Shirlee', 'Becky'],
                      'Building': ['A', 'A', 'B', 'C', 'B',  'C', 'C', 'A', 'B', 'C'],
                      'Years_employed': [3, 2, 3, 1, 2, 1, 2, 5, 4, 4]},
                      columns=['Code', 'Role', 'Name', 'Building', 'Years_employed'])
  daily = pd.DataFrame({'Day':['2017-11-01', '2017-11-01', '2017-11-01',
                               '2017-11-01', '2017-11-01', '2017-11-01',
                               '2017-11-01', '2017-11-01', '2017-11-01',
                               '2017-11-01', '2017-11-02', '2017-11-02',
                               '2017-11-02', '2017-11-02', '2017-11-02',
                               '2017-11-02', '2017-11-02', '2017-11-02',
                               '2017-11-02', '2017-11-02', '2017-11-03',
                               '2017-11-03', '2017-11-03', '2017-11-03',
                               '2017-11-03', '2017-11-03', '2017-11-03',
                               '2017-11-03', '2017-11-03', '2017-11-03'],
                        'Code':[1232, 4234, 4213, 3123, 4221, 5123, 1233,
                                2231, 4320, 3322, 1232, 4234, 4213, 3123,
                                4221, 5123, 1233, 2231, 4320, 3322, 1232,
                                4234, 4213, 3123, 4221, 5123, 1233, 2231,
                                4320, 3322],
                        'Hours': [6,7,7,8,8,6,6,7,8,10,7,6,8,8,8,6,7,8,8,9,
                                  8,6,7,7,7,8,7,8,8,9]},
                       columns=['Day', 'Code', 'Hours'])

  emp
  #    Code      Role     Name Building  Years_employed
  # 0  1232  Engineer    Becky        A               3
  # 1  4234  Engineer      Dan        A               2
  # 2  4213  Engineer   Sharon        B               3
  # 3  3123  Engineer    Scott        C               1
  # 4  4221    Artist    Daria        B               2
  # 5  5123    Artist    Jacob        C               1
  # 6  1233    Artist    Tylar        C               2
  # 7  2231   Manager  Brandon        A               5
  # 8  4320   Manager  Shirlee        B               4
  # 9  3322   Manager    Becky        C               4

  daily
  #            Day  Code  Hours
  # 0   2017-11-01  1232      6
  # 1   2017-11-01  4234      7
  # 2   2017-11-01  4213      7
  # 3   2017-11-01  3123      8
  # 4   2017-11-01  4221      8
  # ..         ...   ...    ...
  # 25  2017-11-03  5123      8
  # 26  2017-11-03  1233      7
  # 27  2017-11-03  2231      8
  # 28  2017-11-03  4320      8
  # 29  2017-11-03  3322      9
  #
  # [30 rows x 3 columns]


1. Sort employees by Years_employed.

2. For each role, find the average number of years.

3. Find the total number of employes in each building.

4. How many hours has worked each employee in total ?

5. How many hours in average has worked each employee ?

6. Add to emp dataframe, the min, max, mean, total hours worked in this period.

7. Return a dataframe with this structure:

   For each day how many employees have worked  8 hours (normal_hours),
   less than 8 hrs (min_hours) and greater than 8 hrs (extra_hours)

   - For example:

      .. code:: python

                 Day Normal_Hours  Min_Hours  Extra_Hours
          2017-11-01            3          6            1

8. Determine for each employee if he has been employed less than the average in
   his role (2 methods)

9. did a person, per building had the same role the last employed ?

  Determine for each employee if he has the same role as the last employed
  person of the building -- Tips: use indexing dataframe and idxmin

10. Sales in 3 shops around 3 Categories

  - ``shop`` Dataframe is:

    .. code:: python

       shop = pd.DataFrame({'Item': ['Shoes', 'TV', 'Book', 'Phone', 'DVD', 'Skirt',
                                     'Shirt', 'Comic', 'Magazine', 'Pants'],
                            'Shop1': [45, 200, 20, 300, 100, 50, 40, 5, 4, 60],
                            'Shop2': [50, 300, 17, 350, 90, 55, 44, 4, 4, 55],
                            'Shop3': [53, 250, 21, 400, 85, 52, 38, 4, 3, 58],
                            'Category': ['Clothes', 'Technology', 'Books',
                                         'Technology', 'Technology', 'Clothes',
                                         'Clothes', 'Books', 'Books', 'Clothes']},
                            columns=['Item', 'Shop1', 'Shop2', 'Shop3', 'Category'])
  - Add a column to the shop dataframe that contains the number of items in
    each category,
  - Create a new column named ``cumCat`` which contains the cumulated count of
    categories (obtained with a ``groupby`` strategy),
  - For each shop_{i}, create a ``mean_s{i}`` a column containing the average amount of items
    per category,
  - For each item in shop 1, create a column ``sumS1`` which contains the total
    amount of items per category and a column ``perc1`` which contains the
    pourcentage of the total amount of items that represents each item in its
    own category.

.. 1
.. shop.loc[:, 'ItCatCount'] = shop.groupby('Category')['Item'].transform('count')
.. 2
.. shop = shop.sort_values('Category')
.. shop.loc[:, 'cumCat'] = shop.groupby('Category')['Item'].transform('cumcount')
.. 3
.. shop.loc[:, 'mean_s1'] = shop.groupby('Category')['Shop1'].transform('mean')
.. 4
.. shop.loc[:, 'sumS1'] = shop.groupby('Category')['Shop1'].transform('sum')
.. shop.loc[:, 'perc1'] = shop.loc[:, 'Shop1'] / shop.loc[:, 'sumS1']

Bibliography
=============

- https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

