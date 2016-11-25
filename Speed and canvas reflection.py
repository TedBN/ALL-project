aSpeed = 1
bSpeed = 2

while True:
    w.move(robot, aSpeed, bSpeed)
    Pos = w.coords(robot)
    if Pos[3] >=600 or Pos[1] <=0:
        aSpeed = -aSpeed
    if Pos[2] >=1500 or Pos[0] <=0:
        bSpeed = -bSpeed
