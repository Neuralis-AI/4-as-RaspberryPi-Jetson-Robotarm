# 4-as-RaspberryPi-Jetson-Robotarm
Een handleiding hoe je een 4-assige programmeerbare robotarm maakt met 5 onderdelen + 3d parts.

Benodigdheden:   
4x SG90 Servo (https://neuralis.ai/?product=sg90-digitale-metalen-tandwiel-servo)   
1x Raspberry Pi Zero W(H) (https://neuralis.ai/?product=raspberry-pi-zero-w)   
OF 1x Raspberry Pi 4 (https://neuralis.ai/?product=raspberry-pi-4-model-b-2gb)   
OF 1x Nvidia Jetson Nano (https://neuralis.ai/?product=nvidia-jetson-nano-developer-kit-b01)   
1x 3D print files: https://www.thingiverse.com/thing:1015238   
Of bestel ze als pakket hier: (https://neuralis.ai/?product=4-assige-robotarm-3d-onderdelen)   
   
Maak het jezelf makkelijker door eerst een opstelling te maken op een Breadboard (https://neuralis.ai/?product=breadboard)   
   
**Voorbereiding:**   
Schrijf een nieuwe SDkaart met je favoriete OS.   
Deze handleiding is identiek voor zowel de Raspberry Pi 3/4/Zero/W als de Nvidia Jetson Nano/Xavier NX   
   
Bij gebruik van Raspbian OS of Nvidia Jetpack zijn alle benodigdheden standaard geinstalleerd.   
Zorg dat er een recente Python versie en een recente versie van nano geinstalleerd is.   
   
Installeer Git om deze repository te clonen, of kopieer de code uit test.py naar een nieuw uitvoerbaar document.   
Clone de repository:   
```
git clone https://github.com/Neuralis-AI/4-as-RaspberryPi-Jetson-Robotarm.git
```
Run het script met:   
```
python test.py
```
Bewerk het volledig becommentarieerde script met:   
```
nano test.py
```
