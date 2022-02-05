import logging
import socket
import random
from time import sleep
 
_LOGGER = logging.getLogger(__name__)
 
DOMAIN = 'c4_services'

# Variables
ip_address = "192.168.X.XXX"
 
def send_udp_command(command, host, port):
    COUNTER = "0s2a" + str(random.randint(10, 99))
    COMMAND = COUNTER + " " + command + " \r\n"
    _LOGGER.warn("Sending command: %s", COMMAND)
    HOST = host
    PORT = port
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto( bytes(COMMAND, "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    _LOGGER.warn("Command sent. Response: %s", str(received))
    
def setup(hass, config):
    
    # Zone 1
    
    def handle_zone1_amp_off_select(call):
        #_LOGGER.warn("Powering AMP Off...")
        send_udp_command("c4.amp.out 01 00", ip_address, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zone1_amp_on_select(call):
        #_LOGGER.warn("Powering AMP On...")
        amp_input = hass.states.get("input_select.zone1_amp_input").state[:1]
        tuner_station = hass.states.get("input_select.zone1_radio_stations").state
        send_udp_command("c4.amp.chvol 01 a9", ip_address, 8750)
        send_udp_command("c4.amp.out 01 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("AMP Powered On...")
        
    def handle_zone1_amp_volume_select(call):
        #_LOGGER.warn("Changing amp volume...")
        volume_select = hass.states.get("input_number.zone1_amp_volume").state
        volume_select = int(float(volume_select) * 100) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 01 " + volume_select, ip_address, 8750)
        #_LOGGER.warn("Volume set...")
        
    def handle_zone1_amp_input_select(call):
        #_LOGGER.warn("Changing amp input...")
        amp_input = hass.states.get("input_select.zone1_amp_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 01 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("Amp input changed...")
        
        # Zone 2
        
    def handle_zone2_amp_off_select(call):
        #_LOGGER.warn("Powering AMP Off...")
        send_udp_command("c4.amp.out 02 00", ip_address, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zone2_amp_on_select(call):
        #_LOGGER.warn("Powering AMP On...")
        amp_input = hass.states.get("input_select.zone2_amp_input").state[:1]
        tuner_station = hass.states.get("input_select.zone2_radio_stations").state
        send_udp_command("c4.amp.chvol 02 a9", ip_address, 8750)
        send_udp_command("c4.amp.out 02 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("AMP Powered On...")
        
    def handle_zone2_amp_volume_select(call):
        #_LOGGER.warn("Changing amp volume...")
        volume_select = hass.states.get("input_number.zone2_amp_volume").state
        volume_select = int(float(volume_select) * 100) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 02 " + volume_select, ip_address, 8750)
        #_LOGGER.warn("Volume set...")
        
    def handle_zone2_amp_input_select(call):
        #_LOGGER.warn("Changing amp input...")
        amp_input = hass.states.get("input_select.zone2_amp_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 02 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("Amp input changed...")
        
         # Zone 3
        
    def handle_zone3_amp_off_select(call):
        #_LOGGER.warn("Powering AMP Off...")
        send_udp_command("c4.amp.out 03 00", ip_address, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zone3_amp_on_select(call):
        #_LOGGER.warn("Powering AMP On...")
        amp_input = hass.states.get("input_select.zone3_amp_input").state[:1]
        tuner_station = hass.states.get("input_select.zone2_radio_stations").state
        send_udp_command("c4.amp.chvol 03 a9", ip_address, 8750)
        send_udp_command("c4.amp.out 03 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("AMP Powered On...")
        
    def handle_zone3_amp_volume_select(call):
        #_LOGGER.warn("Changing amp volume...")
        volume_select = hass.states.get("input_number.zone3_amp_volume").state
        volume_select = int(float(volume_select) * 100) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 03 " + volume_select, ip_address, 8750)
        #_LOGGER.warn("Volume set...")
        
    def handle_zone3_amp_input_select(call):
        #_LOGGER.warn("Changing amp input...")
        amp_input = hass.states.get("input_select.zone3_amp_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 03 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("Amp input changed...")
        
        # Zone 4
        
    def handle_zone4_amp_off_select(call):
        #_LOGGER.warn("Powering AMP Off...")
        send_udp_command("c4.amp.out 04 00", ip_address, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zone4_amp_on_select(call):
        #_LOGGER.warn("Powering AMP On...")
        amp_input = hass.states.get("input_select.zone4_amp_input").state[:1]
        tuner_station = hass.states.get("input_select.zone2_radio_stations").state
        send_udp_command("c4.amp.chvol 04 a9", ip_address, 8750)
        send_udp_command("c4.amp.out 04 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("AMP Powered On...")
        
    def handle_zone4_amp_volume_select(call):
        #_LOGGER.warn("Changing amp volume...")
        volume_select = hass.states.get("input_number.zone4_amp_volume").state
        volume_select = int(float(volume_select) * 100) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 04 " + volume_select, ip_address, 8750)
        #_LOGGER.warn("Volume set...")
        
    def handle_zone3_amp_input_select(call):
        #_LOGGER.warn("Changing amp input...")
        amp_input = hass.states.get("input_select.zone4_amp_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 04 0" + amp_input, ip_address, 8750)
        #_LOGGER.warn("Amp input changed...")
        
    hass.services.register(DOMAIN, 'handle_zone1_amp_off_select', handle_zone1_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_on_select', handle_zone1_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_volume_select', handle_zone1_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_input_select', handle_zone1_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_off_select', handle_zone2_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_on_select', handle_zone2_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_volume_select', handle_zone2_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_input_select', handle_zone2_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_off_select', handle_zone3_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_on_select', handle_zone3_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_volume_select', handle_zone3_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_input_select', handle_zone3_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_off_select', handle_zone4_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_on_select', handle_zone4_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_volume_select', handle_zone4_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_input_select', handle_zone4_amp_input_select)

    # Return boolean to indicate that initialization was successfull.
    return True
