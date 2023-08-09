# IP Enum

## Enumerates the individual IP addresses for any given subnet

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

`python ./ipenum.py 192.168.100.0/28 --json`
```
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
  ]
}
```

