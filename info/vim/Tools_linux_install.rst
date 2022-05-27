========================================
 Install Your DataScience Ubuntu Laptop
========================================
:Authors:
    Luis Belmar-Letelier <lbelmarletelier@zettafox.com>,
:Version: 2020/07

:Training reviewer:
    Luis Belmar-Letelier <lbelmarletelier@zettafox.com>,

Install Linux
==============

In order to install Ubuntu, you need to have a bootable USB key : a USB key
that your BIOS will recognize and that contain the necessary data to install
Ubuntu on your machine.

Once you've created your bootable USB key as explained below, reboot on it
(enter the BIOS and choose your USB key to install Ubuntu)

The way to enter the BIOS depends only on your machine, look for informations
on Google or on the website of your machine's constructor.

WARNING
You will have to choose a password, pay a close attention to the configuration
of your keyboard (QWERTY, AZERTY, BEPO...). It is a common mistake to type your
password with a wrong keyboard configuration, which makes it almost impossible
to find back. If you cannot find back your password you will have to reinstall
Ubuntu from scratch and lose a lot of your precious time.  Hint : type a first
password only using keys common to both QWERTY and AZERTY to avoid mistyping,
and change it later when you are sure of your password.

Create a bootable USB key on Linux
----------------------------------
Download the .iso here https://www.ubuntu.com/download/desktop and install it
with ``dd``::

  # dd if=/ubuntu-20.04-desktop-amd64.iso of=/dev/sdb

On the target laptop, enter in bios and set Legacy boot and USB boot first.

Finally, reboot on USB key.

If it doesn't work try ''F12'' while your computer is rebooting, and select the USB key.

Install Ubuntu
----------------
- choose to cypher the disque (not the home folder)

   - choose VLM when formating the DD
- choose a short name for your laptop (no more than 8 digits)

Install software stack
========================

Update remote packages repositories
------------------------------------
Before doing any installation, you have to make sure everything is
up to date::

  sudo apt-get update

Apt-get to install software stack
-----------------------------------

The aim of this part is for you to install and understand what each package will be used for.

Manipulate images and pdf::

  apt-get install geeqie gimp qpdf unoconv pdfposter imagemagick
  apt-get install inkscape

  # # to advanced screenshot: shutter

  sudo add-apt-repository -y ppa:shutter/ppa
  sudo apt-get update
  apt install shutter

To configure Shutter as the default tool to take screenshots with when you
press PrtSc or Alt+PrtSc:
https://shutter-project.org/faq-help/set-shutter-as-the-default-screenshot-tool

.. rsvg-convert -f pdf -o page1.pdf page1.svg
.. https://forum.ubuntu-fr.org/viewtopic.php?id=1628301
.. pdfposter  myuses.pdf out.pdf -p1x3a4
.. dot -Tsvg a.dot > myuses.svg; eog myuses.svg
.. inkscape myuses.svg
.. https://designer.io/#download

Network tools::

  apt-get install wget rsync ncftp openssh-client
  apt-get install dnsutils net-tools

git tools::

  apt-get install git gitg gitk tig

Files tools::

  apt-get install terminator tree htop ncdu p7zip-full pigz tar unzip
  apt-get install texlive-extra-utils

date tools::

  apt-get install gcal
  gcal -s1 -K 2018
  echo "alias gcal='gcal -s1 -K '" >> ~/.bashrc

Set up config file for terminator::

  cd ~/.config/terminator && rm -r *
  wget https://cdn-atlas.mazars.global/knowledge_data_advisory/fox_config_files/.config/terminator/config

Python tools::

  apt-get install python3-venv python3-dev python3-pip
  pip3 install jupyter --user

Install Python documentation::

 apt-get install python-sklearn-doc \
                 python-flask-doc python-gevent-doc python-jinja2-doc  \
                 python-ipython-doc python-matplotlib-doc python-scipy-doc

Vim::

  apt-get install vim-common wordwarvi

