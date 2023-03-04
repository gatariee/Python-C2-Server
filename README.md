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
- Run victim.py on victim machine



## API
API calls are handled by the beacon
- ```POST /status```

| Description                        |
| :-------------------------         |
| Updates beacon on status of clients |

- ```GET /clients```

| Description                        |
| :-------------------------         |
| Returns the status of clients |

- ```POST /command```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `command`      | `string` | Sends command to be executed by the victim  |

- ```GET /get_command```

| Description                        |
| :-------------------------         |
| Retrieves the latest command to be executed by the victim |

- ```POST /post_result```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `result`  | `string` | Result of the command executed by the victim  |

- ```GET /get_result```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `result`  | `string` | Returns the result of the latest command executed by victim  |


## Note
- API Endpoints are incomplete, you can add/remove/edit the existing endpoints to suit your needs
- More commands can be implemented if required, these scripts serve as an outline


