# PORTSCANNER

Simple software made in Python that serves as a port scanner using the TCP/IP protocol, the Socket library was used to make connections and send packets through the mentioned protocols. Then use the Colorama library to help identify Open doors and Closed doors, finally, use
Use the Time and Datetime library for time manipulation.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/e74396f7-3a68-4db6-acc7-3c151196771e"></div>

## Operation
### Preparation - Definition of doors and target
   
A (simple) banner is created to test the functioning of the colorama library, then a "ports" array is created that will contain the ports that will be tested, once this is done a variable will store the target's IP or link, for example "localhost ".
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/8853aa49-4ea4-440a-9d41-41aca681f8ce"></div>

### Port Test
Using the For function, each port within the array is tested, where within the for function a TCP/IP socket is created that can be used to connect to other computers using the IPv4 protocol, waiting 0.5 seconds and attempting a connection (or sending packet) with the target on the specified port. If the "code" returns 0,
the door is open then it will print the message in green "Door Open", otherwise, red stating "Door closed", in both cases a return code is also informed.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/fdb27b1b-3503-48d2-897f-08d605d045e6"></div>

## Menu

A menu is created to test the execution of the portscanner, if everything goes correctly the code will start.
<div align=center><img src="https://github.com/cvinicius369/PortScanner/assets/137227050/6a5266d7-9f93-40ce-8f44-cab9da410caa"></div>

#OBS
This code is for educational purposes only, use sparingly.
