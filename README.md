# Vevor-Thermal-Utilities
Small script to extract raw temperature data from Vevor and Infiray thermal camera images

## Embedded data format

In this section the format used by Vevor thermal cameras, firmware vxxx, is explained.
When an image is taken two files are generated. One .irg, that contains all thermal data, and one .jpg with the dispay as shown on the camera during capture. 

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
| 0 - 3 | 186 171 128   0 | uint32 | ? |
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

