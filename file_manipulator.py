import sys
import os

def validate_args(args, expected_args):
    """引数の数とファイルの存在を検証"""
    if len(args) != expected_args:
        print(f"Error: {args[1]} コマンドには {expected_args} つの引数が必要です。")
        sys.exit(1)
    if not os.path.exists(args[2]):
        print(f"Error: {args[2]} ファイルが見つかりません。")
        sys.exit(1)

def get_int(n):
    """数値の入力を受け取り、整数にして返す"""
    try:
        return int(n)
    except ValueError:
        print("Error: 整数を入力してください。")
        sys.exit(1)

def reverse_file(input_path, output_path):
    """ファイルの内容を逆にしたファイルを作成"""
    with open(input_path, "r") as f:
        content = f.read()
    with open(output_path, "w") as f:
        f.write(content[::-1])

def copy_file(input_path, output_path):
    """ファイルのコピーを作成"""
    with open(input_path, "r") as f:
        content = f.read()
    with open(output_path, "w") as f:
        f.write(content)

def duplicate_contents(input_path, n):
    """ファイルの複製を作成"""
    with open(input_path, "r") as f:
        content = f.read()
    n = get_int(n)
    duplicated_contents = content * n
    with open(input_path, "w") as f:
        f.write(duplicated_contents)

def replace_string(input_path, needle, newstring):
    """ファイルの内容から文字列を検索し、置き換え"""
    with open(input_path, "r") as f:
        content = f.read()
    content = content.replace(needle, newstring)
    with open(input_path, "w") as f:
        f.write(content)

def main():
    command = sys.argv[1]

    if command == "reverse":
        validate_args(sys.argv, 4)
        reverse_file(sys.argv[2], sys.argv[3])

    elif command == "copy":
        validate_args(sys.argv, 4)
        copy_file(sys.argv[2], sys.argv[3])

    elif command == "duplicate-contents":
        validate_args(sys.argv, 4)
        duplicate_contents(sys.argv[2], sys.argv[3])

    elif command == "replace-string":
        validate_args(sys.argv, 5)
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    
    else:
        print(f"Error: {command} というコマンドは存在しません。")
        sys.exit(1)

if __name__ == "__main__":
    main()