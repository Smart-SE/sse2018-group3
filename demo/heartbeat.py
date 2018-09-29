
import numpy as np
import matplotlib.pyplot as plt
import smbus2
import time

HEART_STATE_UP1 = 0
HEART_STATE_UP2 = 1
HEART_STATE_DOWN1 = 2
HEART_STATE_DOWN2 = 3

def get_heartbeat():
    bus = smbus2.SMBus(1)

    heartbeat = []
    heartstatus = HEART_STATE_DOWN1
    heartcount = 0
    retcnt = 0
    

    for i in range(200):
        data = bus.read_i2c_block_data(0x2a, 0x00, 2)
        #print(data)
        beat = data[1]
        heartbeat += [beat]
        time.sleep(0.01)

        heartcount +=1
        if heartstatus == HEART_STATE_UP1:
            if beat > 120 :
                #print("u2")
                heartstatus = HEART_STATE_UP2
        elif heartstatus == HEART_STATE_UP2:
            if beat < 100 :
                #print("d1")
                heartstatus = HEART_STATE_DOWN1
        elif heartstatus == HEART_STATE_DOWN1:
            if beat < 80 :
                #print("d2")
                heartstatus = HEART_STATE_DOWN2
        elif heartstatus == HEART_STATE_DOWN2:
            if beat > 100 :
                #print("u1")
                heartstatus = HEART_STATE_UP1
                retcnt = heartcount
                #print(heartcount)
                heartcount = 0

    #print(heartbeat)

    fig = plt.figure(figsize=(2.4,2.2))
    #fig.subplots_adjust(left=0.30)
    ax = fig.add_subplot(1,1,1)
    ax.set_title("heartbeat")
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.plot(heartbeat)
    plt.savefig("heartbeat.png")
    return retcnt

#b = get_heartbeat()
#print(b)


