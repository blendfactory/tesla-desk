# TeslaDesk アーキテクチャ

## 方針

**現行案（単一 lib）** を採用する。core / data / features でレイヤーを分けつつ、機能単位でまとめる。

## ディレクトリ構造

```
lib/
  main.dart              # エントリ
  core/                  # 共有（ルーティング・テーマ・定数）
  data/                  # 共通データ層（Tesla API、認証）
    api/
    auth/
  features/              # 機能ごと（vehicle, auth, routines 等）
    <feature>/
      ui/
      # domain/, リポジトリは必要に応じて
```

- **core**: アプリ全体で共有。将来 go_router のルート定義はここに置く。
- **data**: Tesla API クライアント・認証・ローカル永続化。features からはリポジトリ経由でのみ利用する。
- **features**: 各機能は ui/ と必要なら domain やリポジトリを持つ。Tesla API の実装は data に集約する。

## 状態管理・ナビゲーション

- **状態管理**: 最初のドメイン機能実装時に Riverpod を導入する。
- **ナビゲーション**: 画面が 2 つ以上になったら go_router を core で導入する。

## データフロー（将来像）

UI → Riverpod Provider → Repository / UseCase → Tesla API Client（data 層）。ドメインロジックは feature 内の domain または application に置く。

## テスト

- test/ は lib/ と同構造。共通ヘルパーは test/helpers/。
- 単体: ドメイン・data 層を優先。外部はモック。
- ウィジェット: 重要画面から追加。Provider override でモック。
- 統合: 必要に応じて integration_test/ に配置。
