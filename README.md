# Survellience system using MQTT
This is demo code written in Python that can monitor any remote place using the MQTT server.

MQTT stands for MQ Telemetry Transport. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for constrained devices and low-bandwidth, high-latency or unreliable networks. The design principles are to minimise network bandwidth and device resource requirements whilst also attempting to ensure reliability and some degree of assurance of delivery. These principles also turn out to make the protocol ideal of the emerging “machine-to-machine” (M2M) or “Internet of Things” world of connected devices, and for mobile applications where bandwidth and battery power are at a premium.

Hardware dependencies :

- Raspberry pi as the Target 
- Camera connected to the raspberry pi


Software Dependencies:
- Python
- Raspbian OS
- paho-mqtt

#### How to run the code : ####

1. Install the dependencies on Target machine (Raspberry pi)

```bash
  sudo apt-get update
  sudo apt-get install fswebcam
  sudo apt-get install python-dev python-pip
  pip install paho-mqtt
```
2. Install the dependencies on Host machine (Laptop)

```bash
  sudo apt-get update
  sudo apt-get install python-dev python-pip
  pip install paho-mqtt
```

3. System Arrangement

Connect the camera to the Target machine. To understand the flow better refer the diagram below 

![alt text](https://github.com/huzz/Remote-surveillance-system-using-mqtt/blob/master/mqtt_flow.png)

4. Run the code :

On Target Machine
 ```bash
 python client_publish.py
 ```
On Host Machine
 ```bash
 python client.py &
 python publish.py 
 enter capture
 ```

