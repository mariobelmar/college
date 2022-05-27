==================================================
 Vim minimal toolkit for modern Data Scientist
==================================================

:Authors:
    Luis Belmar-Letelier <luis.belmar-letelier@mazars.fr>
:Version: 4.0 (2022/01)

:Training reviewer:
    Luis Belmar-Letelier <luis.belmar-letelier@mazars.fr>

Preliminaries
=============
Please install::

  $ sudo apt-get install klavaro ktouch wordwarvi

- It's a good time to learn Typing with `klavaro` and/or `ktouch`
- Play to `wordwarvi` without using arrows in your keybord, use j, k, l and h.
  Play untill you get a good score.
- Setup vim: Follow install from: https://doc.zettafox.com/Tool_linux_install.html#vim
- To play vim golf uses screenkey: `sudo apt-get install screenkey`

Vim basics
===========

4 Vim modes
---------------
There are 4 modes in Vim:

- Interactive mode: j, k, l, h to move around
- Insertion mode: **ESC+i**, **ESC+A**, capital **I** to insert on a block
  selection, **o** and **O** to enter in insert mode line below and line above
- Replace mode: **ESC+r**
- Command mode: starts with : (e.g. :w|!clear; make)

- Who to use this:

    - It it very important to understant that you have to stay most of the time
      on *Interactive mode*, the powerfull one.
    - Do not use the arrow keys, do not !
    - As soon as you are done with typing text hit ESC to come back to
      *Interactive Mode*

Manipulate text and move around
-----------------------------------

=================================================  ===================================================
Manipulate text                                    Move around
=================================================  ===================================================
**y**  - Copy (Yank)                               **h** - go left
**yy** - Copy the line                             **j** - go down
**P**  - Paste                                     **k** - go top
**d**  - delete the selection                      **l** - go right
**dd** - delete the line                           **0** and **$** - go to start/end of line
**dw** - delete a word                             **w** - go to the next word forward
                                                   **b** - go to the next word backward
**d4w** - delete 4 words                           **:33** :NUMBER - Reach the line's NUMBER
**d0** and **d$** - delete start/end the line      **/def m** reach the next python function
**x** - remove caracter under cursor                            starting by m
**e** - go to the end of the word or next word     **#** go forward to the next word similar to
**gUw** - capitalize the next word                       the one under the cursor **\*** backward
**.**   - repeate last action                      **f{char}** go next occurrence of {char} to the right
**u**   - undo                                     **F{char}** go next occurrence of {char} to the left
**Ctrl r** - redo                                  **t{char}** same than f{char} but do not include `char`
**<** indent left                                  **gv** select again last selected
**>** indent right
=================================================  ===================================================


==================== ============================================
 Block Manipulation  action
==================== ============================================
 **vit**             select block in tags e.g. <p>...
 **vat**             same including the tag *Visual Around Tag*
 **vib**             select `()` *visual in block*
 **viB**             select `{}` *visual in block*
 **vi[**             select `[]` *visual in block*
 **vi"**             select `""` *visual in block*
 **vi'**             select `''` *visual in block*
 **vis**             select `sentence`
 **vip**             select `paragraph`
 **cit**             Change in tag
 **dit**             delete in tag
 **yit**             yank in tag
==================== ============================================


Use visual mode to select/highligh a block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`vit` will select the inner most outer tag (Visual Inner Tag)::

  <h1><a href="https://re.fr"> https://re.fr</a></h1>
          ^
          |`vit` will select https://re.fr
          |`vat` will select <a href="https://re.fr"> https://re.fr</a>

Note about the::

  `vi{t,b,B,w,[,",',s,p}`.
   ^
   |_one of v (visual to select), y (to yank/copy), c (to change), > (to indent)

Pattern to act on a block of text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is very often not "needed to select something" to be able to act on it: the
change, delete and yank operators all work on text-objects and motions.

So `yit` in the following HTML text::

  <div>
    <p>
      ^cursor
      currsor
      Issues reported by division from the
      <a href="https://re.fr"> https://re.fr</a>
        they will create an issue.
    </p>
  </div>

You can do `yit` if you want to copy the content of that tag, `dit` if you
want to delete it or `cit` if you want to change it (been directly on input
mode). Depending the initial cursor position `vit` will capture the closest
outer tag.

Same with `vib` it will get all the function arguments with only 3 keystrokes::

  def show(self, name=Luis,
           a=33,
            ^cursor
           b=44,
           o='other'):
     return f'name: {name}, Age: {a+b}'

General pattern to select/act on a block of text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  `{v,c,d,y,>,<}{i,a}{t,b,B,w,[,",',`,s,p}
   ^            ^    ^
   |            |    |
   |            |    └--|one of `b` for () block, `B` for {} block `[` for [] block
   |            |       └- `s` for a sentance, `p` for a paragraph `"` for "" block
   |            └--|one of `a` or `i`, i for inner
   |               └-e.g. in case `dis` delete sentence without end sentence dot
   └-|one of `v` (visual to select), `y` (to yank/copy), `c` (to change),
     └-      `>` (to indent), ...

