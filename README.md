# Fairy Tale Factory 童話工廠

歡迎來到 Fairy Tale Factory 專案！這份文件旨在提供清晰、有效、系統、全面的指南，以幫助新手和經驗豐富的開發者快速了解並貢獻於該專案。

## 專案結構概觀

Fairy Tale Factory 專案的結構設計使得導航和開發變得輕鬆。以下是主要目錄和文件的概覽：

- **.env**：包含專案配置的環境變數。
- **manage.py**：一個命令行實用工具，可讓您與這個 Django 專案進行互動。
- **requirements.txt**：列出專案的所有 Python 相關第三方套件。

### 目錄：

- **docs/**：開發者文件目錄。
  - *coding_indent_guide.md*：代碼縮進指南，介紹代碼縮進的標準和最佳實踐。
  - *commit_guidelines.md*：關於對該專案進行提交的指南，規範提交訊息的格式和內容。
  - *django_commands.md*：專案中常用的 Django 命令，列舉了常見的 Django 命令及其使用方法。
  - *docker_commands.md*：用於容器管理的有用 Docker 命令，包括容器的建立、啟動、停止等操作。
  - *layout_design_guide.md*：版面設計指南，介紹專案中的版面設計規範和最佳實踐。
  - *sql_commands.md*：用於資料庫管理的常見 SQL 命令，包括資料查詢、修改等操作。
  - *talk_to_chatgpt.md*：集成並與 ChatGPT 進行互動的說明，介紹如何整合 ChatGPT 並進行對話。
  - *TODO.md*：待實現的任務和功能列表，列出尚未完成的任務和待辦事項。
  - **git/**：Git 相關文件目錄，提供了有關版本控制的指南和命令參考。
    - *command_guide.md*：Git 命令參考指南，列舉了常見的 Git 命令及其用法。
    - *commit_guide.md*：提交指南，規範了提交訊息的格式和提交流程。
    - *workflow_guide.md*：工作流指南，介紹了專案中常用的工作流程和最佳實踐。
  - **env/**：環境設定目錄，包括對開發環境進行配置的相關文件。
    - *1_rename_br_and_test_db.md*：重命名分支和資料庫測試的指南，介紹如何重命名分支以及資料庫測試的配置。
    - *2_decouple_and_env_config.md*：分離敏感資訊並使用環境變量文件的指南，介紹如何將敏感資訊分離並存儲於環境變量文件中。
    - *3_new_env_setup.md*：新環境設置指南，介紹在新環境中進行配置的步驟和注意事項。

- **fixture/**：包含用於將初始資料加載到資料庫中的文件。
  - *database_data.json*：用於初始資料庫種子資料的 JSON 格式化資料。
  - *database_data.sql, database_structure.sql*：用於資料庫設置和資料導入的 SQL 文件。

- **project/**：主要的 Django 專案目錄。
  - **middleware/**：用於請求處理的自定義中間件。
    - *webversion.py*：用於處理 Web 版本的中間件。
  - **static/**：靜態文件，如 CSS、JavaScript 和圖片。
    - **css/**、**fonts/**、**img/**、**js/**：用於 CSS 樣式表、自定義字體、圖片和 JavaScript 文件的目錄。
  - **templates/**：用於渲染視圖的 HTML 模板。
  - *settings.py, urls.py, views.py*：Django 設置、URL 配置和視圖定義。

- **story/**：用於管理故事相關功能的 Django 應用。
  - **static/** 和 **templates/**：與故事應用程序相關的靜態文件和 HTML 模板。
  - *models.py, views.py, urls.py*：用於故事管理的模型定義、視圖邏輯和 URL 配置。

- **user/**：用於使用者身份驗證和配置管理的 Django 應用。
  - **static/** 和 **templates/**：用於使用者相關視圖的靜態文件和 HTML 模板。
  - *forms.py, models.py, views.py*：用於使用者管理的表單定義、模型定義和視圖邏輯。

- **utils/**：在整個專案中使用的實用程序函式和輔助工具。
  - *common_utils.py*：常用的輔助函式。

## 開始使用

要開始進行開發：

1. **設置你的環境**：調整 `.env` 的設置以符合你的開發環境。
2. **安裝相依套件**：運行 `pip install -r requirements.txt` 來安裝所需的 Python 套件。
3. **初始化資料庫**：使用 `fixture/database_structure.sql` 中的指令來設置你的資料庫架構。
4. **運行開發伺服器**：執行 `python manage.py runserver` 以啟動 Django 開發伺服器。

## 貢獻指南

- 請參閱 `docs/command_guide.md` 以了解我們的提交訊息慣例。
- 對於新功能或錯誤修正，請建立一個分支並提交拉取請求。
- 確保你的程式碼符合項目的編碼標準並通過所有測試。

## 支援

如有任何問題或問題，請參閱 `docs/talk_to_chatgpt.md` 以獲取通過 ChatGPT 獲取支援的指南，或在項目的問題追踪器中建立一個問題。

本 README 旨在使項目的結構和設置過程盡可能簡單明瞭。無論你是資深開發人員還是剛入門，我們希望這個指南能夠幫助你有效地導航並貢獻到 Fairy Tale Factory 項目中。祝你寫代碼愉快！
