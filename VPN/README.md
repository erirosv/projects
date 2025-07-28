# Setting up an VPN for a home lab


# Netmaker on Raspberry Pi — Full Setup Guide

This guide walks you through setting up a **self-hosted Netmaker VPN server** on a **Raspberry Pi**, from OS installation to launching the Web UI.

---

## ⚙️ Overview

1. Install Raspberry Pi OS (Lite or Full)
2. Update and install dependencies
3. Install Docker & Docker Compose
4. Install Netmaker via Docker
5. Access the Netmaker Web UI
6. Set up your first network and clients

---

## Step 1: Install Raspberry Pi OS

1. Download **Raspberry Pi OS Lite (64-bit)**:  
    https://www.raspberrypi.com/software/operating-systems/

2. Flash the image using **Raspberry Pi Imager** or **balenaEtcher**

3. Optional for headless setup:
   - Enable SSH: create a file named `ssh` in the boot partition
   - Set up Wi-Fi: create a `wpa_supplicant.conf` file with your SSID and password

4. Boot the Pi and log in:

   ```bash
   ssh pi@raspberrypi.local
   # Or use your Pi's local IP

## Step 2: Update System and Install Dependencies
```
sudo apt update && sudo apt upgrade -y
sudo apt install curl git net-tools ufw -y
```

## Step 3: Install Docker and Docker Compose
```
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker  # Or log out and back in
```

**Install Docker Compose plugin:**
```
sudo apt install docker-compose -y
```

**Verify installation:**
```
docker version
docker-compose version
```

## Step 4: Set Up Netmaker (Self-Hosted)
**A. Clone the Netmaker Repository**
```
git clone https://github.com/gravitl/netmaker.git
cd netmaker
```

**B. Configure the .env File**
1. Copy the example:
   ```
   cp .env.example .env
   ```
2. Edit .env:
   ```
   nano .env
   OR
   vim .env
   ```
   Update values:
   ```
   SERVER_HOST=yourdomain.duckdns.org  # Use your DuckDNS or public hostname
   API_PORT=443
   DNS_MODE=on
   ```

 Set up [DuckDNS](https://www.duckdns.org/)first if using dynamic IPs.

**C. Set Up Reverse Proxy with Traefik (HTTPS)**
Netmaker includes Traefik for HTTPS with automatic TLS via Let’s Encrypt.

Make sure:
- Port 443 is forwarded to your Pi
- Port 51821/UDP is forwarded for WireGuard

**D. Deploy Netmaker with Docker Compose**
```
docker compose -f docker-compose.yml -f docker-compose.traefik.yml up -d
```
> Wait for 1–2 minutes for the services to initialize.

## Step 5: Access the Netmaker Web UI
Go to:
```
https://yourdomain.duckdns.org
```

Login credentials:
- Username: admin
- Password: as defined in .env (MASTER_KEY)

## Step 6: Create Your First Network
- In the Netmaker UI, click Create Network
- Name it (e.g., homesites)
- Set CIDR (e.g., 10.10.0.0/24)
- Add your Raspberry Pi and other devices as nodes
- Netmaker will generate keys and config files automatically

## Security & Maintenance Tips
- Enable firewall and allow needed ports:
   ```
   sudo ufw enable
   sudo ufw allow ssh
   sudo ufw allow 443/tcp
   sudo ufw allow 51821/udp
   ```
- Back up your:
   - `.env`fidle
   - Docker volumes (Netmaker data lives in `/root/netmaker` by default)
- Use Netmaker’s agent to easily add remote clients:
   ```
   curl -s https://raw.githubusercontent.com/gravitl/netmaker/dev/scripts/netclient-install.sh | sudo bash
   ```

## Resources
- [Netmaker Docs](https://docs.netmaker.io)
- [DuckDNS](https://www.duckdns.org)
- Netmaker UI: `https://yourdomain.duckdns.org`