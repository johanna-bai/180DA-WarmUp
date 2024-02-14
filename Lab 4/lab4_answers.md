## Task 3
From my screenshot, the lag seems to be around 6 to 7 measurement. However, given the high frequency that the IMU takes measurements at, the lag is around one second or less. We could send data less frequently or do some processing on the IMU before transmitting, but that depends on testing data later. In our tag game, we could also put a constraint on how quickly our player moves to minimize the effects of lag. 

## Task 4
1. The gravity acceleration is usually in the range of 990-1020 mg when idle. 
2. Yes, the values do drift even when idle. When idle, the value ranges for my IMU usually are: 
    - x acceleration: -50 to 50 mg
    - y acceleration: -50 to 50 mg
    - z acceleration: 990 to 1030 mg
    - x, y, z rotation: -3 to 3 DPS
    The idle classification with these values is nearly 100% accurate. 
3. I used acceleration in the x direction for forward push and acceleration in the z direction for upward lift. I used simple if statements and not a decision tree for this classification. 
