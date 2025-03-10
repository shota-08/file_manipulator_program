# 📝 ファイル操作スクリプト (File Manipulation Script)

## 📖 概要
- コマンドラインから実行することでファイルの操作を簡単に行うツールです。
- 以下の機能をサポートしています。
    - ファイルの内容を逆順にする
    - ファイルをコピーする
    - ファイルの内容を複製する
    - 指定した文字列を置換する

## 🚀 使い方

このスクリプトはコマンドラインから実行できます。以下の形式で使用してください。
```
python script.py <command> <input_file> [args]
```

### 1. ファイルの内容を逆順にする
input.txt の内容を逆順にして output.txt に保存します。
```
python script.py reverse input.txt output.txt
```

### 2. ファイルをコピーする
input.txt の内容を output.txt にコピーします。
```
python script.py copy input.txt output.txt
```

### 3. ファイルの内容を複製する
input.txt の内容を N 回繰り返して上書きします。
```
python script.py duplicate-contents input.txt N
```

### 4. 文字列を置換する
input.txt の中の "old_string" を "new_string" に置き換えます。
```
python script.py replace-string input.txt "old_string" "new_string"
```

## 🛠 コードの説明
### 1. validate_args(args, expected_args)
- コマンドの引数が正しいかチェック。
- 指定したファイルが存在しない場合はエラーを表示。
### 2. reverse_file(input_path, output_path)
- input_path の内容を逆順にし、output_path に書き込む。
### 3. copy_file(input_path, output_path)
- input_path の内容をそのまま output_path にコピー。
### 4. duplicate_contents(input_path, n)
- input_path の内容を n 回繰り返して書き込む。
### 5. replace_string(input_path, needle, newstring)
- input_path の中で needle を newstring に置き換える。

