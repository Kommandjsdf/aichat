from django.shortcuts import render

from .forms import PromptForm

import openai
openai.api_key = ''

# Create your views here.
def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        ## is_valid
        if form.is_valid():
            prompt = form.cleaned_data['prompt']


            completion = openai.OpenAI().chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = completion.choices[0].message

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form':form,
        'response_text':response_text,
        'response_image':response_image,
    })