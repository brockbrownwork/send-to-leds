'''
What happens if I try to connect to a network I'm already connected to?
What happens if I try to connect to a network that doesn't exist?
What if wifi is turned off?
'''
import subprocess

def connect(led_sign_id):
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
