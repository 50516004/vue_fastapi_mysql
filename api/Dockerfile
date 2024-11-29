# ベースイメージとしてpythonの公式イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# ライブラリの記述ファイルをコンテナ内にコピー
COPY requirements.txt .

# ライブラリをインストール
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# アプリケーションプログラムをコピー
COPY ./app/ .

# 開発サーバの起動をデフォルト実行
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
