'''
What happens if I try to connect to a network I'm already connected to?
What happens if I try to connect to a network that doesn't exist?
What if wifi is turned off?
'''

import subprocess
from os import system
from time import sleep, time

def connect(led_sign_id, timeout = 10):
    stop_trying_time = timeout + time()
    disconnect()
    number_to_network = {}
    with open("network_names_for_signs.txt") as f:
        network_names = f.read().split('\n')
    for line in network_names:
        led_id, network_name = line.split(":")
        number_to_network[int(led_id)] = network_name
    network_name = number_to_network[led_sign_id]
    print("attempting connection to {0}".format(network_name))
    command = 'cmd /c "netsh wlan connect name={0}"'.format(network_name)
    message = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    message = message.stdout.read().decode('UTF-8')
    with open("output_of_connection_attempt.txt", "w") as f:
        f.write(message)
    print(message)
    print(number_to_network)
    while not connected() and time() <= stop_trying_time:
        sleep(0.5)
        print("waiting for connection...")
    if time() >= stop_trying_time:
        print("couldn't connect to led #{0}, gave up after {1} seconds".format(led_sign_id, timeout))
        return False
    else:
        print("connected to led #{0}!".format(led_sign_id))
        return True

def connected():
    command = 'cmd /c "ipconfig"'
    message = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    message = message.stdout.read().decode('UTF-8')
    message = message.lower()
    index = message.find('wi-fi')
    message = message[index:]
    return 'disconnected' not in message

def disconnect():
    system("netsh wlan disconnect")

