# CodeReview 定義 — manus-remote-apply-poc

## 対象

- リポジトリ全体 (`calc.py`, `tests/`, `README.md`, `.github/workflows/`)
- 除外: なし

## 観点

| # | 観点 | 証拠ソース | 検証手順 |
|---|------|-----------|---------|
| 1 | README のテスト記述が実テストと一致するか | `README.md`, `tests/test_calc.py` | README が列挙するテスト関数名・件数と `tests/test_calc.py` の `test_*` 関数定義を実測比較する。過不足・名称不一致は指摘する。 |
| 2 | calc.py の公開関数にテストがあるか | `calc.py`, `tests/test_calc.py` | `calc.py` の各関数を走査し、対応する `test_*` があるか確認する。無いものは指摘する。 |

## 出力

- 各観点ごとに 判定 (true/partial/false)・根拠 (file:line)・修正方針を示す。
- 集約: 指摘ゼロなら クリーン、1 つでもあれば 要修正。

## 修正方針の指定

- ドキュメント側 (README) を実態 (コード) に合わせる方向で修正する。コードを README に合わせない。
