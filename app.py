import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
#from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

#model_id = "CompVis/stable-diffusion-v1-4"
#model_id = "CompVis/stable-diffusion-hyperprior-v1"
model_id = "CompVis/stable-diffusion-unet-v1"
#model_id = "CompVis/stable-diffusion-guided-diffusion-v1"

device = 'cuda'
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16)
pipe.to(device)

def generate():
    with autocast(device):
        generator = torch.Generator(device).manual_seed(1024)
        image = pipe(prompt.get(), guidance_scale=7.5, generator=generator ).images[0]
        
    image.save('generated_image.png')
    img = ImageTk.PhotoImage(image)
    label_main.config(image=img)

#Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Image Generation")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height=40, width=512, text_color='black', fg_color='white')
prompt.place(x=10, y=10)

label_main = ctk.CTkLabel(app, height=512, width=512)
label_main.place(x=10, y=110)

trigger = ctk.CTkButton(app, height=40, width=140, text_color='white', fg_color='blue', text='Generate', command=generate)
trigger.place(x=196, y=60)

app.mainloop()