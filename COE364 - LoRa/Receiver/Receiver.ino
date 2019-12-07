#include <SPI.h>
#include <LoRa.h>

//Definindo os pinos a serem usados no transceiver
#define ss 5
#define rst 14
#define dio0 2

int LED = 4;


void setup() {
  pinMode(LED, OUTPUT);
  //Frequencia do Monitor Serial
  Serial.begin(115200);
  while (!Serial);
  Serial.println("LoRa Receiver");

  //Configurando os pinos do transceiver LoRa
  LoRa.setPins(ss, rst, dio0);
  
  //Frequencias do LoRa 
  //433E6 for Asia
  //866E6 for Europe
  //915E6 for North America
  while (!LoRa.begin(915E6)) {
    Serial.println(".");
    delay(500);
  }
   // A palavra de sincronizacao (0xF3) serve para garantir a sincronia entre as partes
  // A palavra de sincronizacao garante que voce nao recebera mensagens de outros transmissores
  // ranges from 0-0xFF
  LoRa.setSyncWord(0xF3);
  Serial.println("Lora Inicializado!");
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // pacote recebido
    Serial.print("Pacote recebido '");
    digitalWrite(4, HIGH);
    delay(200);
    digitalWrite(4, LOW);

    

    // Ler pacote
    while (LoRa.available()) {
      String LoRaData = LoRa.readString();
      Serial.print(LoRaData); 
    }

    // Mostra o RSSI do pacote
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}
