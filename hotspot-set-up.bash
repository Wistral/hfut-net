#!/usr/bin/env bash

cd $(dirname $0)
architecture=$(dpkg --print-architecture)

case "${architecture}" in
    "amd64" | "i386" | "armhf" | "arm64")
        if [ "$architecture" = "arm64" ];
        then architecture="armhf"
        fi
        # package hostapd from http://old-releases.ubuntu.com/ubuntu/pool/universe/w/wpa/
        which ap-hotspot && echo 'Dependency already satisfied!' \
        || (echo 'Dependency not found!' && sudo apt-get install -y dnsmasq \
        && wget -c http://old-releases.ubuntu.com/ubuntu/pool/universe/w/wpa/hostapd_1.0-3ubuntu2.1_${architecture}.deb \
        && wget -c https://launchpad.net/~nilarimogard/+archive/ubuntu/webupd8/+files/ap-hotspot_0.3-1~webupd8~4_all.deb \
        && sudo dpkg -i hostapd_1.0-3ubuntu2.1_${architecture}.deb ap-hotspot_0.3-1~webupd8~4_all.deb \
        && sudo apt-mark hold ap-hotspot \
        && echo "hold ap-hotspot" \
        && sudo apt-get install -fy mpdcron \
        && echo 'Install dependency successfully!')
        echo 'Start hotspot configuration...'
        sudo ap-hotspot configure && echo 'Configuration finished, try to start...'
        sudo ap-hotspot start && echo 'Hotspot starts successfully, enjoy!'
        ;;
    *)
        echo "architecture ${architecture} is not supported yet! 
exit..."
        ;;
esac

