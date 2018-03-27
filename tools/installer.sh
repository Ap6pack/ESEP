echo "Installing dependencies"
sudo apt-get install git wget curl -y

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

# Begin Dependencies and Installation
echo "Installing Powershell"
dpkg -i powershell_6.1.0-preview.1-1.debian.8_amd64.deb;
