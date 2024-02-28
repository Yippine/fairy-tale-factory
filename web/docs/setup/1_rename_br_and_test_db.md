# 專案設定指南

本指南旨在幫助您快速將專案更新至最新版本並成功運行網站。請依照以下步驟操作：

## 更新專案至最新版本

首先，確保您的本地專案與遠端儲存庫同步至最新狀態。

1. **版本切換與重命名**

    ```bash
    git checkout v1.0.0
    git branch -m v1.0.0 v0.1.0
    git push origin -u v0.1.0
    git push origin --delete v1.0.0
    ```

2. **設定並同步上游儲存庫**

    ```bash
    git remote add upstream https://github.com/Yippine/fairy-tale-factory
    git fetch upstream
    ```

3. **合併更新**

    ```bash
    git checkout -b v0.0.0
    git merge upstream/v0.0.0
    git checkout v0.1.0
    git rebase v0.1.0
    git merge upstream/v0.1.0
    ```

4. **開發分支操作**

- 如果有開發分支，請合併更新：

    ```bash
    git merge `開發者名稱`
    git branch -d `開發者名稱`
    ```

- 或創建新的開發分支：

    ```bash
    git checkout -b `開發者名稱`
    git merge v0.1.0
    ```

5. **查看版本記錄**

    ```bash
    git lg
    # 或
    git log --graph --pretty=format:'%C(auto)%h %C(bold blue)%cn %C(auto)%s %C(bold green)%cr'
    ```

## 運行網站

確保您的環境已準備就緒並且資料庫已設定。

1. **設定虛擬環境與套件安裝**

    ```bash
    pipenv --python 3.9
    pipenv shell
    pip install -r requirements.txt
    ```

2. **資料庫設定**

    執行 `database_structure.sql` 創建並配置 `fairy_tale_factory` 資料庫，並建立一筆 `user` 表格的資料。

3. **配置 Django 設定**

    更新 `project/project/settings.py` 中的資料庫配置。

    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'fairy_tale_factory',
            'USER': '你的資料庫使用者名稱',
            'PASSWORD': '你的資料庫使用者密碼',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

4. **運行網站**

    ```bash
    cd project
    python manage.py runserver
    ```

前往 [http://127.0.0.1/](http://127.0.0.1/) 查看網站是否運行成功。測試資料是否顯示，訪問 [http://127.0.0.1/user/test/getfirstuser/](http://127.0.0.1/user/test/getfirstuser/)。
