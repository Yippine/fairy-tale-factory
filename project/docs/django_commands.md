# Django Commands Full Guide

## 建立 Django 專案

```bash
django-admin startproject <project_name>
```

- `<project_name>`：替換為您的專案名稱。
- 這條指令會建立一個新的 Django 專案。

## 建立 Django 應用

```bash
python manage.py startapp <app_name>
```

- `<app_name>`：替換為您的應用名稱。
- 每個 Django 應用都封裝了特定的功能。

## 啟動 Django 開發伺服器

```bash
python manage.py runserver
```

- 在本地端啟動一個輕量級的 Web 伺服器，方便開發和測試。

## 檢查資料庫結構並生成模型

```bash
python manage.py inspectdb > models.py
```

- 執行此指令將會自動檢查資料庫中的表格結構，並根據結構生成相對應的 Django 模型類別，這將大大節省您建立模型的時間和精力。

## 自定義模型名稱

```bash
python manage.py inspectdb --database=<database_name> > custom_models.py
```

- `<database_name>`：替換為您想要檢查的資料庫名稱。

## 從特定資料庫檢查表格結構

```bash
python manage.py inspectdb --database=<database_name> > models_from_specific_db.py
```

- `<database_name>`：替換為您想要檢查的特定資料庫名稱。

## 建立資料庫遷移

```bash
python manage.py makemigrations
```

- 檢測模型的變更並創建遷移檔案。

## 應用資料庫遷移

```bash
python manage.py migrate
```

- 執行遷移以更新資料庫結構。

## 建立超級用戶

```bash
python manage.py createsuperuser
```

- 建立一個可以登入管理後台的超級用戶。

## 建立翻譯文件

```bash
python manage.py makemessages -l zh_TW
```

- `l zh_TW`：指定翻譯語言為繁體中文。

## 編譯翻譯文件

```bash
python manage.py compilemessages
```

- 將 `.po` 翻譯文件編譯成 `.mo` 文件，供 Django 使用。

## 將資料庫轉換成 JSON 格式的 fixture 文件

要將資料庫中的數據轉換成 JSON 格式的 fixture 文件，可以使用以下命令：

```bash
python -Xutf8 manage.py dumpdata --indent 4 --output=fixture/sql/database_data.json
```

- 這個命令將當前資料庫的資料導出為 JSON 格式，並指定了輸出文件的路徑為 fixture/sql/database_data.json。
- 使用 --indent 4 參數可以美化輸出的 JSON 文件，使其易讀性更高。
- 該操作對於數據遷移、備份和重用非常有用。

## 加載 fixture 數據

一旦您已經將資料庫數據導出為 JSON fixture 文件，您可以使用以下命令來加載數據：

```bash
python manage.py loaddata fixture/sql/database_data.json
```

- 這個命令將指定的 fixture 文件中的數據加載到當前資料庫中。
- 請確保指定的文件路徑和文件名正確，以免加載錯誤的數據。
- 通常在測試、開發或數據還原的情況下使用此操作。
