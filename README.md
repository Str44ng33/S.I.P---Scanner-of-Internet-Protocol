# S.I.P-Scanner-of-Internet-Protocol
Nmap com interface kkkkkkk
## Funcionalidades

1. **Escanear IPs dos Dispositivos Conectados**: Identifique os IPs dos dispositivos conectados em um roteador.
2. **Escanear Portas Abertas**: Verifique quais portas estão abertas em um dispositivo específico.

**Requisitos para:**

*Baseado em Arch linux*
```bash
sudo pacman -Syu
sudo pacman -S --noconfirm python python-nmap nmap
```
*Termux*

   ```bash
pkg update
pkg install -y python nmap
pip install python-nmap
   ```
*Baseado em Ubuntu*

```bash
sudo apt update
sudo apt install -y python3 python3-pip nmap
pip3 install python-nmap
```
**Depois de instalar os requisitos...**
dê os comandos:
```bash
git clone https://github.com/Str44ng33/S.I.P---Scanner-of-Internet-Protocol
cd S.I.P---Scanner-of-Internet-Protocol
python3 arquivo.py
```
