# 🌡️ RPiFan - Raspberry Pi Temperature Control System

<div align="center">
<img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge" />
</div>

## 📋 Overview
RPiFan is an intelligent temperature control system for Raspberry Pi that automatically manages fan speed based on CPU temperature. The system provides efficient cooling while minimizing noise and power consumption.

## 🔥 Features
- **Automatic Temperature Monitoring**: Continuously monitors CPU temperature
- **Smart Fan Control**: Three-stage PWM fan speed control
  - Full speed (100%) above 50°C
  - Half speed (50%) between 45°C and 50°C
  - Fan off below 42°C
- **Resource Efficient**: Minimal CPU usage with 2-second polling interval
- **Safe Operation**: Includes fail-safes and proper GPIO cleanup

## 🛠️ Setup Instructions

### Hardware Setup
This project utilizes the following components:

- **Fan**: [Official Raspberry Pi 4 Case Fan](https://www.raspberrypi.com/products/raspberry-pi-4-case-fan/) (extracted from its original housing)
- **Case**: [Official Raspberry Pi Zero Case](https://robu.in/product/official-raspberry-pi-zero-case/)
- **Modification Details**:
  - Custom ventilation hole cut in the official case lid
  - Fan mounted directly above the CPU using hot glue
  - Clean, professional finish maintaining the original case aesthetics

> 📸 *Reference images showing the modification process and final setup can be found in the gallery below*

### Gallery
<table>
  <tr>
    <td width="33%">
      <img src="resources/x1.jpg" alt="Inside" width="100%"/>
      <p align="center"><em>Inside</em></p>
    </td>
    <td width="33%">
      <img src="resources/x2.jpg" alt="Front View" width="100%"/>
      <p align="center"><em>Front View</em></p>
    </td>
    <td width="33%">
      <img src="resources/x3.jpg" alt="Top View" width="100%"/>
      <p align="center"><em>Top View</em></p>
    </td>
  </tr>
</table>

### Hardware Requirements
- Raspberry Pi (any model)
- PWM-compatible cooling fan
- Connections:
  - PWM control wire to GPIO pin 12 (BCM mode)
  - Power wire to 5V pin
  - Ground wire to GND pin

### Software Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RPiFan.git
   cd RPiFan
   ```

2. Make the service script executable:
   ```bash
   chmod +x fanService.sh
   ```

3. Set up automatic startup using crontab:
   ```bash
   sudo crontab -e
   ```
   Add the following line:
   ```bash
   @reboot /home/admin/projects/RPiFan/fanService.sh
   ```

> 💡 For detailed help with startup configuration, check out [this Instructables guide](https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/)

## 🔧 Configuration
You can modify the following constants in `fan_control.py`:
- `TEMP_HIGH`: Temperature threshold for full speed (default: 50°C)
- `TEMP_MEDIUM`: Temperature threshold for half speed (default: 45°C)
- `TEMP_OFF`: Temperature threshold to turn off fan (default: 42°C)
- `PWM_FREQ`: PWM frequency in Hz (default: 25Hz)

## 📝 License

This project is licensed under the GNU General Public License v3.0 (GPLv3).

### Key points of the GPLv3 License:
- ✔️ Freedom to use the software for any purpose
- ✔️ Freedom to change the software to suit your needs
- ✔️ Freedom to share the software with your friends and neighbors
- ✔️ Freedom to share the changes you make

For more details, see the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

---
<div align="center">
Made with ❤️ for Raspberry Pi Community
</div>