Application to [un-]comments python code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using the above, select tuples structures with `va(`, dictionaries with `va{`,
lists with `va[` or a block with `vip`.

Then to comment you can use `:norm i#` and uncoment with `:norm ^x`


More Vim
===========
Comment un-comment block
--------------------------
Comment a block e.g. the `def __init__` method:

.. code:: python

  class Pet(object):

    def __init__(self, name, food='eggs'):
      # name and food are instance variables
      self.name = name
      self.food = food

    show_msg = "I am {name}, a Pet, I eat {food}"

    def show(self, msg=None):
      ns = dict(name=self.name, food=self.food)
      print(Pet.show_msg.format(**ns))

Comment block
~~~~~~~~~~~~~~
To comment, from any place inside the ``__init__`` methode ``vip:norm i  #``::

  /init<enter>     => to go to `def __init__` line
  vip              => select e.g. the paragraphe
  :norm i    #     => apply line per line on normal mode insert `i    #`

Alternatives to `vip:norm i  #` can be:

- ``vip:norm lllli#``
- ``vip:g/    /norm lllli#``

un-comment block
~~~~~~~~~~~~~~~~~
To un-comment the block:

.. code:: python

  class Pet(object):

    # def __init__(self, name, food='eggs'):
    #   # name and food are instance variables
    #   self.name = name
    #   self.food = food

Use:

- ``vip:s/  #//``       or
- ``vip:norm ^xxxxx``   or
- ``vip:g/#/norm ^xx``

The `g/#/norm ^xx` correspond to the `g[lobal]/{pattern}/[cmd]` global pattern,
it means: for every line that match the pattern run the command, Cf.
:ref:`multi-repeate-the-power-of_g`.

Selection and Search
----------------------

Selection
~~~~~~~~~~
- **v** to select the cursor
- **V** to select lines
- **CTRL-v** to select blocks
   - use CTRL-v to select a block and "I" (MAJ-i) to repeat the insertion on the left.

Search
~~~~~~
- /pattern - search down the pattern, use **n** to move to the next occurence
  of the pattern.
- ?pattern - search up the pattern, you can use **n** here as well
- :%s/pattern/replace - search replace a pattern. The "%" is for all the document.
- :'<, >'s/pattern/replace - same for the selected area (with v, V or CTRL+v)

.. note::

  After doing a search in Vim, we get all the occurrences highlighted.
  To turn off highlighting until the next search use::

      :noh


Strip all trailing whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  :%s/ \s*$//e

  :%s to run :substitute over the range %, which is the entire buffer.
  `_\s*` to match a space followed by any number of whitespace characters.
  $ to anchor at the end of the line.
  The e flag to not give an error if there is no match (i.e. the file is
  already without trailing whitespace).

multiples space go CSV
~~~~~~~~~~~~~~~~~~~~~~~
Tranforme a file like this::

  C1       TEST   PROD
  A1    BE


  T1     B1

To a csv file like this::

  C1,TEST,PROD
  A1,BE
  T1,B1

Solution1::

  :%s/\s\{1,}/,/g

Solution2 in two steps (first delete blank lines)::

  :%g/^\s*$/d

