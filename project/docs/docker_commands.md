# Docker Commands Full Guide

## 使用 Docker Compose 啟動你的應用容器
```bash
docker-compose up -d --build
```
- `-d`：在背景運行。
- `--build`：如果有必要，重新構建容器。

## 停止並移除容器、網路、映像和卷
```bash
docker-compose down
```
- 用於停止並移除所有由 `docker-compose up` 啟動的資源。

## 拉取 MySQL 映像
```bash
docker pull mysql:8
```
- 拉取 MySQL 8 版本的官方 Docker 映像。

## 查看所有運行中的容器
```bash
docker ps
```
- 查看當前所有運行中的 Docker 容器。

## 停止運行中的容器
```bash
docker stop <container_id>
```
- `<container_id>`：替換為容器的 ID。

## 移除容器
```bash
docker rm <container_id>
```
- 移除指定的 Docker 容器。

## 查看本地所有 Docker 映像
```bash
docker images
```
- 列出本地所有的 Docker 映像。

## 移除 Docker 映像
```bash
docker rmi <image_id>
```
- `<image_id>`：替換為映像的 ID。


## 使用 Docker Compose 執行 Django 程式資料庫遷移命令
```bash
docker-compose exec web python manage.py migrate
```
- 在 Docker Compose 環境中執行 Django 程式的資料庫遷移命令。

## 進入運行中的容器內部（交互式方式）
```bash
docker exec -it <container_id> bash
```
- `<container_id>`：替換為容器的 ID。
- 這將以交互式方式進入容器的命令行界面。

## 進入運行中的 MySQL 容器並使用指定的用戶名進行登錄
```bash
docker exec -it <container_id> mysql -u <user_name> -p
```
- `<container_id>`：替換為 MySQL 容器的 ID。
- `<user_name>`：替換為要使用的 MySQL 用戶名。
- 這將以交互式方式進入 MySQL 容器並使用指定的用戶名登錄 MySQL。
- 登錄後，系統將提示您輸入密碼以完成登錄。
