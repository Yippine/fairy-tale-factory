# 啟動 Docker Compose 配置文件中定義的所有容器
# -d 選項表示在背景執行它們
docker compose up -d --build

# 將應用所有未應用的遷移到您的資料庫
docker-compose exec web python manage.py migrate
