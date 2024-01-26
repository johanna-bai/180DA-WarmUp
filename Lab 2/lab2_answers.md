# Task 1
## Screenshot Explanations
- 4_way_comm.png was created with my teammates Nancy Zhao, Anna Jin, and Abbas Hassani. 
- ping_pong.png was created using two programs that ping-pong each other a counter that increments each time they receive a message 
## Answers
MQTT could be used in sensors and microcontrollers to communicate with each other or with a computer during gameplay. Since many clients can be sending to the same topic, it takes some logic to distinguish whom each message was from. When multiple clients are in communication with each other, this added processing could add complexity and time in real-time gameplay. However, I still think that MQTT is better than TCP/IP or UDP in this game setting because of its simplicity compared to those other protocols. Using MQTT, we can expect lag time to be less than a second. 
# Task 2
## Testing
- In a quiet setting, the program can distinguish the fruit words in the word guessing game pretty well. It usually recognizes the word within 1 to 2 seconds. 
- The program was able to distinguish similar words sometimes, but not with a high success rate. The program also can't distinguish letters too well since they sound very similar to many other words. 
- The longest phrase that has worked is around 6 to 7 words. Nothing longer has been recognized even if I kept speaking. 
- When the background is loud, the program takes a lot longer to process input. Sometimes it can recognize the word but the accuracy is lower than when the room is quiet. I also had to speak very close to the microphone regardless of the loudness of the room. 

## Answers regarding the project
- We can give short verbal commands in our game using this program. 
- We can only expect speech recognition to recognize one or two words as a time with reasonable accuracy, so we don't want our speech recognition to be too complex in our project. We will probably just have single word commands for a higher accuracy rate. 
- We don't want to rely on the accuracy or latency of speech recognition too much in our game, because neither of them have very high performance. Ideally, we don't want a missed recognition to hurt the gameplay too much. 
- We could use clip-on microphones that are close to the players to mitigate background noise. 
