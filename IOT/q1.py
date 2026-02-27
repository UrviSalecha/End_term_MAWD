# Question-1
# SITUATION given to us is there is a continuous live video streaming from multiple cameras to a montioringserver
# Critical alert notifications must reach the control room without failure 
# Must support real time communication efficiently

#1.A) The protocol that I will use for live video streaming amongst TCP and UDP will be TCP
#The reason being it is connection oriented protocol it can implemented using sockets there is no loss of data unlike UDP.
# Although slower but still more secure no leakage of data

#1.B)  The protocol that I will use for critical alert notifications amongst TCP and UDP will be UDP.
# As it is a faster transmission of data compared to TCP AND AS THE ALERT IS CRITICAL we need faster notification protocol

#1.C) 1. Realibility: TCP
#2. Speed: UDP
#3. Connection establishment: UDP (connectionless)
#4. Packet Loss Handling: TCP 
