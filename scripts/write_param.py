#!/usr/bin/env python
import os, sys


template = """
{{
  "ClockSpeed": 1,
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "ViewMode": "SpringArmChase",
  "Vehicles": {{
    "Drone_{}": {{
      "VehicleType": "SimpleFlight",
      "Sensors": {{
        "imu_1": {{
          "SensorType": 2,
          "Enabled": true
        }}
      }},
      "AllowAPIAlways": false,
      "Cameras": {{
        "leftcamera_1": {{
          "CaptureSettings": [
            {{
              "ImageType": 1,
              "Width": 640,
              "Height": 480,
              "FOV_Degrees": 90,
              "TargetGamma": 1.5
            }}
          ],
          "X": 0.35, "Y": -0.05, "Z": -0.1,
          "Pitch": 0, "Roll": 0, "Yaw": 0
        }}
      }},
      "X": 0, "Y": 0, "Z": 0,
      "Pitch": 0, "Roll": 0, "Yaw": 0
      }}
    }}
}}
"""

if __name__ == "__main__":
    from os.path import expanduser
    home = expanduser("~")
    _id = sys.argv[1]
    f = open(home + "/Documents/AirSim/settings.json", "w")
    f.write(template.format(_id))
    f.close()