Then use a substitution (``:s///``) over each line (``%``) to replace all
(``g``) continuous whitespace (``\s\+``) with a comma (``,``).::

  :%s/\s\+/,/g


.. note::

  To check you regexs you can use https://regex101.com/ or https://regexr.com/

Completion with words from the same buffer
-------------------------------------------
- In insert mode, **Ctrl-p** suggests completion with buffer words.
- Editing a python file (with .py extention).

Recording macros
-----------------
- **qa** says: let's start recording a macro on the letter a
- **q** says: let's stop recording and store it on letter "a"
- **ESC-@-a** execute the macro "a"
- **ESC-@-@** execute the last executed macro again

Adding a text on a rectangular selection
------------------------------------------
- **Ctrl-v** select where do you want to write your character
- **I**  write what do you want
- **ESC** then your character will appear after few sec

Fix problems with cut & paste
---------------------------------
If, when you cut & paste content from some other application, the content is
strangely pasted, use **u** to undo and call **:set paste** before the paste.
This will deactivate the autoindent (useful in python to autoindent code).
**:set nopaste** reverts the **:set paste**

Split screens
---------------
- **:split** - horizontal split the screen
   - ESC+CTRL+w - to switch from the actual window to the next one
- **:vsplit** - vertically split the screen
   - **:close** - close the window
   - **:only** - close all the other windows

You can cut (with **y**) and paste (with **P**) from one split window to another.

Call the bash with ``!``
--------------------------
- **:!tree**
   - "!" says "call the bash ``tree`` command"
- **:w|!tree -d**
   - "w|!" says "save the buffer and then call the bash"
- **:w|!clear; make**
   -  very useful pattern to save and execute

Write below the cursor the result of a bash call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  :r!tree -d

"**r**!" says "write below the cursor" the result of ``tree -d``

Introspection in python code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**ESC-m** to have an overview of functions, class and methods in python :

This will call the command::

  :!clear; grep -E "def |class " %

You can modify it, e.g. to see all the R functions.



Mandatory patterns to know
===========================

Reindent code
--------------

- Select a long line with **V**
- **gq** to reindent it

Sometimes, you will need to join lines first.
- **J** to join the actual line with the next one
- To reindent a block of 4 lines:

   - **JJJJ** to join lines, **V** to select it and then **gq**

Format json
------------
Reformat::

  :%!python -m json.tool

If you have instaled `jq` (`$ sudo apt-get install jq`) you can use too::

  :%!jq

To do this not on all the file but just a buch of json use `viB` this will select the
`{}` bloc and call `!python -m json.tool` on it.

Prettify columns data
----------------------

We want to convert this::

  N:F:C
  abcd:def:35644
  ab jkkbbc:def:43
  xga bc:def:9
  bonjour hbc:def:11

Into this::

  N            F    C
  abcd         def  35644
  ab jkkbbc    def  43
  xga bc       def  9
  bonjour hbc  def  11

Select lines with **V** then call the unix column **:'<,'>!column -ts:**.

Print a pygmentized content to pdf
------------------------------------

To create a PDF from code::

  :set background=light
  :hardcopy > out.ps|!ps2pdf out.ps
  :!evince out.pdf

.. _`multi-repeate-the-power-of_g`:

multi-repeate: The Power of `g`
---------------------------------
The `g/#/norm ^xx` correspond to

The `g/{pattern}/[cmd]` global pattern, means: for every line that match
the pattern run the command `cmd`.

.. note::

  ``v/{pattern}/[cmd]`` will apply `cmd` to all the lines that **do not match the
  pattern**

`g` to delete and copy lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For `[cmd]` we will use `d` to delete the lines, or `t$` to copy lines to the
end of document.

e.g to copy all Python functions and method to the end of the file::

  :%g/def /t$

e.g to delete all lines that contain "DEBUG" in a log file::

  :%g/DEBUG/d

Delete all lines that (don't) match a pattern::

  :g/pattern/d
  :g!/pattern/d

  e.g.
  :g/## Debug/d

Delete all blank lines::

  :g/^\s*$/d

Delete all empty lines::

  :g/^$/d

Remove duplicate blank lines::

  :%!cat -s

.. note::

  To remove ``^M`` you can use::

    :%s/{Ctrl+V}{Ctrl+M}//g

  # or, if ``dos2unix`` is installed::

    :%!dos2unix

`g` with normal commands
~~~~~~~~~~~~~~~~~~~~~~~~~
To execute a non-Ex command, you can use the :normal command:
`:g/pat/normal {commands}` e.g.:

To uppercase all lines that contain the "alert" word::

  :g/and/norm gU$

To apply macro `@a` to all lines that contain the "debug" word::

  :g/debug/norm @a

To add `]` at the end of all lines not matching a pattern::

  :v/pattern/s/$/]

  or

  :v/pattern/norm A]

