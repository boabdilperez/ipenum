# IP Enum

## Enumerates the individual IP addresses for any given subnet

The script takes in IPv4 addresses and returns the complete list of IP addresses on that network for each. Output can be either in a formatted plain-text or in a json object.

```json
{
  "network1": [
    "address1",
    "addressN"
  ],
  "networkN": [
    "address"
  ]
}
```

### Examples

`python ./ipenum.py --help`
```
usage: ipenum.py [-h] [--json] A [A ...]

Enumerate the entire network behind any IP address

positional arguments:
  A           One or more IP addresses in CIDR notation

options:
  -h, --help  show this help message and exit
  --json      Return answer in json format
```


`python ./ipenum.py 192.168.100.0/28`
```
Address: 192.168.100.0/28
Network: 192.168.100.0/28

===== IP Address List Start =====
192.168.100.0
192.168.100.1
192.168.100.2
192.168.100.3
192.168.100.4
192.168.100.5
192.168.100.6
192.168.100.7
192.168.100.8
192.168.100.9
192.168.100.10
192.168.100.11
192.168.100.12
192.168.100.13
192.168.100.14
192.168.100.15
===== End IP Address List =====
```

`python ./ipenum.py 192.168.100.0/28 192.168.200.0/28 --json`
```json
{
  "192.168.100.0/28": [
    "192.168.100.0",
    "192.168.100.1",
    "192.168.100.2",
    "192.168.100.3",
    "192.168.100.4",
    "192.168.100.5",
    "192.168.100.6",
    "192.168.100.7",
    "192.168.100.8",
    "192.168.100.9",
    "192.168.100.10",
    "192.168.100.11",
    "192.168.100.12",
    "192.168.100.13",
    "192.168.100.14",
    "192.168.100.15"
  ],
  "192.168.200.0/28": [
    "192.168.200.0",
    "192.168.200.1",
    "192.168.200.2",
    "192.168.200.3",
    "192.168.200.4",
    "192.168.200.5",
    "192.168.200.6",
    "192.168.200.7",
    "192.168.200.8",
    "192.168.200.9",
    "192.168.200.10",
    "192.168.200.11",
    "192.168.200.12",
    "192.168.200.13",
    "192.168.200.14",
    "192.168.200.15"
  ]
}
```

