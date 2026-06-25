## Basic Network Sniffer

A Python-based Basic Network Sniffer developed as part of the **CodeAlpha Cyber Security Internship**. This project captures network packets using Python raw sockets and displays essential packet information in real time.

---

## Features

* Capture network packets.
* Display Source IP Address.
* Display Destination IP Address.
* Detect Protocol (ICMP, TCP, UDP).
* Display TTL (Time To Live).
* Display Packet Size.
* Display Packet Capture Time.
* Save captured packets into a log file (`packets.txt`).

---

## Technologies Used

* Python 3.12
* Socket Module
* Struct Module
* Datetime Module
* Windows OS

---

## Project Structure

```text
CodeAlpha_Basic_Network_Sniffer/
│
├── network_sniffer.py
├── packets.txt
├── README.md
├── requirements.txt
├── screenshots/
│   └── output.png
└── Report/
    └── Professional_Report.pdf
```

---

## Installation

1. Install Python 3.x.
2. Open Command Prompt as Administrator.
3. Clone the repository:

```bash
git clone https://github.com/YourUsername/CodeAlpha_Basic_Network_Sniffer.git
```

4. Navigate to the project folder:

```bash
cd CodeAlpha_Basic_Network_Sniffer
```

5. Run the application:

```bash
python network_sniffer.py
```

---

## Sample Output

```text
Packet #1
Time            : 02:41:34
Source IP       : 192.168.142.1
Destination IP  : 192.168.142.1
Protocol        : ICMP
TTL             : 128
Packet Size     : 124 Bytes
```

---

## Future Improvements

* Display TCP and UDP ports.
* Export captured packets to CSV.
* Add packet filtering.
* Develop a graphical user interface (GUI).
* Visualize packet statistics.

---

## Author

**Ahmed AbdelRahman Fathy**

Faculty of Computers and Artificial Intelligence

Sphinx University

Cyber Security Program

---

## License

This project was developed for educational purposes as part of the **CodeAlpha Cyber Security Internship**.
