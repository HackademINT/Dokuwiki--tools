#!/usr/bin/python3

import ipaddress
from bot.colors import blue, cyan, green, purple, red
from bot.config.network import subnets, password, key_filename, timeout
from bot.display.table import create_tab
from bot.network.ping import get_ips_available
from bot.network.ssh import connect, res_process
from bot.parser.ip import extract_ips


def get_data_subnet_ip(ip, username, already, subnet):
    if ip in already:
        return None, already

    ssh, transport = connect(ip, username)
    if ssh is None: 
        red('Cannot connect to {}'.format(ip))
        purple('-----------------------------------------------------')
        return None, already

    green('Connect to {} using SSH'.format(ip))
    outdata, errdata = res_process('ip a', transport)
    ips_virt, already = extract_ips(outdata, already, subnet)
    blue('List of IP(s) found: ' +  ' | '.join(ips_virt))

    outdata, errdata = res_process('cat /etc/hostname', transport)
    hostname = outdata[:-1].decode()
    cyan('Hostname found: {}'.format(hostname))
    purple('-----------------------------------------------------')

    result = {'ips': ips_virt, 'hostname': hostname}
    return result, already


def get_data_subnet(subnet_data, already):
    subnet, username = subnet_data['subnet'], subnet_data['username']
    network = ipaddress.ip_network(subnet, strict=False)
    ips = [ str(ip) for ip in network ]
    ips_available = get_ips_available(ips)
    data_from_subnet = []

    for ip in ips_available:
        data_subnet_ip, already = get_data_subnet_ip(ip, username, already, subnet)
        if data_subnet_ip is not None:
            data_from_subnet.append(data_subnet_ip)

    return data_from_subnet, already


def get_data():
    already, data = [], []
    for subnet_data in subnets:
        data_from_subnet, already = get_data_subnet(subnet_data, already)
        data += data_from_subnet
    return data


if __name__ == '__main__':
    data = get_data()
    create_tab(data)
