# Temporal global variables for terminal
This is a simple script that allows you to use global
variables shared between independent terminal session.

## Installation
```shell
sudo ln -s /HDD/Code/Python/global/global.py /usr/bin/global
```

## How to use
```shell
# Set a variable
global myVar Hwr20!!.2

# Get a variale
global myVar
```

# A more elaborate example
Insted of do something like
```bash
ssh Admin@this_is_a_very_long_url_for_a_remote_server.something.com
```
You can do something like
```
gb aws this_is_a_very_long_url_for_a_remote_server.something.com

ssh Admin@`gb aws` 
```
And then in another termianl (maybe you already have it open) you can continue using it.
```bash
# In another terminal
ping -c 3 `gb aws`
scp ./somefile.sql Admin@`gb aws`
```

## Alias
Optionally you can reate an alias.
```shell
echo alias gb='global' >> ~/.bashrc

gb myVar
```
