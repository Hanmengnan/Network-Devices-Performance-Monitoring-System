from snmp_cmds import *
from Agent.util.paramer import *


class MachineInfo:
    machine_data = {'systemData': {}, 'cpuData': {}, 'diskData': {}, 'memoryData': {}, 'networkData': {}}

    def __init__(self, machine_ip):
        self.machine_ip = machine_ip

    def __get_data(self, oid_title):
        data_list = snmpwalk(ipaddress=self.machine_ip, oid=OID[oid_title], community='public')
        data_aim = [item[1] for item in data_list]
        return data_aim

    @staticmethod
    def get_operating_system(data_system):
        if 'Linux' in data_system:
            return 'Linux'
        elif 'Windows' in data_system:
            return 'Windows'
        else:
            return 'Router'

    def get_data_system(self):
        data_title = ['SysDesc', 'sysUptime', 'SysName', 'SysLocation', 'SysService']
        for title in data_title:
            data_raw = self.__get_data(title)
            if title == 'SysDesc':
                self.machine_data['systemData'][title] = MachineInfo.get_operating_system(data_raw[0])
                # example: ['Linux iZ2h3l4ah1nepvZ 4.4.0-193-generic] => Linux
            elif title == 'SysService':
                self.machine_data['systemData'][title] = SysServiceDict.get(data_raw[0])
                # example: ['72'] => ['应用层', '网络层']
            else:
                self.machine_data['systemData'][title] = data_raw[0]

    def get_data_cpu(self):
        data_title = ['ssCpuIdle', 'hrProcessorLoad']
        for title in data_title:
            data_raw = self.__get_data(title)
            self.machine_data['cpuData'][title] = data_raw[0]

    def get_data_disk(self):
        data_title = ['dskPath', 'dskTotal', 'dskAvail', 'dskPercent']
        for title in data_title:
            data_raw = self.__get_data(title)
            self.machine_data['diskData'][title] = data_raw[0]

    def get_data_memory(self):
        data_title = ['hrMemorySize', 'hrStorageIndex', 'hrStorageDescr',
                      'hrStorageUsed']
        for title in data_title:
            data_raw = self.__get_data(title)
            self.machine_data['memoryData'][title] = data_raw[0]

    def get_data_network(self):
        data_title = ['IfNumber', 'IfDescr', 'IfType', 'IfSpeed', 'IfPhysAddress', 'IfInOctet', 'IfOutOctet']
        for title in data_title:
            data_raw = self.__get_data(title)
            self.machine_data['networkData'][title] = data_raw[0]

        ip_in_discards = self.__get_data('ipInDiscards')[0]

        ip_in = self.__get_data('ifInUcastPkts')[0]
        self.machine_data['networkData']['loss'] = int(ip_in_discards) / int(ip_in)

    def get_data_ip(self):
        pass

    def get_data_tcp(self):
        data_title = ['tcpConnTable']
        for title in data_title:
            data_raw = self.__get_data(title)
            table_row = int(len(data_raw) / 5)
            self.machine_data['networkData'][title] = [data_raw[:table_row], data_raw[table_row:table_row * 2],
                                                       data_raw[table_row * 2:table_row * 3],
                                                       data_raw[table_row * 3:table_row * 4],
                                                       data_raw[table_row * 4:]]

    def get_data_udp(self):
        data_title = ['udpTable']
        for title in data_title:
            data_raw = self.__get_data(title)
            table_row = int(len(data_raw) / 2)
            self.machine_data['networkData'][title] = [data_raw[:table_row], data_raw[table_row:]]


if __name__ == "__main__":
    my_machine = MachineInfo('39.107.91.78')
    # my_machine = MachineInfo('127.0.0.1')
    my_machine.get_data_system()
    my_machine.get_data_cpu()
    my_machine.get_data_memory()
    my_machine.get_data_disk()
    my_machine.get_data_network()
    my_machine.get_data_tcp()
    my_machine.get_data_udp()
    print(my_machine.machine_data)
