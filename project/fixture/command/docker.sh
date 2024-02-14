# 使用 Docker Compose 啟動你的應用容器
# -d 背景運行
# --build 重新構建容器
docker compose up -d --build

# 在 Docker 容器中運行 Django 的資料庫遷移指令，確保容器中的資料庫與你的應用同步
docker-compose exec web python manage.py migrate

# 拉取 mysql 映像
docker pull mysql:8

# 進入 Docker 容器的命令行環境，可以在其中執行各種操作
docker exec -it <container id> bash

# 進入 MySQL 容器的 MySQL 命令行環境，可以在其中執行各種操作
# <user name> 為資料庫用戶名
# 按下 Enter 後需要輸入密碼以登入 MySQL
docker exec -it <container id> mysql -u <user name> -p