Virtualbox::

  apt-get install virtualbox virtualbox-guest-additions-iso

Skype::

  wget -q https://repo.skype.com/data/SKYPE-GPG-KEY -O- | sudo apt-key add -
  echo "deb [arch=amd64] https://repo.skype.com/deb stable main" | sudo tee /etc/apt/sources.list.d/skypeforlinux.list
  sudo apt update
  sudo apt install skypeforlinux


Media codecs and fonts: (MP3, MS Web fonts, LAME)::

  apt-get install ubuntu-restricted-extras
  # see https://help.ubuntu.com/community/RestrictedFormats/PlayingDVDs

VD-Video playing library::

  # sudo apt install libdvd-pkg && sudo dpkg-reconfigure libdvd-pkg

NodeJS 14.x LTS (jusque Avril 2023)::

  wget -qO- https://deb.nodesource.com/setup_14.x | sudo -E bash -
  sudo apt install nodejs npm

Mermaid-CLI (a powerful programmatic diagram tool, see :
https://mermaid-js.github.io/mermaid/#/)::

  npm install -g npm  # npm update
  npm install -g @mermaid-js/mermaid-cli
  mmdc -h  # If error, perform the following command
  # sudo ln -s ~/.node_modules/.bin/mmdc /usr/bin/mmdc

Decktape (a PDf generator for impress-based webpages)

.. code:: shell

    npm install -g decktape
    decktape -h  # If error, perform the following command
    # sudo ln -s $(npm -g root)/../../bin/decktape /usr/bin/decktape

VPN ACCESS
==================

Client installation
-------------------------

VPN is used to access servers remotly (outside mazars network).

First install F5 client::

  $ wget https://fox:gae3tazktYuFie4@files.zettafox.com/vpn/linux_f5vpn.x86_64.deb
  $ sudo dpkg -i linux_f5vpn.x86_64.deb

Then access https://vpnssl.mazars.fr/my.policy. Using the following
credentials.

 * login: name.surname

 * Password: Your Mazars Password

.. image:: ./Tools_linux_install/f5vpn.png

.. image:: ./Tools_linux_install/f5vpn2.png

You should now able to access the Bastion.

SSH key
----------

Once you get this done please add this configuration to your
~/.ssh/config(Please change the `IdentityFile` path by the new key you receive)
get this result **Please make sure your keys have the correct permissions which
is 600** ($ chmod 600 path_to_your_private_key )::

  host bastion bastion.mazars.fr
     hostname bastion.mazars.fr
     User YOUNAME.SURNAME (With - if it's a compose surname Exception for Luis
     who should use luis)
     IdentityFile ~/.ssh/XXXTOBECHANGEXXX
     ForwardAgent yes

Reminder **ADD your key to your agent**::

  $ ssh-add /path_To_your_agent

Once this is done please launch the VPN and try to ssh the bastion you should
get this result ::

  (venv) baptiste@euler:~/ssh_fox$ ssh bastion.mazars.fr
  AVERTISSEMENT :
  L’accès à ce système est restreint et réservé aux seuls utilisateurs dûment
  autorisés. Toute tentative d’accès sans autorisation ou de maintien
  frauduleux dans ce système fera l’objet de poursuites judiciaires.  Tout
  utilisateur dûment autorisé à accéder au système est d’ores et déjà informé
  et reconnaît que ses actions sont susceptibles d’être enregistrées,
  conservées et auditées.


  Account successfully checked out

  Connexion à baptiste@local@vm131.zettafox.com:SSH...

  Vous êtes informé(e)s et reconnaissez que vos actions sont susceptibles
  d’être enregistrées, conservées et auditées conformément à la politique de
  sécurité de votre organisation.  Veuillez vous rapprocher de votre
  administrateur WALLIX Bastion pour plus d’informations.

  Linux vm131 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11)
  x86_64

  The programs included with the Debian GNU/Linux system are free software; the
  exact distribution terms for each program are described in the individual
  files in /usr/share/doc/*/copyright.

  Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent permitted
  by applicable law.  Last login: Wed Jan 19 14:07:35 2022 from 10.240.14.156
  baptiste@vm131:~$


Fromt here you should be able to ssh to any Data Advisory ressources like
srv-00 etc... ::

  $ baptiste@vm131:~$ ssh srv-00
    Linux srv-00 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64

    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Mon Jan 17 12:15:34 2022 from 172.16.2.170
    baptiste@srv-00:~$


**Warning** Please remove any proxyjump configuration(~/.ssh/ssh_config) you
have to any akdX..srv-xx..vmxx. as they will no longer work.

At the moment it's not yet possible to configure some kind of `ProxyJump` to
allow to issue this kind of command::

  $ ssh srv-00.zettafox.com

This will hopefully will be fixed soon.

Sending files through VPN
---------------------------

As Agent forwarding is not supported by Wallix Bastion you will have to create
a scp command wrapper in order to send files to vm131.zettafox.com.::

  $ sudo touch /usr/bin/scp-A
  $ echo $'#!/bin/sh\nscp -oForwardAgent=yes -S scp-A-wrapper "$@"' |sudo tee /usr/bin/scp-A
  $ sudo touch /usr/bin/scp-A-wrapper
  $ echo $'#!/usr/bin/perl\nexec '/usr/bin/ssh', map {($_ =~ /^-oForwardAgent[ =]no$/) || ($_ eq '-a') ? ( ) : $_} @ARGV;' |sudo tee -a /usr/bin/scp-A-wrapper
  $ chmod +x /usr/bin/scp-A /usr/bin/scp-A-wrapper

Quick verification::

  $ cat /usr/bin/scp-A
    #!/bin/sh

    scp -oForwardAgent=yes -S scp-A-wrapper "$@"

  $ cat /usr/bin/scp-A-wrapper
    #!/usr/bin/perl

    exec '/usr/bin/ssh', map {($_ =~ /^-oForwardAgent[ =]no$/) || ($_ eq '-a') ? ( ) : $_} @ARGV;

SCP test::

  $ touch text.txt
  $ scp-A  test.txt  fox@Mazars_Lab@vm131.zettafox.com+SSH+NAME.SURRNAME@bastion.mazars.fr:/tmp

    test.txt                                        100%  579    11.1KB/s   00:00



Configure SSH
=================

Set up your ssh keys
---------------------
This step will enable proper connection to Gitlab, servers, ...

Ask for the USB stick with your ssh keys and follow next step::

  $ ssh-keygen  # this will create a ~/.ssh folder

Copy your ssh key pairs from (an admin will provide them to you) to the ``.ssh`` folder::

  $ cd ~/.ssh/ && rm id_rsa*
  $ tree -a /path/to_usb_key/
  $ cp path/to_usb_key/new_fox@mazars.fr* ~/.ssh/
  $ ln -s ~/.ssh/new_fox@mazars.fr id_rsa
  $ chmod 0600 ~/.ssh/*

Add a the minimal ssh config file ::

  $ cd ~/.ssh
  # to tunnel MazarsLab Web access through akd6
  #   e.g. to access https://reinventingaudit.mazars.fr
  #  1. first run a ssh tunel (keep consol opened)
  #   $ ssh -D 8123 -q -C -N -A fox@akd6.zettafox.com
  #  2. configure firefox to proxy all trafic throught our tunel
  #   config: set Proxy > manual > Hôte SOCKS V5: localhost Port:8123

  $ # Please copy the below in your `~/.ssh/config`
  $ cat ~/.ssh/config
  AddKeysToAgent yes

  host *
     ForwardAgent yes
     GSSAPIAuthentication no
     AddKeysToAgent yes
     ServerAliveInterval 15

  Host *.zettafox.com
     ServerAliveInterval 15

  host akd6 akd6.zettafox.com
     hostname akd6.zettafox.com
     Port 443
     User fox

  host akd4 akd4.zettafox.com
     hostname akd4.zettafox.com
     ProxyJump fox@akd6.zettafox.com

  host code.mazars.global
     Hostname 52.169.52.102

  host srv-00 srv-00.zettafox.com
     hostname srv-00.zettafox.com
     ProxyJump fox@akd4.zettafox.com


Create arbo
-------------
Create same arborescence as our Gitlab groups::

  $ mkdir -p proj/g/{knowledge,demo,2019,2020,infra,mz}

clone your first repo
----------------------
::

  $ cd ~/proj/knowledge
  $ git clone git@code.mazars.global:knowledge/knowledge_data_advisory.git
  $ cd fox_dojo.git

Private PYPI server configuration
===================================================

As all private dependency will be now stored in our private pypi server, you
will to make a persistent configuration for it. :: 

  $ echo 'export PIP_CONFIG_FILE=~/.pip.conf' | tee -a ~/.bashrc
  $ source ~/.bashrc
  $ echo $PIP_CONFIG_FILE
    /home/xxxx/.pip.conf
  $ echo -e '[global]\n index= https://pypi.org/\n index-url = https://pypi.org/simple\n extra-index-url = https://fox:secret@pypi.zettafox.com' >> ~/.pip.conf
  $ cat ~/.pip.conf

    [global]
    index= https://pypi.org/
    index-url = https://pypi.org/simple
    extra-index-url = https://ci_user:iNgeeyigh9ain7ooy4@pypi.zettafox.com

Testing pulling private repository(In a venv)::

  $ pip install mz_rd








Install Python stuff in ``~/venv`` in virtualenv
===================================================

Never use pip as root (``sudo pip install ...``).

Create ``~/venv``, our own python development environment::

  $ deactivate  # to quit venv if any
  $ python3 -m venv ~/venv

Activate your virtualenv::

  $ source ~/venv/bin/activate
  (venv) $

Make this persistant::

  (venv) $ echo "source ~/venv/bin/activate" >> ~/.bashrc

Upgrade pip and others::

  $ pip install -U pip setuptools wheel

To get a insulated jupyter-kernel dedicated to a specific virtualenv::

  (venv) $ pip3 install ipykernel
  (venv) $ python -m ipykernel install --name "venv-python-kernel" --display-name "venv-python" --user
  (venv) $

You can check if your python is correctly installed::

  (venv) $ which python
  /home/fox/venv/bin/python
  (venv) $

Install our software stack::

  $ pip install yapf flake8
  $ pip install pandas
  $ pip install scikit-learn
  $ pip install scipy
  $ pip install git+https://github.com/LuisBL/pyan

Install tools for akd-doc::

  $ pip install PyYAML
  $ pip install docutils
  $ pip install pygments
  $ pip install rst2html5-tools
  $ sudo apt-get install pandoc
  $ git clone https://github.com/chrissimpkins/md2rst.git; cd md2rst
  $ sudo make install

pyenv to switch from differents Pythons and manages virtualenv
================================================================

Install pyenv
--------------

``pyenv`` allow you to use on your laptop differents Python version on a
project base e.g. a project on Python 3.7 (to run on a production server using
Debian 10.x) even if your Ubuntu default Python is the 3.8.

1. Have packages to be able to compile you own python::

    $ sudo apt-get install git python3-pip make build-essential libssl-dev \
      zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libffi-dev

2. install pyenv::

   $ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

The above just create a ``~/.pyenv`` folder and add 6 lines (below) to your
``.bashrc``

3. Restart your shell so the path changes take effect::

   $ exec $SHELL

4. Anytime **update** in case there is now stuff on pyenv github project::

   $ pyenv update

5. in case you need to **uninstall** you only have to remove `~/.pyenv` and remove
   from your `~/.bashrc` the following lines::

     export PYENV_ROOT="$HOME/.pyenv"
     export PATH="$PYENV_ROOT/bin:$PATH"
     if command -v pyenv 1>/dev/null 2>&1; then
       eval "$(pyenv init --path)"
       eval "$(pyenv init -)"
       eval "$(pyenv virtualenv-init -)"
     fi

Install/Compile a specific Python
-----------------------------------
initialy there is only the ``system`` Python::

  $ pyenv versions
    system
  $

Install/compile a specific Python e.g. ``3.7.3`` (this can take some time)::

  $ pyenv install 3.7.3
  Downloading Python-3.7.3.tar.xz...
  -> https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
  Installing Python-3.7.3...
  Installed Python-3.7.3 to /home/luis/.pyenv/versions/3.7.3
  $

Check pyenv ::

  $ cd /tmp/
  /tmp$

  /tmp$ pyenv versions
  * system (set by /home/luis/.pyenv/version)
    3.7.3
  /tmp$

Switch from installed Pythons with ``pyenv global ...``
---------------------------------------------------------
To **switch from one Python to another** (from the ones installed in
``.pyenv/version`` use ``pyenv global x.y.z`` or ``pyenv global system`` to
comeback to the system Python::

  /tmp$ mkdir abc
  /tmp$ cd abc
  /tmp/abc$ pyenv versions
  * system (set by /home/luis/.pyenv/version)
    3.7.3
  /tmp/abc$ python3 --version
  Python 3.8.5
  /tmp/abc$

  /tmp/abc$ pyenv global 3.7.3
  /tmp/abc$ python3 --version
  Python 3.7.3
  /tmp/abc$ pyenv global system
  /tmp/abc$ python3 --version
  Python 3.8.5
  /tmp/abc$

.. note::

  ``pyenv global`` work by reads/writes the ``~/.python-version`` file.


Create/manage Virtualenvs
---------------------------
Virtualenvs are managed directly by ``pyenv``, they are handeled like
additional environments.::

  $ pyenv virtualenvs
  $

Create new virtualenv::

  $ pyenv virtualenv 3.7.3 v37
  ...
  $
  $ pyenv virtualenvs
  3.7.3/envs/v37 (created from /home/luis/.pyenv/versions/3.7.3)
  v37 (created from /home/luis/.pyenv/versions/3.7.3)
  $

.. note::

  For one virtualenvs two lines are showed on ``pyenv virtualenvs`` the short
  name for the prompt and the long one to know in which Python this virtualenv
  has been created.

Manualy activate this virtualenv::

  $ pyenv global v37
  (v37) $

  (v37) $ pyenv virtualenvs
    3.7.3/envs/v37 (created from /home/luis/.pyenv/versions/3.7.3)
  * v37 (created from /home/luis/.pyenv/versions/3.7.3)
  (v37) $

As we said virtualenvs are managed as new Python versions::

  (v37) $ pyenv versions
    system
    3.7.3
    3.7.3/envs/v37
  * v37 (set by /home/luis/.pyenv/version)
  (v37) $

Automate Python version and Virtualenvs on folder basis
---------------------------------------------------------
``pyenv local <version>`` create a locale `.python-version` file with the
`<version>` in it, `<version>` could be a Python version or a Virtualenv.::

  (v37) /tmp/abc$ pyenv global system
  /tmp/abc$ pyenv versions
  * system (set by /home/luis/.pyenv/version)
    3.7.3
    3.7.3/envs/v37
    v37
  /tmp/abc$
  (v37) /tmp/abc$ ls -lA
  total 0
  (v37) /tmp/abc$


  /tmp/abc$ pyenv local v37
  (v37) /tmp/abc$ ls -lA
  total 44
  -rw-rw-r--  1 luis luis     4 juin  28 00:56 .python-version
  (v37) /tmp/abc$ more .python-version
  v37
  (v37) /tmp/abc$

So now the magic !

Because of the ``eval "$(pyenv virtualenv-init -)"`` in ``~/.bashrc``
pyenv-virtualenv will automatically activate/deactivate virtualenvs on
entering/leaving directories which contain a .python-version file that contains
the name of a valid virtual environment::

  (v37) /tmp/abc$
  (v37) /tmp/abc$ cd /tmp/
  /tmp$                        # <== not any more in the virtualenv
  /tmp$ cd abc
  (v37) /tmp/abc$              # <== back on the virtualenv automatically


Now if we change directory to a project that contain a ``.python-version`` file
with ``3.7.3`` in it, ``pyenv`` will automaticly trigger Python 3.7.3 if we call python::

  $ cd ~/proj/g/mz/aaa/
  $ more .python-version
  3.7.3
  $

``pyenv`` provide a way to urbanize ``virtualenv`` for all ours projects::

.. note::

  More on ``pyenv`` https://pycon.switowski.com/02-packages/pyenv/ and
  https://github.com/pyenv/pyenv/wiki


Configure Nautilus, gnome and vim
===================================

Nautilus
---------
We can use nautilus as scp/sftp connection.

Example of connection to akd6::

  $ nautilus sftp://pepsakd@IP_ADDRESS:22

Other example of connection to lpm::

  $ nautilus sftp://fox@ftp.zettafox.com:22/home/fox/

gnome-tweak-tool
-----------------
To configure the desktop and keyboard, use ``gnome-tweaks``

vim
---------
Get ``~/.vimrc file``::

   $ cd ~
   $ cp .vimrc .vimrc_old
   $ mv ~/.vim ~/.vim_old
   $ wget https://cdn-atlas.mazars.global/knowledge_data_advisory/fox_config_files/.vimrc
   $ curl -sfLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

Restart vim and call `:PlugUpdate` from inside ``vim``::

   :PlugUpdate

Note: In case files are not yet on `config.zettafox.com` take them from the
data advisory knowledge repository: `knowledge_data_advisory/fox_config_files`

Annexe
=======

Create a bootable key on Windows
--------------------------------
https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows?_ga=2.179043747.663370362.1526377069-1982938259.1521117453#0

Exercice 1
----------
- sceenshot the Zett Know Center
- crop the image with `gimp`

Exercice 2
----------
- use `shutter` to document the interface with arrows and blocktext
- download with firefox two pdf files with more than 5 pages using
  `curl` and then `wget`
- use `qpdf` to create a result.pdf with a selection of pages
   - concatenate pages from both pdf
   - create a result_2x2.pdf page (as people often do when printing ppt slides)
- use a `pdftotext` create a result.txt with the text of the pdf

.. to split a doc in pages
.. XXX please upgrade this to qpdf pdftk source.pdf burst output out_%03d.pdf
.. pdftk source.pdf burst output out_%03d.pdf

Exercice 3
----------
- create a folder with files in it (pdf, resullt_xyz, ...)

  - create a zip file of this folder
  - create a ziped tarball .tgz and a tar file

    - gzip the tarball with pigz

- download an excel file use `unoconv` to convert it in:

  - xlsx, pdf and in text

- download a pptx file use `unoconv` to convert it in:

  - ppt, pdf and in text


- use `pdfnup` to 2 pages per sheet in a pdf

.. solution: `pdfnup doc.pdf`

- use pdfjam to have 4 pages per sheet in a pdf

.. solution: `pdfjam --nup 2x2 doc.pdf` to 4 pages per sheet in a pdf

Additional software stack
===========================
R specific stuff
-----------------
Add cran debian repository::

    $ sudo vim /etc/apt/sources.list  # add this line at the end
       deb http://cran.univ-paris1.fr/bin/linux/ubuntu bionic-cran35/

Set gpg keys::

    $ gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
    $ gpg -a --export E084DAB9 | sudo apt-key add -

Update and install::

    sudo apt-get update
    sudo apt-get install r-base

Install RStudio:

NB: In order to install Rstudio, you will need to add 'libjpeg62' first.

    - get **RStudio Desktop 64bits Ubuntu** from here https://www.rstudio.com/products/rstudio/download/

Install ``rstudio-xyz-amd64.deb`` with ``dpkg``::

    $ sudo dpkg -i rstudio-xyz-amd64.deb
