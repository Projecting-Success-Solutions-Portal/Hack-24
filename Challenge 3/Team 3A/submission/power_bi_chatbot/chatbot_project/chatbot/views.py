from django.http import JsonResponse
from django.shortcuts import render
from .ai_logic import ask_question

def chatbot_view(request):
    if request.method == 'POST':
        try:
            message = request.POST.get('message', '').strip()
            if not message:
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)
            ai_response = ask_question(message)
            return JsonResponse({'response': ai_response})

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=400)

    return render(request, 'chatbot/chatbot.html')