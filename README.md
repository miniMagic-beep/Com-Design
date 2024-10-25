# BPSK Communication System with GNU Radio and BladeRF

# How to Run

1. **Prepare the File**
   - Rename the file to be transmitted as `images.jpeg` (or update the filename in the code).
   - Run `python3 tx.py`, which will create a file named `output.tmp`.

2. **Set Up BladeRF and GNU Radio**
   - Connect a single BladeRF with both antennas attached (Tx and Rx).
   - Run `finalfinal.grc` in GNU Radio, ensuring the path to `output.tmp` is correctly set in the file block.
   - The flowgraph implements both the transmitter and receiver, creating a file named `output.tmp`.

3. **Receive and Process the File**
   - Copy `output.tmp` to the directory containing `rx.py`.
   - Run `python3 rx.py` to generate the final output as `Decrypt_image`.
  
   ---

For any issues, reach me at [wickramarathnemp.21@uom.lk](mailto:wickramarathnemp.21@uom.lk).

## Overview
This project demonstrates a **Binary Phase Shift Keying (BPSK)** communication system using **GNU Radio** and the **BladeRF SDR**. The system is capable of transmitting images between devices wirelessly with advanced features like Forward Error Correction (FEC), Checksum verification, and AES encryption to ensure secure and reliable data transmission.

## Features
- **Modulation**: BPSK modulation for efficient wireless communication.
- **Forward Error Correction (FEC)**: Built-in error-correcting codes for reliable data transfer.
- **Checksum**: Ensures data integrity by verifying that the transmitted data is received correctly.
- **AES Encryption**: Secure data encryption with AES before transmission to protect sensitive information.
- **Image Transmission**: Send images from one device to another wirelessly.
- **GNU Radio**: Utilizes the power of GNU Radio for digital signal processing and flow graph design.
- **BladeRF**: Supports BladeRF SDR for hardware-based transmission and reception.

## Team Members
- **Mihiran Wickramarathne**
- **Dasuni Herath**
- **Shaveen Herath**
- **Danidu Dabare**
