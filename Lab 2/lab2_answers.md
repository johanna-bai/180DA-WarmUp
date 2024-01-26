# Task 1
## Screenshot Explanations
- 4_way_comm.png was created with my teammates Nancy Zhao, Anna Jin, and Abbas Hassani. 
- ping_pong.png was created using two programs that ping-pong each other a counter that increments each time they receive a message 
## Answers
MQTT could be used in sensors and microcontrollers to communicate with each other or with a computer during gameplay. Since many clients can be sending to the same topic, it takes some logic to distinguish whom each message was from. When multiple clients are in communication with each other, this added processing could add complexity and time in real-time gameplay. However, I still think that MQTT is better than TCP/IP or UDP in this game setting because of its simplicity compared to those other protocols. Using MQTT, we can expect lag time to be less than a second. 