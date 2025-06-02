Web VPython 3.2

scene = canvas(width = 900, height = 600)
scene.background = vector(135/255, 206/255, 235/255)

#scene.userzoom = False
#scene.userpan = False
#scene.userspin = False

radii = 6378137

earth = sphere(pos = vec(0,0,0), radius = radii, color = color.white, texture = textures.earth)
earth.rotate(axis=vec(1,0,0), angle = pi, origin = vec(0,0,0))
scene.camera.pos = vec(77440.8, 6389600, 278902)
scene.camera.axis = vec(1201350, 551637, 5615770)

Centradius = 15000
pmass = 1
gravity = 9.8
rpm = 2000
speed = 120

theta = 0;

centrifugue = cylinder(pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20 + (scene.up * -1 * Centradius), axis = vec(1201.350, 551.637, 5615.770), radius = Centradius, color = color.red, texture = textures.wood)

penguin = cylinder(pos = centrifugue.pos + vec(1201.350, 551.637, 5615.770) * -5 + vec(0, centrifugue.radius * -3/7 * cos(theta), 0), radius = 2500, axis = vec(120.1350, 55.1637, 561.5770), color = color.white, 
make_trail = True, trail_radius = 500, trail_type = "points", retain = 20, 
texture = "https://th.bing.com/th/id/OIP.Kbkh1q-J4T8vnU2NM1DW6AHaI-?w=149&h=180&c=7&r=0&o=5&pid=1.7")

radius_label = wtext(text=f'\nRadius = {Centradius/1000:.2f} m\n')
pmass_label = wtext(text=f'Penguin Mass = {pmass:.2f} kg\n')
gravity_label = wtext(text=f'Gravity = {gravity:.2f} m/s²\n')
rpm_label = wtext(text=f'RPM = {rpm:.2f}\n')
speed_label = wtext(text=f'Simulation Speed = {speed:.2f}\n')

def update_radius(s):
    global radius, actualRadius
    radius = s.value
    radius_label.text = f'Radius = {radius/1000:.2f} m\n'
    centrifugue.radius = s.value
    centrifugue.pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20 + (scene.up * -1 * Centradius) + (scene.up * (s.value - 15000))
    actualRadius = s.value / 1000

def update_pmass(s):
    global pmass
    pmass = s.value
    pmass_label.text = f'Penguin Mass = {pmass:.2f} kg\n'
    
def update_gravity(s):
    global gravity
    gravity = s.value
    gravity_label.text = f'Gravity = {gravity:.2f} m/s²\n'
    
def update_rpm(s):
    global rpm
    rpm = s.value
    rpm_label.text = f'RPM = {rpm:.2f}\n'
def update_speed(s):
    global speed
    speed = s.value
    speed_label.text = f'Speed = {speed:.2f}\n'
    
centradius_slider = slider(min=15000, max=45000, value=Centradius, length=500, bind=update_radius, right=15)
wtext(text=f'Centrifuge Radius \n\n')
pmass_slider = slider(min=0.1, max=200, value=pmass, length=500, bind=update_pmass, right=15)
wtext(text=f'Penguin Mass \n\n')
gravity_slider = slider(min=0, max=20, value=gravity, length=500, bind=update_gravity, right=15) 
wtext(text=f'Gravity \n\n')
rpm_slider = slider(min=0, max=6000, value=rpm, length=500, bind=update_rpm, right=15, step = 5)
wtext(text=f'RPM \n\n')
speed_slider = slider(min=0, max=2000, value=speed, length=500, bind=update_speed, right=15, step = 5)
wtext(text=f'Simulation Speed \n\n')

launched = False

def spin():
    spinner.disabled = True
    for i in range(5 * rpm):
        rate(rpm)
        centrifugue.rotate(angle = 0.05, axis = vec(1201.350, 551.637, 5615.770))
        theta = i*0.05
        penguin.pos = penguin.pos + vec(centrifugue.radius * (1.02/28) * cos(theta), centrifugue.radius * (1.02/28) * sin(theta), 0)
    spinner.disabled = False
    launch()
    

actualRadius = centrifugue.radius / 1000
velocity = actualRadius * (2 * pi) * (rpm / 60) 
acceleration = 9.81
G = 6.67 * (10 ** -11)
M = 6 * (10 ** 24)
dist = penguin.pos - earth.pos
t = 0
dt = 3600
    
def launch():
    global launched
    launched = True
    
spinner = button(text = "spin", bind = spin, disabled = False)

crashed = False
initialVel = actualRadius * (2 * pi) * (rpm / 60)
while True:
    global t
    rate(speed)
    if (t == 0):
        velocity = actualRadius * (2 * pi) * (rpm / 60)
    if (launched):
        dist = penguin.pos - earth.pos
        penguin.pos = penguin.pos + vec(0, velocity, 0)
        velocity = velocity + acceleration
        acceleration = (-1 * G * M) / (dist.mag ** 2)
        if (t % 101 == 0):
            print(dist.mag)
            print(acceleration)
            print(velocity)
            #print(scene.camera.pos)
        if (dist.mag > 6700000):
            penguin.radius = 3000
            scene.camera.pos = penguin.pos + (scene.forward * -1 * 70000)
        else:
            scene.camera.pos = vec(77440.8, 6389600, 278902)
            scene.camera.axis = vec(1201350, 551637, 5615770)
        if (dist.mag < earth.radius - 30000):
            crashed = True
            break
        if (abs(acceleration) < 0.01):
            break
        t += dt

if crashed:
    BadEnding = text(text = 'OH NO! \nIt\'s a penguin \ncrash and burn!!', align = 'center', color = color.red, pos = vec(0, 30000, 0))
    BadEnding.height = 1
    scene.camera.axis = BadEnding.axis.cross(vec(0, -1, 0))
    scene.camera.pos = BadEnding.pos + (scene.camera.axis * -1 * 10)
else:
    GoodEnding = text(text = 'Your penguin journeyed \nto the galaxy far far \naway..', align = 'center', color = color.green, pos = vec(0, 30000, 0))
    GoodEnding.height = 1
    scene.camera.axis = GoodEnding.axis.cross(vec(0, -1, 0))
    scene.camera.pos = GoodEnding.pos + (scene.camera.axis * -1 * 10)



