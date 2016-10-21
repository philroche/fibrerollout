# fibrerollout
Simple script to pull fibre rollout exchange data from openeir.ie

The script pulls the javascript source from [1] to find out the URL 
for the CSV containing all the updates for the exchanges. 
It parses that CSV for the provided exchanges and displays the output. 


[1] http://www.openeir.ie/NGAnetwork.aspx

## Binary Install 

Download the binary for your operating system

- [Linux](../../raw/master/dist/linux/fibrerollout)
- [Mac](../../raw/master/dist/mac/fibrerollout)
- [Windows](../../raw/master/dist/win/fibrerollout.exe)

## Binary example usage
```
fibrerollout --exchange COT
```
OR you can specify multiple exchange codes
```
fibrerollout --exchange COT --exchange KBE
```

![Example Usage](example-usage.png?raw=true "Example Usage")

## Source Install 
```
git clone https://github.com/philroche/fibrerollout.git
pip install -r requirements.txt
```

## Source example usage
```
python fibrerollout.py --exchange COT
```
OR you can specify multiple exchange codes
```
python fibrerollout.py --exchange COT --exchange KBE
```


