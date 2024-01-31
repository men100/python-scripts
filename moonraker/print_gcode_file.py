'''
For details, refer https://moonraker.readthedocs.io/en/latest/web_api/
'''
import os
import argparse
import requests

host_name = "input your printer's host_name (or ip)"

base_url = f"http://{host_name}"

def fileUpload(filename, path):
  url = f"{base_url}/server/files/upload"
  files = {
    'file': (filename, open(path, 'rb'))
  }

  response = requests.post(url, files=files)

  # resource が生成されたときは 201 を返す
  if response.status_code in [200, 201]:
    print(response.json())
  else:
    print("Error:", response.status_code)
    exit(1)

def printFileRemotely(filename):
  url = f"{base_url}/printer/print/start"
  json = {
    'filename': filename
  }

  response = requests.post(url, json=json)

  if response.status_code == 200:
    print(response.json())
  else:
    print("Error:", response.status_code)
    exit(1)

def main():
  parser = argparse.ArgumentParser(description="upload gcode and print")
  parser.add_argument("path", help="upload gcode file path")
  args = parser.parse_args()

  path = args.path
  if not os.path.exists(path):
    print(f"file({path}) is not exist.")
    exit(1)
  filename = os.path.basename(path)

  # ファイルをアップロード
  fileUpload(filename, path)

  # ファイルを印刷
  printFileRemotely(filename)

if __name__ == "__main__":
    main()
