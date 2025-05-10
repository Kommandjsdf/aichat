from idlelib.query import Query

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import PromptForm

from project.settings import API_KEY

import openai
# openai.api_key = ''
client = openai.OpenAI(api_key=API_KEY)

# Create your views here.
def home(request):
    if request.user.is_autenticated:
        QueryHistory.objects.create(
            user = request.user,
            query = query,
            response_text = None,
            response_image = None,
        )

    if request.method == 'POST':
        # generate_text = request.POST.get("text_", "no")
        # generate_image = request.POST.get("image_", "no")


        form = PromptForm(request.POST)
        ## is_valid
        if form.is_valid():
            prompt = form.cleaned_data['prompt']


            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # if generate_text == "yes":
            #     response_text = completion.choices[0].message.content
            response_text = completion.choices[0].message.content

            image_result = client.images.generate(
                model="dall-e-3",
                prompt=prompt
            )
            # if generate_image == "yes":
            #     response_image = image_result.data[0].url
            response_image = image_result.data[0].url

            # model "gpt-image-1"
            # image_result = client.images.generate(
            #     model="gpt-image-1",
            #     prompt=prompt
            # )
            #
            # image_base64 = image_result.data[0].b64_json
            # response_image = image_base64.b64decode(image_base64)
    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form':form,
        'response_text':response_text,
        'response_image':response_image,
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
