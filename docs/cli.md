# HIEIコマンドラインインターフェース

## コマンド一覧

### 基本コマンド

#### `hiei start`
監視を開始します。

```bash
# 基本的な使用方法
hiei start

# オプション
--daemon        # バックグラウンドで実行
--config FILE   # 設定ファイルを指定
--debug         # デバッグモードで実行
```

#### `hiei stop`
監視を停止します。

```bash
hiei stop
```

#### `hiei status`
現在の状態を表示します。

```bash
hiei status
```

### 設定管理

#### `hiei config`
設定の管理を行います。

```bash
# 設定を表示
hiei config show

# 設定を編集
hiei config edit

# 設定をリセット
hiei config reset
```

### データ管理

#### `hiei report`
アクティビティレポートを生成します。

```bash
# 基本的な使用方法
hiei report

# オプション
--format FORMAT  # 出力フォーマット（text, json, html）
--from DATE      # 開始日
--to DATE        # 終了日
```

#### `hiei export`
データをエクスポートします。

```bash
# 基本的な使用方法
hiei export OUTPUT_FILE

# オプション
--format FORMAT  # エクスポート形式（json, csv）
--encrypt       # エクスポートデータを暗号化
```

### セキュリティ

#### `hiei security`
セキュリティ設定を管理します。

```bash
# 暗号化キーの生成
hiei security generate-key

# フィルターの管理
hiei security filters list
hiei security filters add PATTERN
hiei security filters remove PATTERN
```

## 環境変数

- `HIEI_CONFIG`: 設定ファイルのパス
- `HIEI_LOG_LEVEL`: ログレベル（DEBUG, INFO, WARNING, ERROR）
- `HIEI_DATA_DIR`: データディレクトリのパス
- `HIEI_ENCRYPTION_KEY`: 暗号化キー（非推奨、設定ファイルを使用してください）

## 終了コード

- 0: 成功
- 1: 一般的なエラー
- 2: 設定エラー
- 3: 権限エラー
- 4: ランタイムエラー
