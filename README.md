# BID color classification example

## requirements

For this tutorial, in addition to the arduino environment you must install __anaconda distribution of python__. For more information see https://www.anaconda.com/

## circuit diagram

Follow [this tutorial](https://kyub.com/model/5feb4cd3e42c3e008936a02d) to build a simple CdS light sensing module.
Make sure you understand how breadboard matches the circuit schematic diagram.

## upload code

1. Open `main.ino` with Arduino IDE (or PlatformIO if you're fan of it) then upload the firmware to the microcontroller.
2. Open serial monitor and check if sensor values are coming. It varies depending on your lighting environment.
3. See `gather_data.py`. Change `port_name` to your arduino's port name. It should be something like `/dev/cu.usbserial...` for macOS/linux or `COMX` for windows.
4. Launch `python gather_data.py` and it will start to count for 10 seconds, spitting out the `out.csv` log file from the sensor readings.
5. Use `ipython notebook` to conduct data analysis. Here we use k-means clustering for non-supervised clustering. One of your task is to implement the algorithm in your arduino.
