# ベースイメージとして公式のNode.jsイメージを使用
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app

# Vue CLIをグローバルにインストール（初期設定で便利）
RUN npm install -g @vue/cli

# 必要なポートを公開
EXPOSE 5173

# シェルをデフォルトコマンドに設定
CMD ["sh"]

