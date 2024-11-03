# HIEI API リファレンス

## コアモジュール

### KeyLogger

キー入力を監視・記録するクラス。

```python
from hiei.core import KeyLogger

logger = KeyLogger()
logger.start()
```

#### メソッド

- `start()`: キーロギングを開始
- `stop()`: キーロギングを停止
- `get_buffer()`: 現在のバッファを取得

### ClipboardMonitor

クリップボードの変更を監視するクラス。

```python
from hiei.core import ClipboardMonitor

monitor = ClipboardMonitor()
monitor.start()
```

#### メソッド

- `start()`: 監視を開始
- `stop()`: 監視を停止
- `get_history()`: クリップボード履歴を取得

### ActivityMonitor

全体の活動を監視・制御するクラス。

```python
from hiei.core import ActivityMonitor

monitor = ActivityMonitor()
monitor.start()
```

#### メソッド

- `start()`: 監視を開始
- `stop()`: 監視を停止
- `status()`: 現在の状態を取得

## プロセッサモジュール

### TextProcessor

テキストデータを処理するクラス。

```python
from hiei.processors import TextProcessor

processor = TextProcessor()
entities = processor.extract_entities(text)
```

#### メソッド

- `extract_entities(text)`: エンティティを抽出
- `sanitize(text)`: テキストをサニタイズ
- `summarize(text, max_length)`: テキストを要約

### ActivityProcessor

活動データを処理・分析するクラス。

```python
from hiei.processors import ActivityProcessor

processor = ActivityProcessor()
summary = processor.get_session_summary()
```

#### メソッド

- `process_keystroke(key_data)`: キーストロークを処理
- `process_clipboard(clipboard_data)`: クリップボードデータを処理
- `get_session_summary()`: セッションサマリーを取得

## ストレージモジュール

### ActivityDatabase

活動データを永続化するクラス。

```python
from hiei.storage import ActivityDatabase

db = ActivityDatabase()
db.store_activity("keystroke", content="example")
```

#### メソッド

- `store_activity(activity_type, content, metadata)`: 活動を記録
- `get_recent_activities(limit)`: 最近の活動を取得

### LocalStorage

ローカルファイルストレージを管理するクラス。

```python
from hiei.storage import LocalStorage

storage = LocalStorage()
storage.save_json("config.json", data)
```

#### メソッド

- `save_json(filename, data)`: JSONとして保存
- `load_json(filename)`: JSONを読み込み

## セキュリティモジュール

### Encryptor

データの暗号化を行うクラス。

```python
from hiei.security import Encryptor

encryptor = Encryptor()
encrypted = encryptor.encrypt("sensitive data")
```

#### メソッド

- `encrypt(data)`: データを暗号化
- `decrypt(encrypted_data)`: データを復号化

### SensitiveDataFilter

センシティブデータをフィルタリングするクラス。

```python
from hiei.security import SensitiveDataFilter

filter = SensitiveDataFilter()
is_sensitive = filter.contains_sensitive_data(text)
```

#### メソッド

- `contains_sensitive_data(text)`: センシティブデータの検出
- `mask_sensitive_data(text)`: センシティブデータのマスク
- `add_pattern(name, pattern)`: 検出パターンの追加
