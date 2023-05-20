from PIL import ImageTk
import torch
from django.shortcuts import render

torch.cuda.empty_cache()
from torch import autocast
from diffusers import StableDiffusionPipeline, DiffusionPipeline
# Set the split_kernel_max_memory_usage parameter
torch.backends.cuda.split_kernel_max_memory_usage = 512

#model_id = "CompVis/stable-diffusion-v1-4"
#model_id = "CompVis/stable-diffusion-hyperprior-v1"
#model_id = "CompVis/stable-diffusion-unet-v1"
#model_id = "CompVis/stable-diffusion-guided-diffusion-v1"
model_id = "runwayml/stable-diffusion-v1-5"

device = 'cuda'
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16)
pipe.to(device)

pipeline = DiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16)
pipeline = pipeline.to(device)
generator = torch.Generator(device).manual_seed(0)

"""def generate():
    with autocast(device):
        generator = torch.Generator(device).manual_seed(1024)
        image = pipe(prompt.get(), guidance_scale=7.5, generator=generator ).images[0]
        
def generate_1():
    with autocast(device):
        image = pipeline(prompt, generator=generator).images[0]
        
    image.save('generated_image.png')
    img = ImageTk.PhotoImage(image)
    label_main.config(image=img)"""

def home(request):
    return render(request, 'home.html')