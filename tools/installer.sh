echo "Installing dependencies"
sudo apt-get install git wget curl python-pip python3-pip -y
cd /opt

# Get all the packages
echo "Downloading the packages"
echo "Gathering wePWNise"
git clone https://github.com/mwrlabs/wePWNise;
echo "Gathering Unicorn"
git clone https://github.com/trustedsec/unicorn;
echo "Gathering WordSteal"
git clone https://github.com/0x09AL/WordSteal;
echo "Gathering Phishery"
wget https://github.com/ryhanson/phishery/releases/download/v1.0.2/phishery1.0.2linux-amd64.tar.gz;
echo "Gathering GoPhish"
wget https://github.com/gophish/gophish/releases/download/v0.5.0/gophish-v0.5.0-linux-64bit.zip;
echo "Gathering PWDology"
git clone https://github.com/tch1001/pwdlogy;
echo "Gathering Empire"
git clone https://github.com/EmpireProject/Empire;
echo "Gathering Streisand"
git clone https://github.com/StreisandEffect/streisand;
echo "Gathering King Phisher"
git clone https://github.com/securestate/king-phisher;
echo "Gathering SPF"
git clone https://github.com/tatanus/SPF;
echo "Gathering Generate Macro"
git clone https://github.com/enigma0x3/Generate-Macro;
echo "Gathering TAP"
git clone https://github.com/trustedsec/tap;
echo "Gathering Powershell"
wget https://github.com/PowerShell/PowerShell/releases/download/v6.1.0-preview.1/powershell_6.1.0-preview.1-1.debian.8_amd64.deb;
echo "Gathering Spiderfoot"
git clone https://github.com/smicallef/spiderfoot;
echo "Gathering Datasploit"
git clone https://github.com/DataSploit/datasploit;
echo "Gathering AltDNS"
git clone https://github.com/upgoingstar/altdns;
echo "Gathering TweetMonitor"
git clone https://github.com/upgoingstar/TweetMonitor;
echo "Gathering HackerOne Public Reports"
git clone https://github.com/upgoingstar/hackerone_public_reports;
echo "Gathering WhatsMyName"
git clone https://github.com/WebBreacher/WhatsMyName;
echo "Gathering "Spaces Finder"
git clone https://github.com/upgoingstar/spaces-finder;
echo "Gathering AuthCheck"
git clone https://github.com/upgoingstar/Auth-Check;
echo "Gathering SimplyEmail"
git clone https://github.com/SimplySecurity/SimplyEmail;
echo "Gathering Veil"
git clone https://github.com/Veil-Framework/Veil;

# Begin Dependencies and Installation
echo "Installing Powershell"
dpkg -i powershell_6.1.0-preview.1-1.debian.8_amd64.deb;
echo "Installing GoPhish"
unzip /opt/gophish-v0.5.0-linux-64bit.zip -d /opt/gophish;
echo "Installing Phishery"
tar -xvf phishery1.0.2linux-amd64.tar.gz --directory /opt/phishery;
cd /opt/phishery;
cp phishery /usr/local/bin;
cd /opt;
echo "Installing Empire"
cd /opt/Empire/setup/;
pip install -r requirements.txt;
cd ..;
./setup/install.sh;
echo "Installing King Phisher"
cd /opt/king-phisher;
pip install -r requirements.txt;
./tools/install.sh;
cd ..;
echo "Installing SPF"
cd /opt/SPF;
pip install -r Requirements.txt;
./install.sh;
cd ..;
echo "Installing Spiderfoot"
cd /opt/spiderfoot;
pip install -r requirements.txt;
python setup.py;
cd..;
echo "Installing Datasploit"
cd /opt/datasploit;
pip install -r requirements.txt;
cd ..;
echo "Installing AltDNS"
cd /opt/altdns;
pip install -r requirements.txt;
cd ..;
echo "Installing WhatsMyName"
cd /opt/WhatsMyName;
pip install -r requirements.txt;
cd ..;
echo "Installing "Spaces Finder"
cd /opt/spaces-finder;
pip install -r requirements.txt;
cd ..;
echo "Installing SimplyEmail"
cd /opt/SimplyEmail/setup;
pip install -r requirements.txt;
cd ..;
/opt/SimplyEmail/setup/setup.sh;
echo "Installing Veil"
cd /opt/Veil/setup;
sudo ./setup.sh -c;
cd /opt;
