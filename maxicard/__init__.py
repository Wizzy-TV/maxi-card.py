import os
from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

class WelcomeCard():

    def __init__(self):
        self.member : str = "member"
        self.server : str = None
        self.color : str = "violet"

    async def create(self):  
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/welcome-bg.png')
        background = Editor(bgc).resize((552, 156))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        sfmono = Font(font_path, size=22)
        background.text(
            (220, 12),
            f"fetch {self.member.id}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 40),
            f"username",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (200, 180),
            f"New User:",
            font=sfmono,
            color=self.color,
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file
