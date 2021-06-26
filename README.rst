Les trucs informatiques et plus de Mario

Git
====

- Use ``tig`` to inspect git tree
- Use::

     git commit -am 'commit message' to create commit

- Use ``git push`` to push/sent the commit to the server

to know list of files versioned (or not) by git use ``ls-files``::

  git ls-files
  git ls-files -o

to add a file e.g. ``quiksort.py`` to git repository::

  git add quiksort.py
  git commit -am 'add quiksort.py'
  git push

