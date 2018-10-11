# ESEP
EC-Council Social Engineering

## Pre-Class Instructions
### Operating System
You may use Kali, Buscador, or a custom Linux (preferably Ubuntu) operating system. You may also use a Digital Ocean droplet (coupon: https://m.do.co/c/ab5f75969c8a) to do the labs using a cloud instance.

### Tools
Kali and Buscador have Recon-ng and TheHarvester installed. You will need to install Datasploit (https://github.com/jocephus/ESEP/blob/master/tools/OSINT/Tools.md) on either system. If you choose to use your custom operating system, instructions to install recon-ng and TheHarvester are included in the link for Datasploit.

### APIs
Using the keys obtained in the API subdirectory, include them in Recon-ng and Datasploit.

#### Recon-ng
To add the keys, open recon-ng and enter 
```keys add <API_Name> <API_Key>```

To add an API Key of a1b2c3 to API EC_Council, we would enter:
```keys add EC_Council a1b2c3```

#### Datasploit
For Datasploit, follow the installation instructions provided in the Github and enter the keys into ```config_sample.py``` then execute the following command:
```cp config_sample.py config.py```

This is everything for now, I look forward to seeing you and working through some Social Engineering and OSINT soon.<br>
 -Joe Gray (Twitter: @C_3PJoe, email: jgray[at]advancedpersistentsecurity[dot]net)
