from netaddr import IPAddress, IPNetwork
import re
from bot.config.network import subnets


def is_in_subnet(ip, subnet):
    for subnet_data in subnets:
        if IPAddress(ip) in IPNetwork(subnet_data['subnet']):
            return True
    return False


def extract_ips(outdata, already, subnet):
    ips = []
    pattern = b'inet (.*?)/.*? scope global'
    match_ips = re.findall(pattern, outdata)

    if match_ips is None:
        return ips, already

    for ip in [ ip.decode() for ip in match_ips ]:
        if is_in_subnet(ip, subnet):
            already.append(ip)
            ips.append(ip)

    return ips, already
