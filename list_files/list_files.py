import os
import argparse

def list_files(directory, relative=False):
    # 指定されたディレクトリが存在するか確認
    if not os.path.exists(directory):
        print(f"not exist directory '{directory}'")
        return

    # ディレクトリとそのサブディレクトリ内のファイルを列挙
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if relative:
                # 相対パスで出力
                print(".\\" + os.path.relpath(filepath, directory))
            else:
                # 完全パスで出力
                print(filepath)

def main():
    parser = argparse.ArgumentParser(description="list files for specified directory and sub directory")
    parser.add_argument("directory", help="target directory")
    parser.add_argument("--relative", action="store_true", help="print relative path")
    args = parser.parse_args()

    list_files(args.directory, args.relative)

if __name__ == "__main__":
    main()
