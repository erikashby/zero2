### this is an example of json file for status
```
def get_status():
    status = {'nodeName':nodeName}
    # get all of the value out of the leds.
    leds_status = []
    for x in leds:
        leds_status.append(x.value)
    
    status.append('leds_status':leds_status)

```