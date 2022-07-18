import os
from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

class WelcomeCard():

    def __init__(self):
        self.member : str = None
        self.datetime : str = None
        self.server : str = None

    async def create(self):  
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/maxicard/imgs/bg-welcome.png')
        background = Editor(bgc).resize((552, 156))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        sfmono = Font(font_path, size=22)
        background.text(
            (159, 12),
            f"fetch {self.member.id}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 44),
            f"username",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 38),
            f"{self.member}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 67),
            f"created",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 67),
            f"{self.datetime}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 98),
            f"status",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 94),
            f"Joined the server",
            font=sfmono,
            color="#2dc970",
        )
        background.text(
            (16, 123),
            f"members",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 124),
            f"{self.server.member_count}",
            font=sfmono,
            color="#c1c1c1",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file

class LeaveCard():

    def __init__(self):
        self.member : str = None
        self.datetime : str = None
        self.server : str = None

    async def create(self):  
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/maxicard/imgs/bg-welcome.png')
        background = Editor(bgc).resize((552, 156))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        sfmono = Font(font_path, size=22)
        background.text(
            (159, 12),
            f"fetch {self.member.id}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 44),
            f"username",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 38),
            f"{self.member}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 67),
            f"created",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 67),
            f"{self.datetime}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 98),
            f"status",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 94),
            f"Left the server",
            font=sfmono,
            color="#e44b3b",
        )
        background.text(
            (16, 123),
            f"members",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (159, 124),
            f"{self.server.member_count}",
            font=sfmono,
            color="#c1c1c1",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file

class DeleteCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/maxicard/imgs/delete-bg.png')
        background = Editor(bgc).resize((1280, 609))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((751, 751))
            background.paste(profile.image, (110, 130))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file
