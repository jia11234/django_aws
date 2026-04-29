from django.shortcuts import render, redirect
from datetime import datetime
from .models import ChatHistory
from django.http import JsonResponse
import json
import requests

def index(request):
    history = ChatHistory.objects.all().order_by('-id') 
    return render(request, 'app/index.html', {'history': history})

def question(request):
    if request.method == 'POST':
        # 1. 브라우저가 보낸 데이터 받기
        data = json.loads(request.body)
        user_msg = data.get('message')
        
        fastapi_res = requests.post(
            "http://127.0.0.1:8080/question/",
            json={"message": user_msg}
        )
        ai_ans = fastapi_res.json().get('answer')
        
        # 3. DB에 저장 (이게 끝!)
        ChatHistory.objects.create(question=user_msg, answer=ai_ans)
        
        return JsonResponse({'answer': ai_ans})
def all(request):
    history = ChatHistory.objects.all().order_by('-id') 
    return render(request, 'app/index.html', {'history': history})
