# raspberrypi

## pin (B+)
                3.3V  - 1| | 2-  5V  
     GPIO2(I2C1_SDA)  - 3| | 4-  5V  
     GPIO3(I2C1_SCL)  - 5| | 6-  GND  
       GPIO4(GPCLK0)  - 7| | 8-  GPIO14(UART_TXD)  
                 GND  - 9| |10-  GPIO15(UART_RXD)  
              GPIO17  -11| |12-  GPIO18  
              GPIO27  -13| |14-  GND  
              GPIO22  -15| |16-  GPIO23  
                3.3V  -17| |18-  GPIO24  
    GPIO10(SPI_MOSI)  -19| |20-  GND  
     GPIO9(SPI_MISO)  -21| |22-  GPIO25  
    GPIO11(SPI_SCLK)  -23| |24-  GPIO8(SPI_CE0)  
                 GND  -25| |26-  GPIO7(SPI_CE1)  
               ID_SD  -27| |28-  ID_SC  
               GPIO5  -29| |30-  GND  
               GPIO6  -31| |32-  GPIO12  
              GPIO13  -33| |34-  GND  
              GPIO19  -35| |36-  GPIO16  
              GPIO26  -37| |38-  GPIO20  
                 GND  -39| |40-  GPIO21  

## car
     MOTO_PIN_1 = 11 (GPIO17)  
     MOTO_PIN_2 = 13 (GPIO27)  
     MOTO_PIN_3 = 15 (GPIO22)  
     MOTO_PIN_4 = 16 (GPIO23)  
