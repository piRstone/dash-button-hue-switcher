#!/usr/bin/env python3
import time
from argparse import ArgumentParser
from scapy.all import *
from qhue import Bridge

parser = ArgumentParser(description="Listener for Amazon Dash Button presses")
parser.add_argument("bridge_ip", help="IP address of the Philips Hue Bridge")
parser.add_argument("username", help="Username of the Amazon Dash Button device")
parser.add_argument("mac_address", help="MAC address of the Amazon Dash Button")

args = parser.parse_args()
dash_mac_address = args.mac_address
bridge_ip = args.bridge_ip
username = args.username

# Connect to Hue to bridge
b = Bridge(bridge_ip, username)

execute = True

# Hue lights
lights = b.lights()

def arp_display(pkt):
    global execute, light_state
    print(pkt[ARP].op)
    print(pkt[ARP].hwsrc)

    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == dash_mac_address:
            if execute:
                for attr in lights:
                    light = b.lights[attr]
                    state = light().get(u'state').get(u'on')
                    if state:
                        light.state(on=False)
            execute = not execute

sniff(prn=arp_display, filter="arp", store=0, count=0)
