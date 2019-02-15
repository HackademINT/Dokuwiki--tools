import ipaddress
from multiping import MultiPing
from bot.colors import red, yellow


def multi_ping(group):
    try:
        mp = MultiPing(group)
        yellow(mp)
        mp.send()
        responses, no_responses = mp.receive(1)
        return responses, no_responses
    except Exception as exception:
        red(exception)
        return None, None


def get_ips_from_group(group):
    """ Discard network, gateway and broadcast ip """
    result = []
    group = group[2:-1]
    responses, no_responses = multi_ping(group)
    if responses is None:
        return None
    for ip in responses:
        result.append(ipaddress.ip_address(ip))
    return map(str, sorted(result))


def get_ips_available(ips):
    size = 256
    ips_tot = []
    groups = [ ips[i:i+size] for i in range(0, len(ips), size) ] 
    for group in groups:
        result = get_ips_from_group(group)
        if result is not None:
            ips_tot += result
    return ips_tot
