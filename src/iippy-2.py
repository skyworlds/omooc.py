import simplegui
import math
import time

state = 0
interval = 1000

def new_game():
    global timer, input1, input2, state, interval, brush, color, brush_list, color_list, draw_list
    if timer.is_running():      
        timer.stop()
    input1.set_text('')
    input2.set_text('')
    state = 0
    interval = 1000
    timer = simplegui.create_timer(interval, tick)
    brush = 1
    color = 'Red'
    brush_list=[]
    color_list=[]
    draw_list=[]


def brush_1():
    global brush
    brush = 1
    
def brush_2():
    global brush
    brush = 2

def brush_3():
    global brush
    brush = 3

def playback():
    global timer, state, brush_list, index, brush_list_copy, color_list_copy, draw_list_copy
    if timer.is_running():
        timer.stop()    
    index = 0
    brush_list_copy = []
    color_list_copy = []
    draw_list_copy = []    
    if len(brush_list) > 0:
        state = 2
        timer.start()
    
def input_handler(col):
    global color
    color = col
    
def input_handler_speed(speed):
    try:
        speed = float(speed)
    except ValueError:
        return()
    if speed > 0:
        global timer, interval
        if timer.is_running():      
            timer.stop()        
            interval = speed*1000
            timer = simplegui.create_timer(interval, tick)
            timer.start()
        else:
            interval = speed*1000
            timer = simplegui.create_timer(interval, tick)
        
def mouse_handler(pos):
    global state
    if state < 2:
        global brush, color, brush_list, color_list, draw_list
        state = 1
        if len(brush_list) ==1024:
            brush_list.pop(0)
            brush_list.append(brush)
            color_list.pop(0)
            color_list.append(color)
            draw_list.pop(0)
            draw_list.append(pos)
        else:    
            brush_list.append(brush)
            color_list.append(color)
            draw_list.append(pos)        

def draw(canvas):
    global state
    if state == 1:
        global brush_list, color_list, draw_list
        count = 0
        i = math.sqrt(48)
        for item in brush_list:
            if item == 1:
                canvas.draw_polygon([(draw_list[count][0], draw_list[count][1]-8), (draw_list[count][0]+i, draw_list[count][1]+4), (draw_list[count][0]-i, draw_list[count][1]+4)], 1, color_list[count], color_list[count])
            elif item == 2:
                canvas.draw_polygon([(draw_list[count][0]-8, draw_list[count][1]-8), (draw_list[count][0]+8, draw_list[count][1]-8), (draw_list[count][0]+8, draw_list[count][1]+8), (draw_list[count][0]-8, draw_list[count][1]+8)], 1, color_list[count], color_list[count])
            else:
                canvas.draw_circle(draw_list[count], 8, 1, color_list[count], color_list[count])
            count += 1
    elif state == 2:
        global bursh_list_copy, color_list_copy, draw_list_copy
        count = 0
        i = math.sqrt(48)
        for item in brush_list_copy:
            if item == 1:
                canvas.draw_polygon([(draw_list_copy[count][0], draw_list_copy[count][1]-8), (draw_list_copy[count][0]+i, draw_list_copy[count][1]+4), (draw_list_copy[count][0]-i, draw_list_copy[count][1]+4)], 1, color_list_copy[count], color_list_copy[count])
            elif item == 2:
                canvas.draw_polygon([(draw_list_copy[count][0]-8, draw_list_copy[count][1]-8), (draw_list_copy[count][0]+8, draw_list_copy[count][1]-8), (draw_list_copy[count][0]+8, draw_list_copy[count][1]+8), (draw_list_copy[count][0]-8, draw_list_copy[count][1]+8)], 1, color_list_copy[count], color_list_copy[count])
            else:
                canvas.draw_circle(draw_list_copy[count], 8, 1, color_list_copy[count], color_list_copy[count])
            count += 1
        
        
def tick():
    global state, brush_list, color_list, draw_list, index, brush_list_copy, color_list_copy, draw_list_copy
    brush_list_copy.append(brush_list[index])
    color_list_copy.append(color_list[index])
    draw_list_copy.append(draw_list[index])    
    index += 1
    if index == len(brush_list):
        state = 1
        timer.stop()



frame = simplegui.create_frame("DianHua", 700, 700)
frame.set_canvas_background('White')
frame.add_label("- Choose a brush. -", 200)
frame.add_button("Triangle", brush_1, 100)
frame.add_button("Square", brush_2, 100)
frame.add_button("Circle", brush_3, 100)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("- Change the color. -", 200)
input1 = frame.add_input("", input_handler, 200)
frame.add_label("Enter a color name", 200)
frame.add_label("or a RGB code.", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_button("Playback", playback, 200)
frame.add_label("Note: default setting of playback rate is one step per second.", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("- Change the playback rate. -", 200)
input2 = frame.add_input("", input_handler_speed, 200)
frame.add_label("Note: only positive numbers are valid.", 200)
frame.add_label("e.x. Enter 2 and the rate becomes one step per 2 seconds; enter 0.001 and the rate becomes one step per 1 millisecond.", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_button("Stop and Renew", new_game, 200)


frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

frame.start()
new_game()