Search and replace Patterns
------------------------------

Search and replace comma_not_followed_by_space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  :%s/,\(\S\)/, \1/gc

- With:

  - \\S matches any character that is not (whitespace, tab, ...)
  - But you need to capture the non-whitespace chain, in order to
    paste it one space further. This is what the **\\(** and **\\)** does.
  - You can then refer to it using **\\1** in the replacement.
  - So you match to some non-whitespace character **,\\S**
  - Then replace it with a comman and space **, ** followed by the captured character: **\1**.
  - **g** is to replace more than one line at a time.
  - **c** activates the confirm mode.

For exemple, this will transform::

  def(a,bof,c,dans)

Into::

   def(a, bof, c, dans)

Replace in a block selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``%s/\%V{pattern}/{string}/g``.

For example, just using **/\%V** in your pattern will change this (visual selection denoted by **\|**)::

  abc|defghi|jkl
  bcd|efghij|kla
  kla|bcdefg|hij

Into this::

  abc|defXYZ|jkl
  bcd|efXYZj|kla
  kla|bcdefg|hij

When you do::

  :%s/\%Vghi/XYZ/g

The main point is that you will ba able to change what is
in the selected block instead of what is in the entire page.

Use match group ``'\1'`` for advanced search/replace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If, from this starting point::

   datamod.predict(data)
   model.predict(mydata)
   model23.predict(data23)

We want::

   datamod.fit(data, target)
   model.fit(mydata, target)
   model23.fit(data23, target)

First, select the 3 lines with **ESC-V**, then call::

   :'<,'>s/predict(\(.*\))/fit(\1, target)/gc

- To get all arguments from predict(arguments), we use **.***
- To be able to re-use arguments as **\\1** in the replacement, we need to
  protect **.*** with **\\(** and **\\)**.

Copy all lines matching a pattern to the end of file
------------------------------------------------------
Use ``:g/pattern/t$``, e.g.::

  :g/def /t$

Increment series on lines **Ctrl-a** and **!nl -v starint**
---------------------------------------------------------------------------
`Ctrl-a` increment a number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Ctrl-a increment a number (you do not need to have cursor on the number)
  - Ctrl-x decrement a number

With the cursor on the `t` of top typing `Ctrl-a`::

   The top percent now own 42 percent of the national wealth.
       ^cursor

Increment 42 to 43::

   The top percent now own 42 percent of the national wealth.

`g Ctrl-a` cumulative increment on a selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- from the below select 3 last lines and call ``g Ctrl-a``::

    1 abc
    1 abc
    1 abc
    1 abc

we get::

    1 abc
    2 abc
    3 abc
    4 abc

Using call to bash for `!nl`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use bash ``nl -v12`` to add lines numbers in front of lines

Select these lines::

    1 abc
    1 abc
    1 abc
    1 abc

And call: **:!nl -v33** to produce::

    33	    abc
    34	    abc
    35	    abc
    36	    abc

Using a macro
~~~~~~~~~~~~~~~
To Write this::

  42 This is an item.
  43 This is an item.
  44 This is an item.
  45 This is an item.
  ...
  105 This is an item.

Let's start with::

  42 This is an item.

And then with the cursor on `4`, write the macro::

  qa
  yypCtrl-A
  q

Call the macro 62 times::

  62@a

As you saw just above the Ctrl-a command is very useful in a macro.  Example:
Use the following steps to make a numbered list::

  1. Create the first list entry, make sure it starts with a number.
  2. qa        - start recording into register 'a'
  3. Y         - yank the entry
  4. p         - put a copy of the entry below the first one
  5. CTRL-A    - increment the number
  6. q         - stop recording
  7. <count>@a - repeat the yank, put and increment <count> times

