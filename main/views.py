from django.shortcuts import render
from .forms import SchoolForm
from g4f.client import Client
import re

client = Client()

def index(request):
    form = SchoolForm()
    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def submit_form(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            selected_class = form.cleaned_data['selected_class']
            region = form.cleaned_data['region']
            preferences = form.cleaned_data['preferences']

            # Вызов API ИИ
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": f"Выберите подходящий колледж, университет, вуз и тд, после класса {selected_class} в городе {region} с предпочтениями {preferences}. И напиши все в виде списка с описанием каждого учреждения!"
                }]
            )

            # Получение ответа от ИИ и удаление нежелательных символов
            suggested_schools_raw = response.choices[0].message.content
            suggested_schools_cleaned = re.sub(r'[\*\#]', '', suggested_schools_raw)
            suggested_schools = [
                {
                    'name': school.split("\n")[0].strip(),
                    'description': "\n".join(school.split("\n")[1:]).strip()
                }
                for school in suggested_schools_cleaned.split("\n\n") if school.strip()
            ]

            context = {
                'selected_class': selected_class,
                'region': region,
                'preferences': preferences,
                'suggested_schools': suggested_schools,
            }
            return render(request, 'result.html', context)
    else:
        form = SchoolForm()
    return render(request, 'index.html', {'form': form})
