import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
Organization = "49x4b9"
deviceType = "Weather_Device"
devceId = "Weather_Monitoring"
authMethod = "use-token-auth"
authToken = "143143143"

#Initalize GPIO

temp=random.randint(0,100)
pulse=random.randint(0,100)
Oxygen=random.randint(0,100)
lat =17
lon =18


def myCommandCallback(cmd):
    print("Command recevied: %s" % cmd.data['command'])
    print(cmd)



try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method":authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
        #...............................................

except Exception as e:
        print("Caught exception connecting device: %s" % str(e))
        sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type"greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
 
         data = { "d":{'temp' : temp, 'pulse': pulse ,'oxygen': oxygen,"lat":lat, 'lon': lon }}
         #print data
         def myOnPublishCallback():
             print("Published Temperature = %s C" % temp,"Humidity = %s %%"%Humidity,"to IBM Watson")

         success=deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallback)
         if not success
            print("Not connectedto IoTF")
         time.sleep(1)

         deviceCli.commandCallback = myCommandCallback

#Diconnectthe device and application from the cloud
deviceCli.disconnect()
                  



























         

         

                                                                         
    
