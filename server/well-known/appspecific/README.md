# Tesla Fleet API 公開鍵の配置場所

このディレクトリに **Tesla Fleet API 用の公開鍵** を配置してください。

## ファイル名

- **必須**: `com.tesla.3p.public-key.pem`

## 手順

1. プロジェクトルートまたは `server/` で秘密鍵・公開鍵を生成（秘密鍵はリポジトリに含めない）:
   ```bash
   openssl ecparam -name prime256v1 -genkey -noout -out private-key.pem
   openssl ec -in private-key.pem -pubout -out public-key.pem
   ```

2. 公開鍵をこのディレクトリに所定の名前で配置:
   ```bash
   cp public-key.pem server/well-known/appspecific/com.tesla.3p.public-key.pem
   ```

3. 認証サーバーを起動すると、次の URL で公開鍵が配信されます:
   ```
   http://localhost:8080/.well-known/appspecific/com.tesla.3p.public-key.pem
   ```

## 注意

- `private-key.pem` は `.gitignore` によりコミット対象外です。ローカルで厳重に管理してください。
- 公開鍵（`com.tesla.3p.public-key.pem`）はリポジトリに含めて問題ありません。
