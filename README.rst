maxi-card.py
============

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
~~~~~~~~~~~~~~~~~~~~

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

       #setting server
       card.server = guild

       #sending image to discord channel
       await channel.send(file=await card.create())

   client.run("TOKEN")

Generated Welcome Card
~~~~~~~~~~~~~~~~~~~~~~ 
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/welcome-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/welcome-card.png 
   :alt: Created card from example code.

Leave Card Example
~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.event
   async def on_member_remove(member):
       #guild definition 
       guild = member.guild

       #welcome channel definition (id=YourLeaveChannelID)
       channel = discord.utils.get(guild.text_channels, id=753239660230082690)

       #creating leave card object
       card = LeaveCard()
       
       #setting member name
       card.member = member

       #setting account created time
       card.datetime = member.created_at.strftime("%d, %B %Y, %H:%M %p")

       #setting server
       card.server = guild

       #sending image to discord channel
       await channel.send(file=await card.create())

   client.run("TOKEN")

Generated Leave Card 
~~~~~~~~~~~~~~~~~~~~ 
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/leave-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/leave-card.png 
   :alt: Created card from example code.

Wanted Card Example
~~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def wanted(ctx):
   
       #creating wanted card object
       card = WantedCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Wanted Card 
~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/wanted-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/wanted-card.png 
   :alt: Created card from example code.

Delete Card Example
~~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def delete(ctx):
   
       #creating delete card object
       card = DeleteCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Delete Card 
~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/delete-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/delete-card.png 
   :alt: Created card from example code.

Trash Card Example
~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def trash(ctx):
   
       #creating trash card object
       card = TrashCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Trash Card 
~~~~~~~~~~~~~~~~~~~~ 
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/trash-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/trash-card.png 
   :alt: Created card from example code.

Tombstone Card Example
~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def tombstone(ctx):
   
       #creating tombstone card object
       card = TombstoneCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Tombstone Card 
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/tombstone-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/tombstone-card.png 
   :alt: Created card from example code.

Hitler Card Example
~~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def hitler(ctx):
   
       #creating hitler card object
       card = HitlerCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Hitler Card 
~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/hitler-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/hitler-card.png 
   :alt: Created card from example code.

Jail Card Example
~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def jail(ctx):
   
       #creating jail card object
       card = JailCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Jail Card 
~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/jail-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/jail-card.png 
   :alt: Created card from example code.

Passed Card Example
~~~~~~~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from maxicard import *

   intents = discord.Intents.default()
   intents.members = True

   client = commands.Bot(command_prefix="!", intents=intents)

   @client.command()
   async def missionpassed(ctx):
   
       #creating passed card object
       card = PassedCard()
       
       #setting avatar image
       card.avatar = ctx.author.avatar_url

       #sending image to discord channel
       await ctx.send(file=await card.create())

   client.run("TOKEN")

Generated Passed Card 
~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/passed-card.png 
   :target: https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/created_cards/passed-card.png 
   :alt: Created card from example code.
