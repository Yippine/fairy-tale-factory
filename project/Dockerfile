# 使用官方 Python 3.9 基礎鏡像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統依賴，這些依賴是 mysqlclient 需要的
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential libssl-dev libffi-dev python3-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# 將 requirements.txt 複製到容器中
COPY requirements.txt /app/

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 將當前目錄內容複製到容器中的 /app
COPY . /app

# 設定環境變量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 暴露容器的 8000 端口
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
