#!/usr/bin/python3

# Appends '-opn' to the firmware output filename so OPNMeshCore builds are
# distinguishable from upstream MeshCore firmware files.
# FIRMWARE_VERSION is handled directly in the source headers.

Import("env")

env.Replace(PROGNAME=env["PROGNAME"] + "-opn")
