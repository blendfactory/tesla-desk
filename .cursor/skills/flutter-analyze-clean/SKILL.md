---
name: flutter-analyze-clean
description: Runs mise exec -- flutter analyze after Dart/Flutter changes and fixes until zero issues. Use when editing or adding Dart files, when the user asks to analyze or fix analyzer warnings, or before committing Dart changes.
---

# Flutter Analyze — 警告 0 を維持する

Dart/Flutter のコードを変更したあと、コミット前に必ず解析を通し、エラー・警告を 0 件にする。

## 手順

1. **実行**: プロジェクトルートで `mise exec -- flutter analyze` を実行する。Flutter コマンドは必ず `mise exec -- flutter` で実行する。
2. **確認**: 出力に `No issues found!` が出るまで修正する。エラー・警告・info のいずれも残さない。
3. **修正**: 指摘されたファイル・行に従って修正する。リンター提案（`// ignore` など）は、本当に必要な場合のみ使い、まずはコードを直すことを優先する。
4. **再実行**: 修正のたびに `mise exec -- flutter analyze` を再実行し、0 件になることを確認する。

## タイミング

- Dart ファイル（`lib/`, `test/` 内の `.dart`）を編集・追加したあと。
- ユーザーが「分析して」「リント直して」などと言ったとき。
- コミットする直前（AGENTS.md の作業の進め方に従う）。

## 注意

- 生成ファイル（`.g.dart`, `.freezed.dart` など）は編集しない。生成元を修正してから `build_runner` 等で再生成する。
