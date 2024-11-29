# ベースイメージとして公式のNodeイメージを使用
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションプログラムをコピー
COPY ./app/ .

# パッケージをインストール
RUN npm install

# 開発サーバの起動をデフォルト実行
CMD ["npm", "run", "dev"]

