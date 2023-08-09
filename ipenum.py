"""Enumerates the individual IP addresses for any given subnet
Author: Boabdil Perez
Date: 9 August 2023
Version: 0.1.0

Args:
  addresses: Any number of IP addresses in CIDR notation

Returns:
  A list of IP addresses that comprises the entirety of the network for each address passed in.

Raises:
  ValueError: If the provided string is not a valid IPv4 address
"""
import argparse
import json
from ipaddress import IPv4Interface
from sys import stderr


def main(args):
    """Script logic entrypoint"""
    valid_addrs: list[IPv4Interface] = []
    json_ret: dict[str, str] = {}
    json_flag: bool = args.json_flag
    for address in args.addresses:
        try:
            valid_addrs.append(IPv4Interface(address))
            json_ret.update({str(IPv4Interface(address).network): list()})
        except ValueError as err:
            print(f"{address} is not a valid IPv4 address: {err=}", file=stderr)
    for address in valid_addrs:
        if not json_flag:
            print(f"Address: {address}\r\nNetwork: {address.network}")
            print("\r\n===== IP Address List Start =====")
        for unique_ip in address.network:
            if not json_flag:
                print(str(unique_ip))
            json_ret[str(address.network)].append(str(unique_ip))
        if not json_flag:
            print("===== End IP Address List =====\r\n")
    if json_flag:
        json_output = json.dumps(json_ret, indent=2)
        print(json_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enumerate the entire network behind any IP address"
    )
    parser.add_argument(
        "addresses",
        metavar="A",
        type=str,
        nargs="+",
        help="One or more IP addresses in CIDR notation",
    )
    parser.add_argument(
        "--json",
        dest="json_flag",
        action="store_true",
        default=False,
        help="Return answer in json format",
    )
    arguments = parser.parse_args()
    main(arguments)
