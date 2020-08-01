#include <WiFi.h>
#include <WiFiMulti.h>
//WiFiMulti object used for handling the Wifi connection
WiFiMulti WiFiConnection;

//Important parameters for connecting to AP and getting instructions from server
char AP_SSID[32] = "";
char PASS[32] = "";
String NET_DUCKY_NAME = "";
const char * SERVER_HOST = "";
const uint16_t SERVER_PORT = ;

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
  
  Serial.println("\nCONNECTED!!!");
  Serial.println(WiFi.localIP());
}

void loop() {
  
 WiFiClient client;

 if(!client.connect(SERVER_HOST, SERVER_PORT)){
    Serial.println("Connection failure. Retry in 5s");
    delay(5000);
    return;
 }

 String url = "/download/" + NET_DUCKY_NAME + "/";
 client.print(url);

 while(!client.available()){
    delay(1);
 }
 if (client.available() > 0){
   Serial.println(client.readStringUntil('\r'));
 }
 else{
   Serial.println("TIMEOUT");
 }
 Serial.println("Waiting 10secs until restarting");
 delay(10000);
}
