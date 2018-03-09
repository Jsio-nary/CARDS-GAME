import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
#image=simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
image=simplegui._LocalImage('E:/second/image_python_memory.gif')
card_len=8
result = random.sample(range(9),int(card_len/2))
result=result+result
random.shuffle(result)
position=[100,100]
index=[1,1,1,1,1,1,1,1,1,1,1,1]
count=0
b=[2,3]
turn_time=0
def newgame():#重置游戏
    global index,turn_time,count
    index=[1,1,1,1,1,1,1,1,1,1,1,1]
    turn_time=0
    label.set_text('turns=0')
def draw(canvas):#画布
    for i in range(card_len):
        if index[i]==1:
            canvas.draw_image(image,(300/2,400/2),(300,400),
                              (position[0]*(2*i+1)/2,position[1]/2),position)
        else:
            canvas.draw_text(str(result[i]),
                              (position[0] *(i+0.25), position[1]-20),100,'white')
def tick(pos):#判定两个是否一样
    global index,count,turn_time
    mouseplace=pos
    a = int(mouseplace[0] / position[0])
    if index[a]==1:
        if count<=1:
            b[count]=a
            index[a]=0
            count=count+1
        else:
            if result[b[0]]!=result[b[1]]:
                index[a]=0
                index[b[0]] = 1
                index[b[1]] = 1
                count=1
                b[0]=a
                turn_time+=1
                label.set_text('turns=' + str(turn_time))
            else:
                count=1
                index[a] = 0
                b[0]=a
                turn_time+=1
                label.set_text('turns=' + str(turn_time))
fr=simplegui.create_frame('day4',800,100)
fr.set_draw_handler(draw)
fr.set_mouseclick_handler(tick)
fr.add_button("Reset", newgame)
label = fr.add_label('turns='+str(turn_time))
fr.start()
