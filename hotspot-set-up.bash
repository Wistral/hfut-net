#!/bin/bash

architecture=$(dpkg --print-architecture)
# package hostapd from http://old-releases.ubuntu.com/ubuntu/pool/universe/w/wpa/
which ap-hotspot && echo 'Dependency already satisfied!' \
|| (echo 'Dependency not found!' && sudo apt-get install -y dnsmasq \
&& sudo dpkg -i hostapd*${architecture}.deb \
&& sudo apt-get install -y ap-hotspot \
&& echo 'Install dependency successfully!')
echo 'Start hotspot configuration'
sudo ap-hotspot configure && echo 'Configuration finished, try to start...'
sudo ap-hotspot start

