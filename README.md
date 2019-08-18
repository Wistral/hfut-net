# HFUT-NET

Python scripts to auto-connect to Internet for school net of HFUT of XC
### Connect to Internet via school net
- #### Dependency
    ```sh
    sudo apt-get install -y python3-pip
    sudo pip3 install requests beautifulsoup4
    ```
- #### Connect
    ```sh
    python3 identify.py [wired | wireless]
    ```

    If you don't know to choose whether wired or wireless, just run `python3 identify.py`.
### Set up hotspot
```sh
bash hotspot-set-up.bash
```
May not suit for non-debian or other rare OS like `RPi OS`.