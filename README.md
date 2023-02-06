# Vevor-Thermal-Utilities
Small script to extract raw temperature data from Vevor SC240M (and likely Infiray C200 Pro) thermal camera images
![Extraction examples](https://github.com/jelle737/Vevor-Thermal-Utilities/raw/main/docs/img/output_example.png)

This shows how my interpretation is on how the data is saved in the irg file saved on the thermal camera. As I was curious what was in this file and if there was raw temperature information. I found there is raw temperature information.

The Infiray software can also open the files from the Vevor camera.

What I believe are the differences between the Infiray C200 Pro and Vevor SC240M:
- No USB live feed to computer software possible on SC240M

## Tested cameras:

- Vevor SC240M firmware V1.4.4 (102)

## Embedded data format

When an image is taken two files are generated. One .irg, that contains all thermal data, and one .jpg with the dispay as shown on the camera during capture.

![Camera Preview](https://github.com/jelle737/Vevor-Thermal-Utilities/raw/main/examples/samples/230201152910.jpg)

The data in the .irg file is distributed in the following blocks: 

| Byte length | Description | Notes |
| --- | --- | --- |
| 126 | Thermal header Embedded data | See next table |
| 240x180 | Historgram corrected preview | 1 bytes per pixel |
| 240x180x2 | Raw Thermal data | 2 bytes per pixel in x10°K |
| Remainder | jpg color image | encoded as standard jpg, resulution identical to thermal camera (240x180) |

The embedded data is as shown in the next table. All is stored in little endian:

| Bytes | Description | Type | Notes |
| --- | --- | --- | --- |
| 0 - 3 | 186 171 128   0 | uint32 | |
| 4 - 7 | 240x180 | int32 |  |
| 8 - 9 | 240 | int16 |  |
| 10 - 11 | 180 | int16 |  |
| 12 | 0 | int8 |  |
| 13 - 16 | 240x180 | int32 |  |
| 17 - 18 | 240 | int16 |  |
| 19 - 20 | 180 | int16 |  |
| 21 | 0 | int8 |  |
| 22 - 25 | 240x180 | int32 |  |
| 16 - 27 | 240 | int16 |  |
| 28 - 29 | 180 | int16 |  |
| 30 - 33 | Emissivity | uint32 | Scaled by 1000 |
| 34 - 37 | Reflective Temperature | uint32 | Scaled by 1000 |
| 38 - 41 | Ambient Temperature | uint32 | Scaled by 1000 |
| 42 - 45 | Distance | uint32 | Scaled by 1000 |
| 46 - 49 | 4000 | uint32 | |
| 50 - 51 | Transmissivity | uint32 | Scaled by 1000 |
| 52 - 55 | 0 | uint32 | |
| 56 - 59 | 10000 | uint32 | |
| .. | .. | .. | |
| 74 | Temperature unit | uint8 | Enum: 0:ºC, 1:ºF |
| .. | .. | .. | |

