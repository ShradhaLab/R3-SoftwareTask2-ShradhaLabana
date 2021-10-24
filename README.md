# R3-SoftwareTask2-ShradhaLabana
The following program gets input from the user, direction (a,w,s, or d) and speed (1-5) to get the expected output from the server program. The input method used is keyboard. The client.py file gets input from the keyboard that the user enters and sends it to the server.py file using TCP. In this case it sends the direction and then the speed, after which the server.py file scales the speed inputted, from 1-5 to 1-255. Then, the server.py file outputs both the direction and speed of the rover. For example, if w and the speed 5 is inputted, the program should output [f255][f255][f255][f255]. The output of the program can be seen below which is exactly like the expected output.

![image](https://user-images.githubusercontent.com/65087658/138599134-e640a6f4-c8cf-4e4e-be65-e01edecc4755.png)

![image](https://user-images.githubusercontent.com/65087658/138599152-3753af4e-2502-447d-9bd5-ea1548c0de3c.png)

I did use if statments to check whether only the speed or direction keys are inputted, however the program doesn't exit if another key is pressed. Since I check for direction first and then speed, if the input is entered incorrectly (speed first and then direction), the program will exit on its own since it won't be able to convert a letter (a,w,s,d) to integer. Also, the code used for getting input in the client.py file is used from the provided website, pypi.org. I used pynput to recieve input. To make a connection and get the data from client.py to server.py, the code from the website, wiki.python.org is used. 
