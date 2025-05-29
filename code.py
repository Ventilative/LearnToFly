Web VPython 3.2

scene = canvas(width = 900, height = 600)
scene.background = vector(135/255, 206/255, 235/255)

scene.userzoom = False
scene.userpan = False
scene.userspin = False

radii = 6378137

earth = sphere(pos = vec(0,0,0), radius = radii, color = color.white, texture = textures.earth)
earth.rotate(axis=vec(1,0,0), angle = pi, origin = vec(0,0,0))
scene.camera.pos = vec(77440.8, 6389600, 278902)
scene.camera.axis = vec(1201350, 551637, 5615770)

Centradius = 15000
pmass = 1
gravity = 9.8
rpm = 600

theta = 0;

centrifugue = cylinder(pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20 + (scene.up * -1 * Centradius), axis = vec(1201.350, 551.637, 5615.770), radius = Centradius, color = color.red, texture = textures.wood)

penguin = sphere(pos = centrifugue.pos + vec(1201.350, 551.637, 5615.770) * -5 + vec(0, centrifugue.radius * -3/7 * cos(theta), 0), radius = 1500, color = color.blue)

radius_label = wtext(text=f'\nRadius = {Centradius/1000:.2f} m\n')
pmass_label = wtext(text=f'Penguin Mass = {pmass:.2f} kg\n')
gravity_label = wtext(text=f'Gravity = {gravity:.2f} m/s²\n')
rpm_label = wtext(text=f'RPM = {rpm:.2f}\n')

def update_radius(s):
    global radius
    radius = s.value
    radius_label.text = f'Radius = {radius/1000:.2f} m\n'
    centrifugue.radius = s.value
    centrifugue.pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20 + (scene.up * -1 * Centradius) + (scene.up * (s.value - 15000))

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
    
centradius_slider = slider(min=15000, max=45000, value=Centradius, length=500, bind=update_radius, right=15)
wtext(text=f'Centrifuge Radius \n\n')
pmass_slider = slider(min=0.1, max=200, value=pmass, length=500, bind=update_pmass, right=15)
wtext(text=f'Penguin Mass \n\n')
gravity_slider = slider(min=0, max=20, value=gravity, length=500, bind=update_gravity, right=15) 
wtext(text=f'Gravity \n\n')
rpm_slider = slider(min=0, max=2000, value=rpm, length=500, bind=update_rpm, right=15, step = 5)
wtext(text=f'RPM \n\n')

def spin():
    spinner.disabled = True
    for i in range(5060):
        rate(rpm)
        centrifugue.rotate(angle = 0.05, axis = vec(1201.350, 551.637, 5615.770))
        theta = i*0.05
        penguin.pos = penguin.pos + vec(centrifugue.radius * (1/30) * cos(theta), centrifugue.radius * (1/30) * sin(theta), 0)
    spinner.disabled = False
    penguin.radius = 50000
    launch()

velocity = 900

def launch():
    for i in range(1000000):
        rate(600)
        penguin.pos = penguin.pos + vec(0, velocity, 0)
        scene.camera.pos += vec(scene.forward * -i)
    
spinner = button(text = "spin", bind = spin, disabled = False)
