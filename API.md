# Project Hogwarts - Node API Documentation

## Endpoints

- GET /node/status  << Returns the status of all items on the node >>
- GET /node/light << perfrom an action (turn off or on) a light>>
    parameters:
        ID - ID of light to turn on (led0..led5)
        action - action to perform ('on', 'off')


## this is an example of json file for status

{
    'name' : 'noteName1',
    status = {
            'datetime' = 'datetime',
            'light_status' : [ {'id'= 'led0','state'=0 },{'id'= 'led1','state'=0 }...]
        }
}
