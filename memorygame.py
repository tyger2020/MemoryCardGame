import simplegui  
import random  
 
num=[]  
 
state=0  
first =0  
last =0  
turn=0  
 
# helper function to initialize globals  
def new_game():  
    global num,exposed,turn  
    num=range(0,8)  
    num.extend(range(0,8))  
    random.shuffle(num)  
    exposed=[False,False,False,False,False,False,False,False,  
         False,False,False,False,False,False,False,False]  
    turn=0  
 
    #print num  
 
       
# define event handlers  
def mouseclick(pos):  
    # add game state logic here  
    global exposed,state,first,last,turn  
    index=pos[0]//50  
    if not exposed[index]:  
        exposed[index]=True   
        if state==0:  
            state=1  
            first=index  
        elif state==1:  
            last=index  
            state=2  
        elif state==2:  
            if num[first]!=num[last]:  
                exposed[first]=False  
                exposed[last]=False  
            first=index  
            state=1  
        turn+=1  
          
                          
# cards are logically 50x100 pixels in size      
def draw(canvas):  
    global num  
    card=0  
    index=0  
    label.set_text("Moves = "+ str(turn))  
    for i in num:  
        if exposed[index]:  
            canvas.draw_text(str(i), (card, 100), 100, "White")  
        else:
            canvas.draw_line((card, 0), (card, 100), 8, "Black")
            canvas.draw_polygon([(card, 0), (card, 100),  
                                 (card + 50, 100),(card + 50, 0)],  
                                1, "Green", "Green")  
        card = card + 50  
        index+=1  
 
 
# create frame and add a button and labels  
frame = simplegui.create_frame("Memory", 800, 100)  
frame.add_button("Restart", new_game)  
label = frame.add_label("Moves = 0")  
 
# initialize global variables  
new_game()  
 
# register event handlers  
frame.set_mouseclick_handler(mouseclick)  
frame.set_draw_handler(draw)  
 
# get things rolling  
frame.start()  
 
