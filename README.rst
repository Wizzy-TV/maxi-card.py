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

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.event
   async def on_member_join(member):
     #creating welcome card object
     card = WelcomeCard()

   client.run("TOKEN")