The very best using `:norm` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To go from this::

  test_values = (
      "hej.txt": "txt",
      "hej.html": "html",
      "hej.TxT": "TxT",
      "hej.TEX": "TEX",
      ".txt": "txt",
      ".html": "html",
      ".html5": "html5",
      ".x.yyy": "yyy",
  )


To this::

  test_values = (
     ("hej.txt", "txt"),
     ("hej.html", "html"),
     ("hej.TxT", "TxT"),
     ("hej.TEX", "TEX"),
     (".txt", "txt"),
     (".html", "html"),
     (".html5", "html5"),
     (".x.yyy", "yyy"),
  )

First select the all `( ... )` zone with *visual in block*::

  :vib

Then using normal, you can simply apply line-wise normal commands without
having to think about not getting into the next state)::

  :'<,'>norm f"hr($i)

Use plugings
=============

.. _`instal_plugings`:

Install plugings
-----------------
::

  $ touch ~/.vimrc; mv ~/.vimrc .vimrc_old
  $ cd ~ ; wget https://cdn-atlas.mazars.global/knowledge_data_advisory/fox_config_files/.vimrc
  $ curl -sfLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  $ vim
  $ # on vim run :PlugUpdate


Plug 'dhruvasagar/vim-table-mode'
----------------------------------
Let's convert in table this sort of files::

  N;F;C
  abcd;def;35644
  ab jkhbbc;def;43
  xga bc;def;9
  hello hbc;def;11

Select the paragraph with `vip` and call on it `:tableize/;`

We then get::

  | N           | F   | C     |
  | abcd        | def | 35644 |
  | ab jkhbbc   | def | 43    |
  | xga bc      | def | 9     |
  | hello hbc | def | 11    |

To have a full table we still have to specifiy the header and in some cases
row separation.

Toggle `vim-table-mode` with `\tm` and add a new line after the first one::

  | N           | F   | C     |
  ^
  | abcd        | def | 35644 |
  | ab jkhbbc   | def | 43    |
  | xga bc      | def | 9     |
  | gglkjlj hbc | def | 11    |

Because of the `\tm` mode now in insert mode double pipe `i||` will automaticly
add an header line.

If we are on a rst file the header will automaticly be `+====+====` and inner
lines will be `+----+----`::

  | N           | F   | C     |
  +=============+=====+=======+
  | abcd        | def | 35644 |
  ^||
  | ab jkhbbc   | def | 43 |
  +-------------+-----+----+
  | xga bc      | def | 9  |
  +-------------+-----+----+
  | gglkjlj hbc | def | 11 |
  +-------------+-----+----+


If we are on a markdown file (e.g. README.md) the header will be `|---|--`::

  | N           | F   | C     |
  |-------------|-----|-------|
  | abcd        | def | 35644 |
  | ab jkhbbc   | def | 43    |
  | xga bc      | def | 9     |
  | gglkjlj hbc | def | 11    |


What is super cool is that if you add content to a column automaticly column
width will adapt itself.

e.g if we replace `F` with `Full definition` automaticly the column will resize to::

  +-------------+-----------------+-------+
  | N           | Full definition | C     |
  +=============+=================+=======+
  | abcd        | def             | 35644 |
  | ab jkhbbc   | def             | 43    |
  | xga bc      | def             | 9     |
  | gglkjlj hbc | def             | 11    |
  +-------------+-----------------+-------+

On a column `\tdc` will insert a column and `\tic` will delete and insert a
column.

Work practices
================
Tasks
------

First, copy the practice data in a separate file  in the Tool_vim directory of
your training repository and open it with Vim.

- Move around in this practice without using arrows but only ``j k h l :12 and /``
- Remove all trailing spaces with a search/replace
- Fix comas_not_followed_by_space in the file
- Go in insert mode and start writing a word that already is in the buffer
  (like a function name), let the completion end the word.
