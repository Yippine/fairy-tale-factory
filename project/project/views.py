import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

#使用 redirect 函數將請求重定向到 "/home"。
def redirect_to_home(request):
    return redirect("/home")

#render 函數將 home.html 模板渲染為HTTP響應
def home(request):
    return render(request, "home.html")

def about_us(request):
    return render(request, 'about_us.html')

def talk_to_chatgpt(request):
    return render(request, 'talk_to_chatgpt.html')

def search_files(request):
    return JsonResponse({'files': ''})

def get_file_content(request):
    return HttpResponse("", content_type='text/plain; charset=utf-8')

def home_new(request):
    return render(request, "home_new.html")

def about_us_new(request):
    return render(request, 'about_us_new.html')

def talk_to_chatgpt_new(request):
    prompt = "你已經是經營這個領域幾十年的 IT 專家，請直接告訴我最簡潔、最有效能且最精美的程式碼範例和最簡單、最有效、最系統且最全面的解答，以及你的心路歷程，感謝您："
    return render(request, 'talk_to_chatgpt_new.html', {"prompt": prompt})

def search_files_new(request):
    search_text = request.GET.get('searchText', '') # 獲取URL參數中的搜尋文字
    directory = os.path.abspath(os.path.dirname(__name__)) # 指定要搜尋的目錄
    matching_files = []
    # 遍歷指定目錄及其子目錄下的所有檔案
    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_text.lower() in file.lower(): # 如果檔案名包含搜尋文字
                full_path = os.path.join(root, file) # 完整的檔案路徑
                relative_path = os.path.relpath(full_path, directory).replace("\\", "/") # 相對於 Django 根目錄的路徑
                file_info = {
                    "full_path": full_path,
                    "relative_path": relative_path
                }
                matching_files.append(file_info)
    return JsonResponse({'files': matching_files}) # 返回JSON響應

def get_file_content_new(request):
    # 從請求中獲取檔案路徑參數
    file_path = request.GET.get('path', '')
    # 確認檔案存在
    if not os.path.isfile(file_path):
        return HttpResponse('File not found.', status=404)
    try:
        # 嘗試以不同編碼讀取檔案內容
        for encoding in ['utf-8', 'utf-16', 'iso-8859-1']:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    content = file.read()
                    return HttpResponse(content, content_type='text/plain; charset=utf-8')
            except UnicodeDecodeError:
                continue
        # 如果所有編碼都失敗，返回錯誤響應
        return HttpResponse('Failed to read file content with known encodings.', status=500)
    except Exception as e:
        return HttpResponse(f'Error reading file: {str(e)}', status=500)
