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

The embedded data is as shown in the next table. All is stored in little endian:

| Bytes | Description | Type | Notes |
| --- | --- | --- | --- |
| 0 | Temperature unit | uint8 | Enum: 0:ºC, 1:ºF |
| 1 - 2 | Maximum temp. | int16 | Scaled by 10 |
| 3 - 4 | Minimum temp. | int16 | Scaled by 10 |
| 5 - 6 | Unknown | int16 | Always 255/0 |
| 7 - 8 | Center temp. | int16 | Scaled by 10 |
| 9 | Emissivity | uint8 | Scaled by 100 |
| 10 - 13 | Unknown | uint16 | Always 6/0/0/0 |
| 14 - 15 | Max. temp. pos X | uint16 | |
| 16 - 17 | Max. temp. pos Y | uint16 | |
| 18 - 19 | Min. temp. pos X | uint16 | |
| 20 - 21 | Min. temp. pos Y | uint16 | |
| 22 - 23 | Center temp. pos X | uint16 | |
| 24 - 25 | Center temp. pos Y | uint16 | |