- Use a macro to create correctly indented set_list, mydict, target_list
- Re-indent the line with mmodel (go to the line with /mmodel)
- Re-indent the full paragraph with "It is important to"
- Get a look on all class, method structure in the python code for the ``Pet`` class
- Create the same kind of search to catch R functions
- Create a PDF file from this file, download it and open it
- Create in restructured text syntax a block of code with the result of ``tree -d akd-doc``
- Write 'September in french' calendar with "nl -1" and Ctrl-v
- Write 'August in french' calendar with "Ctrl-v" and :put=range...
- Write lines with the IPs from 192.168.0.34 to 192.168.0.51
- Replace <p>stuff<\p> with  <pre class='code'>stuff</pre> with a regexps

Practice data::

   It is important to remove variables with no impact on the target in order to improve models performances,
   now we will use Decision Tree to get features importance and we will keep the higher ones.

   now some python code:

   import pandas as pd
   from sklearn.tree import DecisionTreeClassifier

   # Lets apply decision tree in order to get features impact
   mmodel = DecisionTreeClassifier(criterion='gini',max_depth=None,max_features=None).fit(titanic[titanic.columns.drop(['PassengerId','Survived'])],titanic.Survived)

   # the mmodel have a method called .feature_importances_ . But you have to transform the output in order to get it properly
   output = mmodel.feature_importances_
   output = pd.concat([pd.DataFrame(output), pd.Series(titanic.columns.drop(['PassengerId', 'Survived']))], axis=1)
   output.columns = ['importance', 'Vars']
   output = output.sort(['importance'], ascending = False)

   class Pet(object):
       # The constructor is methode named __init__
       def __init__(self, name, eat='eggs'):
           self.name = name
           self.eat = eat
       # show_msg is a Class variable
       show_msg = "I'm {} a Pet, I eat {}"
       # a class method is just a fonction with the self first variable
       def show(self, msg=None):
           if not msg:
               print Pet.show_msg.format(self.name, self.eat)
           else:
               print msg.format(self.name, self.eat)

   pets = [Pet(name) for name in ['Bob','Mick','Yan','Tony']]
   for pet in pets:
       pet.show()
       if len(pet.name) > 3:
           pet.eat = 'bacon'
           pet.show(' Hey now {} eat {}')

   write August in french with "Ctrl-v" and :put=range...
   =======================================================

   July in french

   1  mer juillet 2015
   2  jeu juillet 2015
   3  ven juillet 2015
   4  sam juillet 2015
   5  dim juillet 2015
   6  lun juillet 2015
   7  mar juillet 2015
   8  mer juillet 2015
   9  jeu juillet 2015
   10 ven juillet 2015
   11 sam juillet 2015
   12 dim juillet 2015
   13 lun juillet 2015
   14 mar juillet 2015

   August in french

   1 sam août 2015
   ...

   write September in french with "nl -1" and Ctrl-v
   ====================================================

   September in french

   1 mar septembre 2015
   ...

   Add 'm' in order to have 'my_array' with "Ctrl-v"
   ==================================================

      y_array[6] = 6
      y_array[7] = 7
      y_array[8] = 8
      y_array[9] = 9
      y_array[10] = 10
      y_array[11] = 11
      y_array[12] = 12
      y_array[13] = 13


   Write this my_array with a macro and "Ctrl-a"
   =============================================
   ::

      my_array[6] = 6
      my_array[7] = 7
      my_array[8] = 8
      my_array[9] = 9
      my_array[10] = 10
      my_array[11] = 11
      my_array[12] = 12
      my_array[13] = 13

   Start with::

      my_array[6] = 6

   From this set_list creat a list of words with a macro
   =======================================================

   set_list = ['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


   The list of word should look like this::

     __and__
     __class__
     __cmp__
     ...
     pop
     remove
     symmetric_difference
     symmetric_difference_update
     union
     update


   create a python target_list from a list of words
   =================================================
   With this input (list of words)::

      __and__
      __class__
      __cmp__
      __contains__
      __delattr__
      __doc__
      __eq__
      __format__
      __ge__
      __getattribute__
      __gt__
      __hash__
      __iand__
      __init__
      __ior__
      __isub__
      __iter__
      __ixor__
      __le__
      __len__
      __lt__
      __ne__
      __new__
      __or__
      __rand__
      __reduce__
      __reduce_ex__
      __repr__
      __ror__
      __rsub__
      __rxor__
      __setattr__
      __sizeof__
      __str__
      __sub__
      __subclasshook__
      __xor__
      add
      clear
      copy
      difference
      difference_update
      discard
      intersection
      intersection_update
      isdisjoint
      issubset
      issuperset
      pop
      remove
      symmetric_difference
      symmetric_difference_update
      union
      update

   Create ``target_list`` a python list (use a macro) correctly indented (use **J**, gqj and **:s/ $//g**)::

     target_list = ('__and__', '__class__', '__cmp__', '__contains__',
                    '__delattr__', '__doc__', '__eq__', '__format__', '__ge__',
                    '__getattribute__', '__gt__', '__hash__', '__iand__',
                    '__init__', '__ior__', '__isub__', '__iter__', '__ixor__',
                    '__le__', '__len__', '__lt__', '__ne__', '__new__',
                    '__or__', '__rand__', '__reduce__', '__reduce_ex__',
                    '__repr__', '__ror__', '__rsub__', '__rxor__',
                    '__setattr__', '__sizeof__', '__str__', '__sub__',
                    '__subclasshook__', '__xor__', 'add', 'clear', 'copy',
                    'difference', 'difference_update', 'discard',
                    'intersection', 'intersection_update', 'isdisjoint',
                    'issubset', 'issuperset', 'pop', 'remove',
                    'symmetric_difference', 'symmetric_difference_update',
                    'union', 'update']

   Create a python dict from a list of words
   =========================================
   From this list::

     append
     count
     extend
     index
     insert
     pop
     remove
     reverse
     sort

   Create mydict::

     mydict = {'key1': 'append',
               'key2': 'count,
               'key3':  ...}

   A first time using **Ctrl-v** and then a second time using a macro.

     'key1':'append
     'key2':'count
     'key3':'extend
     'key4':'index
     'key5':'insert
     'key6':'pop
     'key7':'remove
     'key8':'reverse
     'key9':'sort

     '1':'append
     '2':'count
     '3':'extend
     '4':'index
     '5':'insert
     '6':'pop
     '7':'remove
     '8':'reverse
     '9':'sort


   Use match group **'\1'** to replace <p> by <pre class=code>
   ==============================================================

   http://stackoverflow.com/questions/19189703/how-do-you-replace-the-content-of-html-tags-in-vim

   from this::

      <p>To Clone a gitolite Zettafox project using our private key authentification:</p>
      <p> bla bla bla bla and bla</p>

   create this::

     <pre class='code'>To Clone a gitolite Zettafox project using our private key
                       authentification:stuff</pre>
     <pre class='code'> bla bla
          bla bla and bla </pre>

   tips, use (to join lines)::

     J

   and then::

     :%s/<p>\(.*\)<\/p>/<pre class='code'>\1<\/pre>/g

  Convert this::

    test_values = (
        "hej.txt": "txt",
        "hej.html": "html",
        "hej.TxT": "TxT",
        "hej.TEX": "TEX",
        ".txt": "txt",
        ".html": "html",
        ".html5": "html5",
        ".x.yyy": "yyy",
    )

  Into this::

    test_values = (
       ("hej.txt", "txt"),
       ("hej.html", "html"),
       ("hej.TxT", "TxT"),
       ("hej.TEX", "TEX"),
       (".txt", "txt"),
       (".html", "html"),
       (".html5", "html5"),
       (".x.yyy", "yyy"),
    )

   JSON sample please reindent it with !python -m json.tool
   =========================================================

   { "glossary": { "title": "example glossary", "GlossDiv": { "title": "S", "GlossList": { "GlossEntry": { "ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup"}}}}}

   End of the Practice
   ===================
   please undo your modifications with::

   $ git checkout Tool_vim.rst

Todo
=====
- document: https://github.com/jvanja/vim-bootstrap4-snippets

Spell check
=============

For French on vim::

  :setlocal spell spelllang=fr

this will download dicts if not present

For English on vim::

  :setlocal spell spelllang=en

To deactivate the spellcheck::

  :setlocal spell!


A quick way to repeat a spelling correction::

    After making the first correction with ``z=``, e.g. teh to the, use
    ``:spellrepall``, or shorter: ``:spellr``.
