import os
from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

class WelcomeCard():

    def __init__(self):
        self.member : str = None
        self.datetime : str = None
        self.server : str = None

    async def create(self):  
        background = Editor(Canvas((552, 156), color="#181818"))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        sfmono = Font(font_path, size=22)

        background.text(
            (16, 12),
            f"~/discord",
            font=sfmono,
            color="#01ed01",
        )
        background.text(
            (140, 12),
            f"$",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 12),
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
            (140, 44),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 38),
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
            (140, 71),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 67),
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
            (140, 100),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 94),
            f"Joined the server",
            font=sfmono,
            color="#2dc970",
        )
        background.text(
            (16, 124),
            f"members",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (140, 128),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 124),
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
        background = Editor(Canvas((552, 156), color="#181818"))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        sfmono = Font(font_path, size=22)
        background.text(
            (16, 12),
            f"~/discord",
            font=sfmono,
            color="#01ed01",
        )
        background.text(
            (140, 12),
            f"$",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 12),
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
            (140, 44),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 38),
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
            (140, 71),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 67),
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
            (140, 100),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 94),
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
            (140, 128),
            f":",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (169, 124),
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

        img_directory = os.path.join(os.path.dirname(__file__), "imgs")
        img_path = os.path.join(img_directory, "delete-bg.png")

        background = Editor(img_path).resize((1280, 609))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((334, 334))
            background.paste(profile.image, (215, 230))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class TrashCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):

        img_directory = os.path.join(os.path.dirname(__file__), "imgs")
        img_path = os.path.join(img_directory, "trash-bg.png")

        background = Editor(img_path).resize((1080, 583))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((180, 180))
            background.paste(profile.image, (330, 220))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class WantedCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):

        img_directory = os.path.join(os.path.dirname(__file__), "imgs")
        img_path = os.path.join(img_directory, "wanted-bg.png")

        background = Editor(img_path).resize((736, 959))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((353, 353))
            background.paste(profile.image, (185, 310))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class TombstoneCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):

        img_directory = os.path.join(os.path.dirname(__file__), "imgs")
        img_path = os.path.join(img_directory, "tombstone-bg.png")

        background = Editor(img_path).resize((400, 313))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((130, 130))
            background.paste(profile.image, (130, 100))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class HitlerCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):

        img_directory = os.path.join(os.path.dirname(__file__), "imgs")
        img_path = os.path.join(img_directory, "hitler-bg.png")

        background = Editor(img_path).resize((480, 360))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            profile = Editor(profile).resize((142, 142))
            background.paste(profile.image, (45, 40))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class JailCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):
        bgc = await load_image_async(str(self.avatar))
        background = Editor(bgc).resize((350, 350))
        if(self.avatar != None):

            img_directory = os.path.join(os.path.dirname(__file__), "imgs")
            img_path = os.path.join(img_directory, "jail-bg.png")

            jail = Editor(img_path).resize((350, 350))
            background.paste(jail.image, (0, 0))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file

class PassedCard():

    def __init__(self):
        self.avatar : str = None

    async def create(self):
        bgc = await load_image_async(str(self.avatar))
        background = Editor(bgc).resize((512, 512))
        if(self.avatar != None):

            img_directory = os.path.join(os.path.dirname(__file__), "imgs")
            img_path = os.path.join(img_directory, "passed-bg.png")

            passed = Editor(img_path).resize((512, 512))
            background.paste(passed.image, (0, 0))
        
        file = File(fp=background.image_bytes, filename="card.png")
        return file
