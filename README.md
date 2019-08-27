# HFUT-NET

Python scripts to auto-connect to Internet for school net of HFUT of XC
### Connect to Internet
```sh
python3 identify.py [wired | wireless]
```

### Set up hotspot
```sh
bash hotspot-set-up.bash
```

### Build release
- Dependency
  - requests
  - beautifulsoup4
  - pyinstaller
  `pip install pyinstaller beautifulsoup4 requests`
- command
  ```sh
   pyinstaller -F identify.py -n hfut-net --icon ~/Pictures/university_128px_1147037_easyicon.net.ico
   ```