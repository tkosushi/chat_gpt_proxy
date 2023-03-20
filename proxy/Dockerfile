FROM python:3.11.2-slim-bullseye

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# 各種フォルダの作成
RUN mkdir -p /var/cache/nginx && \
    mkdir -p /var/run \
    mkdir /var/log/nginx

# nginxユーザーの追加と権限の設定
RUN adduser --system --no-create-home --group nginx \
    && chown nginx:nginx /var/cache/nginx \
    && chown nginx:nginx /var/run \
    && chown nginx:nginx /var/log/nginx

# nginxの設定ファイルをコピー
COPY workdir/nginx.conf /etc/nginx/nginx.conf

# Pythonの依存関係をインストール
COPY workdir/requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# workdirの中身を全部/appにコピー
COPY workdir/ /app/

CMD ["nginx", "-g", "daemon off;"]