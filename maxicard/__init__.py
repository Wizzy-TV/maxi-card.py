import os
from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

class WelcomeCard():

    def __init__(self):
        self.member : str = None

    async def create(self):  
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/bg.png')
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
            (16, 44),
            f"username",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (145, 38),
            f"{self.member}",
            font=sfmono,
            color="#c1c1c1",
        )
        background.text(
            (16, 76),
            f"created",
            font=sfmono,
            color="#c1c1c1",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file
