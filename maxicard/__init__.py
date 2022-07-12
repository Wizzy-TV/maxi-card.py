import os
from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

class WelcomeCard():

    def __init__(self):
        self.server : str = None
        self.name : str = None
        self.color : str = "violet"
        self.text : str = "Welcome to the server!"
        self.is_rounded : bool = False

    async def create(self):  
        bgc = await load_image_async('https://raw.githubusercontent.com/Maxi-TM/maxi-card.py/main/welcome-bg.png')
        background = Editor(bgc).resize((552, 156))

        font_directory = os.path.join(os.path.dirname(__file__), "fonts")
        font_path = os.path.join(font_directory, "SFMono.ttf")

        poppins = Font(font_path, size=40)
        background.text((200, 35), str(f'    '+str(self.text)+' '), font=poppins, color="white")
        background.rectangle((275, 85), width=500, height=4, fill=self.color)
        background.text(
            (200, 120),
            f"Server: ",
            font=poppins,
            color=self.color,
        )
        background.text(
            (345, 115),
            f"{self.server}",
            font=poppins,
            color="white",
        )
        background.text(
            (200, 180),
            f"New User:",
            font=poppins,
            color=self.color,
        )
        background.text(
            (410, 178),
            f"{self.name}",
            font=poppins,
            color="white",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file
