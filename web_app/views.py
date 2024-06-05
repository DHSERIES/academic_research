from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render


def home(request):
    # View code here...
    return render(request,"index.html")
    
@csrf_exempt 
def chatbot(request):
    if request.method == 'POST':
        message = json.loads(request.body).get('message')
        
        # Use your chatbot logic (e.g., GPT-3, other model) to generate a response
        generate_response  ="hello"
        response_message = generate_response
        
        return JsonResponse({'response': response_message})