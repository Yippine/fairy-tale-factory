import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle_post_request(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            for key, value in data.items():
                request.session[key] = value
            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON format"}, status=400
            )
    return JsonResponse(
        {"status": "error", "message": "Method not allowed"}, status=405
    )

# 清空目錄下的所有檔案和子目錄
def clear_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
