This is a simple CLI-based TCP port-scanner using an user-specified number of parallel threads for scanning.
The scanner is creating a socket which is used to attempt connections to different ports of the target IPv4 Address.
Every port is inserted into a queue from where is retrieved by one or multiple threads, through worker function, to be scanned.
