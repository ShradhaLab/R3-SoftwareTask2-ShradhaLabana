
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#initializing the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen()
arr = []
conn, addr = s.accept()
with conn:
    print ('Connection address:', addr)
    while True:
      data = conn.recv(BUFFER_SIZE)
      if not data: break
      #putting data into an array so speed and direction can be used at the same time
      arr.append(data)
      if(len(arr)>1):
          #checking if the user is inputting speed in order to display the strings (when user inputs direction the program doesn't output anything since it doesnt have speed at the moment)
          if(len(arr) %2 == 0):
              #getting the speed user inputted
              num = int(arr[len(arr)-1])
              #scaling the speed user inputted(since 1=51;2=102;3=153;4=204 and 5=255)
              Speed = num*51
              #outputting the results according to the input
              if(arr[len(arr)-2] == b'w'):
                 print('[f%d][f%d][f%d][f%d]' %(Speed, Speed, Speed, Speed))
              elif(arr[len(arr)-2] == b's'):
                 print('[r%d][r%d][r%d][r%d]' %(Speed, Speed, Speed, Speed))
              elif(arr[len(arr)-2] == b'a'):
                 print('[r%d][r%d][f%d][f%d]' %(Speed, Speed, Speed, Speed))
              elif(arr[len(arr)-2] == b'd'):
                print('[l%d][l%d][f%d][f%d]' %(Speed, Speed, Speed, Speed))
    conn.sendall(data)  # echo
conn.close()
