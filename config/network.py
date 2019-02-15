#!/usr/bin/python3

subnets = [{'subnet': '10.10.10.0/24', 'vmbr': 'vmbr0', 
            'username': 'root', 'description': 'administration principale'},
           {'subnet': '10.20.17.0/24', 'vmbr': 'vmbr17', 
            'username': 'root', 'description': 'ctf kerberint 2017'},
           {'subnet': '10.20.18.0/24', 'vmbr': 'vmbr18', 
            'username': 'root', 'description': 'ctf starhack 2018'},
           {'subnet': '10.20.19.0/24', 'vmbr': 'vmbr19', 
            'username': 'root', 'description': 'ctf 2019'},
           {'subnet': '10.33.0.16/24', 'vmbr': 'vmbr1337', 
            'username': 'deploy', 'description': 'cluster docker'}]
password = None 
key_filename = './config/id_rsa'
timeout = 2
