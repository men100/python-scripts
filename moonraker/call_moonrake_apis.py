'''
For details, refer https://moonraker.readthedocs.io/en/latest/web_api/
'''
import requests

host_name = "input your printer's host_name (or ip)"

base_url = f"http://{host_name}"

def sendGetRequest(end_point, params=None):
  url = f"http://{host_name}{end_point}"
  print(f"url={url}")
  if params is not None:
    print(f"params={params}")
  response = requests.get(url, params=params) 

  if response.status_code == 200:
    print(response.json())
  else:
    print("Error:", response.status_code)

def sendPostRequest(end_point, json=None):
  url = f"http://{host_name}{end_point}"
  print(f"url={url}")
  response = requests.post(url, json=json)

  if response.status_code == 200:
    print(response.json())
  else:
    print("Error:", response.status_code)

def main():
  print("===== Query Server Info")
  sendGetRequest("/server/info")

  print("===== Get Server Configuration")
  sendGetRequest("/server/config")

#  print("===== Restart Server")
#  sendPostRequest("/server/restart")

  print("===== Get Klippy host information")
  sendGetRequest("/printer/info")

#  print("===== Emergency Stop")
#  sendPostRequest("/printer/emergency_stop")

#  print("===== Host Restart")
#  sendPostRequest("/printer/restart")

#  print("===== Firmware Restart")
#  sendPostRequest("/printer/firmware_restart")
  
  print("===== List available printer objects")
  sendGetRequest("/printer/objects/list")

  print("===== Query printer object status")
  params = {
    "gcode_move": "speed",
    "toolhead": "print_time",
    "extruder": "target,temperature"
  }
  sendGetRequest("/printer/objects/query", params)

  print("===== Query Endstops")
  sendGetRequest("/printer/query_endstops/status")
 
  '''
  print("===== Run a gcode")
  data = {
    "script": "G28" # ホームコマンド
  }
  sendPostRequestJson("/printer/gcode/script", data)
  '''

  print("===== Get System Info")
  sendGetRequest("/machine/system_info")

#  print("===== Shutdown the Operating System")
#  sendPostRequest("/machine/shutdown")

#  print("===== Reboot the Operating System")
#  sendPostRequest("/machine/reboot")

  print("===== Get Moonraker Process Stats")
  sendGetRequest("/machine/proc_stats")

  print("===== List available files")
  sendGetRequest("/server/files/list")

  print("===== List registered roots")
  sendGetRequest("/server/files/roots")

  print("===== Get the Current API Key")
  sendGetRequest("/access/api_key")

  print("===== Get Device List")
  sendGetRequest("/machine/device_power/devices")

if __name__ == "__main__":
    main()
