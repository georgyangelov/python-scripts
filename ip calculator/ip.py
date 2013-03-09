import argparse
from ipaddress import *

parser = argparse.ArgumentParser(description=
                                 "IPv4 and IPv6 address calculator")
parser.add_argument("ip_address",
                    help=("IP address of a network or a host. Can be "
                          "IPv4 or IPv6 address"))
parser.add_argument("ip_mask",
                    help="Network mask, either dotted decimal or CIDR")
parser.add_argument("-a", "--allhosts",
                    help="Print all available hosts in the network (if < 257)",
                    action="store_true")
parser.add_argument("-c", "--checkip",
                    help="Check if the IP address belongs to the network")
arguments = parser.parse_args()


interface = ip_interface("{}/{}"
                         .format(arguments.ip_address, arguments.ip_mask))

network = interface.network

if arguments.checkip:
    ip_check = ip_address(arguments.checkip)

    print("The host {} {} within the network".
          format(ip_check, "is" if ip_check in network else "is NOT"))

else:
    print("Stats for {}"
          .format(interface))
    print("Network mask is {}"
          .format(network.netmask))
    print("Network address is {}"
          .format(network.network_address))
    print("Broadcast address is {}"
          .format(network.broadcast_address))
    print("Number of addresses: {}"
          .format(network.num_addresses))

    if arguments.allhosts:
        if network.num_addresses <= 256:
            print("All addresses in the network:",
                  ", ".join(str(address) for address in network))
        else:
            print("All hosts are more than 256 and will not be printed")
