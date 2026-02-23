# Tesla Fleet API 認証サーバー

Tesla Fleet API 用の公開鍵を配信する簡易 HTTP サーバーです。

## 起動方法

プロジェクトルートから:

```bash
python server/server.py
```

または `server` ディレクトリ内で:

```bash
cd server && python server.py
```

- 公開鍵 URL: http://localhost:8080/.well-known/appspecific/com.tesla.3p.public-key.pem
- 公開鍵の配置: `server/well-known/appspecific/README.md` を参照

## 開発時に外部公開する場合

Fleet API の登録（Step 4）では、Tesla が公開鍵の URL にアクセスするため、localhost のままでは登録を完了できません。開発時は [ngrok](https://ngrok.com/) などで localhost:8080 を外部に公開してから、その URL を登録時に指定してください。

```bash
# 別ターミナルで認証サーバーを起動した状態で
ngrok http 8080
```

ngrok が表示する HTTPS の URL（例: `https://xxxx.ngrok-free.app`）の末尾に `/.well-known/appspecific/com.tesla.3p.public-key.pem` を付けたものが、登録用の公開鍵 URL です。
