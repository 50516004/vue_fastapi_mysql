### コンテナの起動
```
docker compose up -d
```
### 各サービスのURL
- WEB：http://localhost:3000
- API：http://localhost:8000
- DB：localhost:3307

### コンテナの削除
```
docker compose down
```
### コンテナに入る
```
docker exec -it [コンテナ名] sh
```
### ログを確認
```
docker logs [コンテナ名]
```
### SQLを実行
```
cmd /c "docker exec -i db mysql -u root -proot < ./sql/[SQLファイル]"
```
