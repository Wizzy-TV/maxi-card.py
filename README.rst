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
       #guild definition 
       guild = member.guild

       #welcome channel definition (id=YourWelcomeChannelID)
       channel = discord.utils.get(guild.text_channels, id=753239660230082690)

       #creating welcome card object
       card = WelcomeCard()
       
       #setting member name
       card.member = member

       #setting account created time
       card.datetime = member.created_at.strftime("%d, %B %Y, %H:%M %p")

       #setting server name
       card.server = guild

       #sending image to discord channel
       await channel.send(file=await card.create())

   client.run("TOKEN")

Generated Welcome Card 
~~~~~~~~~~~~~~~~~~~~ 
.. image:: 
https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/welcome-card.png 
   :target: 
https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/welcome-card.png 
   :alt: Created card from example code.
