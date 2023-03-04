# Python C2 Server using HTTP & API Endpoints 
Python-based Command & Control (C2) server using HTTP & API Endpoints with a beacon to route traffic between victim and operator. 

This is a simple C2 server that shouldn't be used for actual engagements, made just for fun.





## Features

- C2 comms exchanged over HTTP traffic (kind of stealthy)
- Uses API Endpoints to control victim
- Beacon to route traffic between victim and operator


## Usage
- Run beacon.py on random server (e.g. AWS EC2)
- Run main.py on operator machine
- Run Run victim.py on victim machine
