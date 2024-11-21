#!/bin/bash

PORT="/dev/ttyUSB0"
CAN_INTERFACE="can0"
BITRATE="500000"

if sudo modprobe slcan; then
    echo "[+] modeprobe slcan success.."
else
    echo "[-] modeprobe slcan failed!"
    exit 1
fi


if sudo slcand -o -c $PORT $CAN_INTERFACE; then
    echo "[+] slcan $PORT started to $CAN_INTERFACE"
else
    echo "[-] slcan is not started!"
    exit 1
fi


if sudo ip link set $CAN_INTERFACE up type can bitrate $BITRATE; then
    echo "[+] $CAN_INTERFACE set to $BITRATE bitrate.."
else
    echo "[-] $CAN_INTERFACE is not set!"
    exit 1
fi
