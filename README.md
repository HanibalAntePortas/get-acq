# get-acq 🏢 

GET-ACQ is python tool used to gather all companies aquised by given company domain name. It is done by calling SecurityTrails API.

## Usage 🛠 

python3 get-acq.py --domains domains.txt -a <API_KEY> -o output.txt

## Running from Docker 🐳 

docker run -ti -v $(PWD)/data:/data get-acq -u /data/domains.txt -a <API_KEY> -o /data/output.txt
## Parameters 🧰 

Parameter | Description | Type
------------ | ------------- | -------------
-d, --domains | Specify the list with domains. | File
-a, --apikey | APIKEY | String
-o, --output | Specify output filename | String


#### License

This project is licensed under **MIT** license
