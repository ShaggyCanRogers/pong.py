import turtle
import winsound  #sisteme ulaiıp ses dosyasını kullandık

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# cisim 1

cisim_a = turtle.Turtle()
cisim_a.speed(0)
cisim_a.shape("square")
cisim_a.color("white")
cisim_a.shapesize(stretch_wid=5,stretch_len=1)
cisim_a.penup()  # bunu silerek bi sdene
cisim_a.goto(-350, 0)

# cisim2

cisim_b = turtle.Turtle()
cisim_a.speed(0)
cisim_b.shape("square")
cisim_b.color("white")
cisim_b.shapesize(stretch_wid=5, stretch_len=1)
cisim_b.penup()  # bunu silerek bi sdene
cisim_b.goto(350, 0)


# top

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()  # bunu silerek bi sdene
ball.goto(0,0)
ball_dx= 0.1 #değişimler iki piksel hareket ediyor
ball_dy= 0.1

#skor
score_a = 0
score_b = 0


#skor ekleme yapalım
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center", font=("Courier",24,"normal"))



#funcs

def cisim_a_up():
    y = cisim_a.ycor()
    y+=20
    cisim_a.sety(y)  #yeni kordinatı bu oluyor

def cisim_a_down():
    y = cisim_a.ycor()
    y-=20
    cisim_a.sety(y)

def cisim_b_up():
    y = cisim_b.ycor()
    y+=20
    cisim_b.sety(y)  #yeni kordinatı bu oluyor

def cisim_b_down():
    y = cisim_b.ycor()
    y-=20
    cisim_b.sety(y)


#keyboard

wn.listen()
wn.onkeypress(cisim_a_up,"w")
wn.onkeypress(cisim_a_down,"s")
wn.listen()
wn.onkeypress(cisim_b_up,"Up")
wn.onkeypress(cisim_b_down,"Down")



# mainloop

while True:
    wn.update()

    #topun hareketine gelelim
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    #sınır kordinatlarına gelince sekmesi lazım
    if (ball.ycor() > 290) :
        ball.sety(290)
        ball_dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) #sondaki işaret sesi bitiriyor donmasını enegelliyor

    elif (ball.ycor() < -290) :
        ball.sety(-290)
        ball_dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 390):
        ball.goto(0,0)
        ball_dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    elif (ball.xcor() < -390):
        ball.goto(0,0)
        ball_dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -340 and ball.ycor() < cisim_a.ycor() + 50 and ball.ycor() > cisim_a.ycor() - 50:
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and ball.ycor() < cisim_b.ycor() + 50 and ball.ycor() > cisim_b.ycor() - 50:
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
