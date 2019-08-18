# How To Set or Change Timezone on Ubuntu


### Checking the Current Timezone
```
$ timedatectl
```

output 

```
                      Local time: Wed 2019-01-23 22:45:47 UTC
                  Universal time: Wed 2019-01-23 22:45:47 UTC
                        RTC time: Wed 2019-01-23 22:45:48
                       Time zone: Etc/UTC (UTC, +0000)
       System clock synchronized: yes
systemd-timesyncd.service active: yes
                 RTC in local TZ: no
```
   
   
   
   

### Changing the Timezone Using the timedatectl Command
```
$ timedatectl list-timezones
```

output
```
...
Europe/Oslo
Europe/Paris
Europe/Podgorica
Europe/Prague
Europe/Riga
Europe/Rome
Europe/Samara
...
```

Identify which time zone is accurate to your location, run the following command as sudo user:
```
$ sudo timedatectl set-timezone your_time_zone
```

e.g.
```
$ sudo timedatectl set-timezone Asia/Kolkata
```


