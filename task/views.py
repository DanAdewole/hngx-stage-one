from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import datetime


@api_view(['GET'])
def task(request):
    current_time = datetime.datetime.now()
    current_day = current_time.strftime('%A')
    current_utc_time = datetime.datetime.utcnow()
    
    slack_name = request.GET.get('slack_name', None)
    track = request.GET.get('track', None)
    github_repo_url = "https://github.com/DanAdewole/hngx-stage-one.git"
    
    result = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": "to come",
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return Response(result)
    
    
    