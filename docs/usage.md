# HIEI使用ガイド

## 概要

HIEIは、PC作業を記録し、LLMと連携することで効率的な作業環境を実現する個人アシスタントツールです。プライバシーとセキュリティを重視しながら、作業内容を安全に記録・分析します。

## インストール

```bash
# Poetryを使用してインストール（推奨）
poetry add hiei

# または、pipを使用してインストール
pip install hiei
```

## 基本的な使用方法

### 1. 監視の開始

```bash
# 基本的な監視を開始
hiei start

# バックグラウンドで実行
hiei start --daemon
```

### 2. 設定のカスタマイズ

```bash
# 設定ファイルを編集
hiei config edit

# 設定を確認
hiei config show
```

### 3. データの確認

```bash
# アクティビティの概要を表示
hiei status

# 詳細なレポートを生成
hiei report
```

## セキュリティ設定

### センシティブデータの保護

1. `.hiei/config.yml`で保護するパターンを定義
2. 暗号化キーの設定
3. フィルタリングルールのカスタマイズ

```yaml
security:
  encryption:
    enabled: true
    key_file: ~/.hiei/key.enc
  filters:
    - pattern: "\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
      name: "credit_card"
    - pattern: "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
      name: "email"
```

## データストレージ

記録されたデータは以下の場所に保存されます：

- アクティビティデータ: `~/.hiei/data/activities.db`
- ログファイル: `~/.hiei/logs/`
- 設定ファイル: `~/.hiei/config.yml`

## トラブルシューティング

### よくある問題

1. 監視が開始されない
   - 権限の確認
   - プロセスの競合確認

2. データが記録されない
   - ストレージ容量の確認
   - フィルタリング設定の確認

3. パフォーマンスの問題
   - リソース使用量の確認
   - ログレベルの調整

### ログの確認

```bash
# ログファイルの確認
cat ~/.hiei/logs/hiei.log

# デバッグモードでの実行
hiei start --debug
