ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CH

network={
        ssid="my SSID"
        psk="my password"
        key_mgmt=WPA-PSK
        id_str="mywlan0"
}

network={
        ssid="my SSID"
        psk="my password"
        key_mgmt=WPA-PSK
        id_str="mywlan1"
}

