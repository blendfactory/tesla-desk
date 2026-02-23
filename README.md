# Tesdesk

Tesdesk は Tesla API の上に構築された **vehicle intelligence platform** です。車両状態の一元管理、コマンド実行、行動の自動化を、ローカルな統合コントロールシステムに集約します。

**ロングタームのビジョン**: スマートルーティン（カレンダー・天気に基づくプリコンディショニング等）、エネルギー分析、走行行動のインサイト、コスト最適化のトラッキング、ホームオートメーション連携。プログラム可能な「車両の脳」へと進化させることを目指します。

## 必要な環境

- [mise](https://mise.jdx.dev/)（Flutter のバージョン管理・実行は `mise exec -- flutter` で行う）
- Flutter SDK 3.11+
- Dart 3.11+
- 現状のビルドターゲット: macOS

## セットアップ

Flutter コマンドは **mise** でバージョン管理する想定です。必ず `mise exec -- flutter` で実行してください。

```bash
mise exec -- flutter pub get
```

初回ビルド（macOS）:

```bash
mise exec -- flutter run -d macos
```

## Tesla Fleet API 認証サーバー

Tesla Fleet API の公開鍵を配信する簡易 HTTP サーバーが `server/` にあります。Fleet API の登録（Step 3 以降）で、公開鍵を URL で提供するために利用します。

```bash
python server/server.py
```

起動後、公開鍵は次の URL で配信されます。

- http://localhost:8080/.well-known/appspecific/com.tesla.3p.public-key.pem

公開鍵の生成・配置手順は [server/README.md](server/README.md) および [server/well-known/appspecific/README.md](server/well-known/appspecific/README.md) を参照してください。開発時に Fleet API へ登録する場合は、ngrok などで localhost を外部公開する必要があります（詳細は [server/README.md](server/README.md)）。

## よく使うコマンド

| コマンド | 説明 |
|----------|------|
| `mise exec -- flutter run -d macos` | macOS でアプリを起動 |
| `mise exec -- flutter test` | テストを実行 |
| `mise exec -- flutter analyze` | 静的解析（エラー・警告 0 を維持する） |

## ディレクトリ構成

- `lib/` — アプリの Dart ソース（エントリは `main.dart`）
- `macos/` — macOS ネイティブプロジェクト
- `server/` — Tesla Fleet API 用の認証サーバー（公開鍵配信）
- `test/` — 単体・ウィジェットテスト
- `pubspec.yaml` — 依存関係と Flutter 設定
- `analysis_options.yaml` — Dart 解析・リント設定

## Getting Started

Flutter の初めてのプロジェクトの場合:

- [Learn Flutter](https://docs.flutter.dev/get-started/learn-flutter)
- [Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Flutter learning resources](https://docs.flutter.dev/reference/learning-resources)

[オンラインドキュメント](https://docs.flutter.dev/) でチュートリアルや API リファレンスを参照できます。
