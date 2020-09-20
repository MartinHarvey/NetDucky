#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>
//WiFiMulti object used for handling the Wifi connection
WiFiMulti WiFiConnection;

//Important parameters for connecting to AP and getting instructions from server
char AP_SSID[32] = "";
char PASS[32] = "";
String NET_DUCKY_NAME = "";
String SERVER_HOST = "";

void setup() {
  Serial.begin(115200); //Serial baud rate
  Serial.println("START");
  delay(10);
  
  WiFiConnection.addAP(AP_SSID, PASS); //Connect using creds from global vars

  Serial.println("Trying to connect");
  
  while(WiFiConnection.run() != WL_CONNECTED){ //Retry until connection made
    Serial.print("=");
    delay(500);
  }
  
  Serial.print("CONNECTED TO AP!!! Local IP is: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  
 HTTPClient client;

 client.begin(SERVER_HOST + "download/" + NET_DUCKY_NAME );
 int respCode = client.GET();
 Serial.println("Resp code is " + String(respCode));
 
 
 if(respCode == 200){
  Serial.println("Success");
  String responseData = client.getString();
  Serial.println(responseData);
 }
 else{
  Serial.println("Error! Error Code is " + respCode);
 }
 
 
 Serial.println("Waiting 10secs until restarting");
 delay(10000);
}
