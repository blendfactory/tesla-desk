import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// テスト用に [child] を MaterialApp でラップして pump する。
/// ウィジェットテストで Theme や Navigator が必要なときに使う。
Future<void> pumpApp(
  WidgetTester tester, {
  required Widget child,
  ThemeData? theme,
}) async {
  await tester.pumpWidget(
    MaterialApp(
      theme: theme,
      home: child,
    ),
  );
}
