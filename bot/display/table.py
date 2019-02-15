from netaddr import IPAddress, IPNetwork
from bot.config.network import subnets


def display_line(line):
    disp_line = '|'
    print(line)
    hostname, ips_virt = line['hostname'], line['ips']
    for item in subnets:
        verified = False
        for ip in ips_virt:
            if IPAddress(ip) in IPNetwork(item['subnet']):
                verified = True
                disp_line += ip
        if not verified:
            disp_line += '-'
        disp_line += '|'
    disp_line += '-'
    disp_line += '|'
    disp_line += hostname
    disp_line += '|'
    return disp_line


def create_tab(data):
    start = ('===== Suivi des adresses IP ===== \n\n'
	     '<WRAP center round important 80%>\n'
	     'Prendre la première IP libre dans le block concerné ! \\\\ \n'
	     'La première IP est l\'IP de la passerelle (.1) et la dernière '
	     'est celle de broadcast (.255), elles sont réservées !\n'
	     '</WRAP>\n\n'

	     'Les sous réseaux: \n')

    for item in subnets:
        subnet, vmbr, description = item['subnet'], item['vmbr'], item['description']
        start += '  * {}: {} ({})\n'.format(vmbr, subnet, description)
    start += '\\\\'

    tab = ''
    for item in subnets:
        tab += '^ IP ({})  '.format(item['vmbr'])  
    tab += '^ Créé par ^ Commentaires ^ .\n'

    print(start)
    print(tab)

    for line in data:
        disp_line = display_line(line)
        print(disp_line)
    return
