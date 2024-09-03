import time
now=time.ctime()
corpus={
    'hy':"hello",'how are you':'i m fine',"whats your name ":" my name is chatbot"
    ,"what are you doing ":" nothing yar "
    ,"whats ": now}
while True:
    q=input()
    if q=='quict':
        break
    else:
        # q is key 
        print(corpus[q])
