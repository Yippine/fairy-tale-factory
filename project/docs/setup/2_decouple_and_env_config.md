# 專案說明文件

## 專案更新

最新版本更新內容如下：

- 移除了兩個 Docker 文件，改為使用 decouple 庫進行設定。
- 將資料庫設定轉移到與 manage.py 同一層的 .env 檔案中。
- 使用者需要安裝 decouple 庫，可以透過指令 `pip install decouple` 進行安裝，或者執行 `pip install -r requirements.txt` 安裝專案所需的所有套件。

## 資料庫設定

在使用本專案前，請確保在 `.env` 檔案中填寫正確的資料庫設定。以下是一個範例 `.env` 檔案內容（請將帳號和密碼更換為您的資訊）：

```bash
MYSQL_DATABASE=fairy_tale_factory
MYSQL_USER=你的資料庫使用者名稱
MYSQL_PASSWORD=你的資料庫使用者密碼
MYSQL_ROOT_PASSWORD=你的資料庫根使用者密碼
DB_HOST=
DB_PORT=
```

請注意，DB_HOST 和 DB_PORT 可根據您的實際情況填寫或留空。

## 注意事項

- 使用本專案前，請確保已安裝 `decouple` 庫。
- 請確保在 `.env` 檔案中填寫正確的資料庫設定。
