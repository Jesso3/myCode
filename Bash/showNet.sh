#!/bin/zsh
bettercap -iface en0 -eval "net.probe on; sleep 1; net.show; quit"

