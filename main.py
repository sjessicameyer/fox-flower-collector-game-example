import turtle, time, random

sc = turtle.Screen()
sc.setup(500, 500)
sc.bgpic("bg.gif")
sc.title("Finn the Fox's Flower Collector")
sc.register_shape("flower-red.gif")
sc.register_shape("flower-purple.gif")
sc.register_shape("fox-right.gif")
sc.register_shape("fox-left.gif")
sc.register_shape("floofy.gif")
sc.tracer(0)

shop_floofy = turtle.Turtle()
shop_floofy.up()
shop_floofy.shape("floofy.gif")
shop_floofy.goto(0, -180)

all_floofy = []
def add_floofy(x, y):
  global score
  if score > 10:
    new_floofy = shop_floofy.clone()
    randX = random.randint(-225, 225)
    randY = random.randint(-180, 225)
    new_floofy.goto(randX, randY)
    all_floofy.append(new_floofy)
    new_floofy.target = None
    score -= 10
shop_floofy.onclick(add_floofy)

sk = turtle.Turtle()
sk.ht()
sk.up()
sk.goto(-225, 220)
score = 0

def write_score():
  global score
  sk.clear()
  sk.write(f"Flowers collected: {score}", align="left", font = ("Roman", 17, "normal" ))
write_score()

player = turtle.Turtle()
player.shape("fox-right.gif")
player.up()
player.speed(0)

def on_move():
  detect_coins()
  detect_wall()
  sc.update()
def go_right():
  player.shape("fox-right.gif")
  player.setx(player.xcor()+10)
  on_move()
def go_left():
  player.shape("fox-left.gif")
  player.setx(player.xcor()-10)
  on_move()
def go_up():
  player.sety(player.ycor()+10)
  on_move()
def go_down():
  player.sety(player.ycor()-10)
  on_move()
sc.onkey(go_right, "Right")
sc.onkey(go_left, "Left")
sc.onkey(go_up, "Up")
sc.onkey(go_down, "Down")
sc.listen()

coin = turtle.Turtle()
coin.shape("flower-red.gif")
coin.up()
coin.speed(0)
coin.ht()

all_coins = []
flower_choices = ["flower-purple.gif", "flower-red.gif"]
def random_coin():
  new_coin = coin.clone()
  new_coin.shape(random.choice(flower_choices))
  randX = random.randint(-225, 225)
  randY = random.randint(-180, 225)
  new_coin.goto(randX, randY)
  new_coin.st()
  all_coins.append(new_coin)
for i in range(20):
  random_coin()

def detect_coins():
  global score
  for c in all_coins:
    if c.distance(player) < 50:
      all_coins.remove(c)
      c.ht()
      random_coin()
      score += 1
      write_score()

def detect_wall():
  if player.xcor() > 250:
    player.setx(-250)
  elif player.xcor() <-250:
    player.setx(250)
  elif player.ycor() > 250:
    player.sety(-250)
  elif player.ycor() < -250:
    player.sety(250)

#TIMER CODE
tk = turtle.Turtle()
tk.ht()
tk.up()
tk.goto(-225, 200)
start_time = time.time()

limit = 30
while (time.time()-start_time) < limit:
  seconds = limit-(time.time()-start_time)
  tk.clear()
  tk.write(f"Time remaining: {seconds:.1f}", align = "left", font = ("Courier", 15, "normal"))

  for f in all_floofy:
    if f.target == None:
      f.target = random.choice(all_coins)
    #NEW CODE
    f.setheading(f.towards(f.target))
    f.forward(3)
    while f.target.distance(f) < 30:
      f.target = random.choice(all_coins)
    for c in all_coins:
      if c.distance(f) < 30:
        all_coins.remove(c)
        c.ht()
        random_coin()
        score += 1
        write_score()
  sc.update()
  time.sleep(0.05)

sc.onkey(None, "Up")
sc.onkey(None, "Down")
sc.onkey(None, "Right")
sc.onkey(None, "Left")
tk.goto(0, 80)
tk.color("white")
tk.shape("square")
tk.turtlesize(3, 40)
tk.stamp()
tk.color("maroon")
tk.sety(70)
tk.write(f"Game Over! You collected {score} flowers", align = "center", font = ("Courier", 15, "bold"))
player.home()
sc.update()