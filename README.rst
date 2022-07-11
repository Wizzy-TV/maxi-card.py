maxi-card.py
==========

This is simple maker for welcome and leave cards in discord bot in discord.py or pycord.


Installing
~~~~~~~~~~

**Python 3.8 or higher is required**


.. code:: sh

    # Linux/macOS
    pip3 install -U maxi-card.py

    # Windows
    pip install -U maxi-card.py


Welcome Card Example
~~~~~~~~~~~~~~~~~~

.. code:: py

   from discord.ext import commands
   from maxicard import *

   client = commands.Bot(command_prefix=".") code:: sh

   client.run("TOKEN")