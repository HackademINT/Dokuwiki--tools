import paramiko
from time import sleep
from bot.config.network import password, key_filename, timeout

def connect(ip, username):
    if password is None and key_filename is None:
        return None, None
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    try:
        ssh.connect(ip, username=username, password=password,
                    key_filename=key_filename, timeout=timeout) 
    except Exception as exception:
        return None, None
    transport = ssh.get_transport()
    return ssh, transport


def read(channel):
    outdata, errdata = b'', b''
    while True: 
        """ Reading from output streams """
        sleep(0.5)
        while channel.recv_ready():
            outdata += channel.recv(1000)
        while channel.recv_stderr_ready():
            errdata += channel.recv_stderr(1000)
        if channel.exit_status_ready():
            return channel, outdata, errdata


def process(cmd, transport): 
    channel = transport.open_session()
    channel.setblocking(0)
    channel.exec_command(cmd)
    channel, outdata, errdata = read(channel)
    return channel, outdata, errdata


def res_process(cmd, transport):
    channel, outdata, errdata = process(cmd, transport)
    retcode = channel.recv_exit_status()
    #transport.close()
    return outdata, errdata
