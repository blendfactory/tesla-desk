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
