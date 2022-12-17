import turtle as hg

#hg.mode('logo')
hg.setup(800,600)
hg.title('雪容融')
hg.pensize(6)
hg.pencolor('#f2dc95')
hg.speed(10)


#头饰


# 头
hg.circle(100,360)
hg.penup()
hg.goto(-60,100)
hg.pendown()
hg.setheading(90)
for i in range(3):
    print(i)
    hg.circle(-16,180)
    hg.circle(6,180)
# 脸


hg.done()