import turtle
my_turtel= turtle.Turtle()
c=my_turtel.clone()
my_turtel.color("red")
c.color("blue")
my_turtel.circle(100)
c.circle(70)
n=10
while n<=50:
    c.circle(n)
    n=n+1

