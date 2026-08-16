# manus-remote-apply-poc

Manus リモート適用 (remote apply) の PoC リポジトリ。

- `calc.py`: テスト対象の小さなモジュール
- `tests/test_calc.py`: 3 つのテスト (`test_add`, `test_mul`, `test_add_negative`)
- CI: GitHub Actions が push / PR ごとに pytest を実行
