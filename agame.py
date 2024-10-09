import turtle

def gameBegin():
   screen = turtle.Screen()
   screen.title("Pong!")
   screen.bgcolor("black")
   screen.setup(width=1000, height=600)

   left = turtle.Turtle()
   left.speed(0)
   left.shape("square")
   left.color("deep pink")
   left.shapesize(stretch_wid=6, stretch_len=2)
   left.penup()
   left.goto(-400, 0)

   right = turtle.Turtle()
   right.speed(0)
   right.shape("square")
   right.color("blue")
   right.shapesize(stretch_wid=6, stretch_len=2)
   right.penup()
   right.goto(400, 0)

   ball = turtle.Turtle()
   ball.speed(50)
   ball.shape("circle")
   ball.color("yellow")
   ball.penup()
   ball.goto(0, 0)
   ball.dx = 5
   ball.dy = -5

   board = turtle.Turtle()
   board.speed(0)
   board.color("white")
   board.penup()
   board.hideturtle()
   board.goto(0, 260)
   board.write("Pink: {}                                  Blue: {}",
                     align="center", font=("Comic Sans", 24, "normal"))

   return screen, ball, left, right, board


def changeScore(leftScore, rightScore, player, board):
   if player == "l":
       leftScore += 1
   else:
       rightScore += 1

   board.clear()
   board.write("Pink: {}                                  Blue: {}".format(
       leftScore, rightScore), align="center",
       font=("Comic Sans", 24, "normal"))
   return leftScore, rightScore, board


def gamePlay():
   gameParts = gameBegin()
   screen = gameParts[0]
   ball = gameParts[1]
   left = gameParts[2]
   right = gameParts[3]
   board = gameParts[4]
   leftScore = 0
   rightScore = 0

   def leftUp():
       left.sety(left.ycor() + 20)

   def leftDown():
       left.sety(left.ycor() - 20)

   def rightUp():
       right.sety(right.ycor() + 20)

   def rightDown():
       right.sety(right.ycor() - 20)

   screen.listen()
   screen.onkeypress(leftUp, "w")
   screen.onkeypress(leftDown, "s")
   screen.onkeypress(rightUp, "Up")
   screen.onkeypress(rightDown, "Down")

   while True:
       screen.update()
       ball.setx(ball.xcor()+ball.dx)
       ball.sety(ball.ycor()+ball.dy)

       if ball.ycor() > 280:
           ball.sety(280)
           ball.dy *= -1

       if ball.ycor() < -280:
           ball.sety(-280)
           ball.dy *= -1

       if ball.xcor() > 500:
           ball.goto(0, 0)
           ball.dy *= -1
           leftScore, rightScore, board = changeScore(
               leftScore, rightScore, "l", board)
           continue

       elif ball.xcor() < -500:
           ball.goto(0, 0)
           ball.dy *= -1
           leftScore, rightScore, board = changeScore(
               leftScore, rightScore, "r", board)
           continue

       if ((ball.xcor() > 360) and
           (ball.xcor() < 380) and
           (ball.ycor() < right.ycor()+50) and
               (ball.ycor() > right.ycor()-50)):
           ball.setx(360)
           ball.dx *= -1

       if ((ball.xcor() < -360) and
               (ball.xcor() > -380) and
               (ball.ycor() < left
        .ycor()+50) and
               (ball.ycor() > left
        .ycor()-50)):
           ball.setx(-360)
           ball.dx *= -1


if __name__ == "__main__":
   gamePlay()