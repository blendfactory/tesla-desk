---
name: conventional-commits
description: Generates Conventional Commits style commit messages from staged changes. Defines when to commit (appropriate timing) and how to split commits (appropriate granularity). Use when writing or suggesting commit messages, or when the user asks about commit timing or splitting commits.
---

# Conventional Commits — メッセージ生成とコミット方針

ステージ済みの変更から Conventional Commits 形式のメッセージを生成する。あわせて、**いつコミットするか**と**どの粒度で分けるか**の判断基準に従う。

## メッセージ形式

```
<型>[任意 スコープ]: <タイトル>

[任意 本文]
```

- **型** (必須): `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` など。小文字。
- **スコープ** (任意): 括弧で囲む（例: `(auth)`, `(parser)`）。
- **タイトル**: 変更の短い要約。 imperative で書く（「〇〇する」）。

## いつコミットするか（適切なタイミング）

- 論理的にひと区切りついたときだけコミットする。
  - 例: 1 機能の実装が完了した、1 つのバグ修正が完了した、`mise exec -- flutter analyze` が通ったあと。
- 長時間の変更をため込まない。作業の区切りごとにコミットする。
- 未完成の変更はコミットしない（ビルド・解析が通る単位で切る）。

## どの粒度で分けるか（適切な単位）

- **1 コミット = 1 つの論理的な変更**にする。
- 複数の機能・複数の修正・無関係な変更を 1 コミットにまとめない。
- 複数の変更がある場合は、可能な限り複数コミットに分ける（例: リファクタと機能追加は別コミット）。

## メッセージ生成の流れ

1. `git diff --staged` でステージ済み変更を確認する。
2. 変更内容から「型」と「スコープ」を決める。
3. タイトルを 1 文で要約する（日本語可）。本文は必要なときだけ書く。
4. 1 つのコミットに複数の論理的な変更が含まれている場合は、ユーザーに「分割した方がよい」と伝え、単位ごとにメッセージを提案する。

## 例

| 変更の内容 | メッセージ例 |
|------------|--------------|
| 新機能追加 | `feat: 車両状態を一覧表示する画面を追加` |
| バグ修正 | `fix(auth): トークン期限切れ時のクラッシュを修正` |
| リントのみ | `style: dart format と analyzer 指摘を修正` |
| ドキュメント | `docs: AGENTS.md にコミット方針を追記` |
