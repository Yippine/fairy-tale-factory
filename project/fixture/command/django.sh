# 建立 Django 專案
django-admin startproject <project_name>

# 建立 Django 應用，依照不同功能組織前後端的程式碼
python manage.py startapp <app_name>

# 啟動 Django 開發伺服器，讓你能夠在本地瀏覽器中測試你的網站應用
python manage.py runserver

# 將資料庫結構自動轉換為 Django 應用中的模型代碼，並保存到 models.py 文件中
# 需要到專案的根目錄執行
python manage.py inspectdb > models.py

# 建立資料庫遷移（migrations），它會檢測你對模型的更改並記錄下來
python manage.py makemigrations

# 將遷移應用到資料庫，確保你的資料庫與你的模型保持同步
python manage.py migrate

# 建立翻譯文件，特別是針對中文翻譯
python manage.py makemessages -l zh_TW

# 將資料庫轉換成 JSON 格式的 fixture 文件
python -Xutf8 manage.py dumpdata --indent 4 --output=fixture/sql/database_data.json
