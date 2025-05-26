Web VPython 3.2

scene = canvas(width = 900, height = 600)
scene.background = vector(135/255, 206/255, 235/255)

#scene.userzoom = False
scene.userpan = False
scene.userspin = False

radii = 6378137

earth = sphere(pos = vec(0,0,0), radius = radii, color = color.white, texture = textures.earth)
earth.rotate(axis=vec(1,0,0), angle = pi, origin = vec(0,0,0))
scene.camera.pos = vec(77440.8, 6389600, 278902)
scene.camera.axis = vec(1201350, 551637, 5615770)

Centradius = 30000
pmass = 1
gravity = 9.8
rpm = 1000

centrifugue = cylinder(pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20, axis = vec(1201.350, 551.637, 5615.770), radius = Centradius, color = color.red, texture = textures.wood)

radius_label = wtext(text=f'Radius = {Centradius:.2f} m\n')
pmass_label = wtext(text=f'Penguin Mass = {pmass:.2f} kg\n')
gravity_label = wtext(text=f'Gravity = {gravity:.2f} m/s²\n')
rpm_label = wtext(text=f'RPM = {rpm:.2f}\n')

def update_radius(s):
    global radius
    radius = s.value
    radius_label.text = f'Radius = {radius:.2f} m\n'
    centrifugue.radius = s.value
    centrifugue.pos = scene.camera.pos + vec(1201.350, 551.637, 5615.770) * 20 + (scene.up * (s.value - 30000))
    
radius_slider = slider(min=30000, max=100000, value=Centradius, length=500, bind=update_radius, right=15)
wtext(text='\n\n')

spinning = False

def spin():
    spinning = True
    for i in range(5000):
        rate(rpm)
        centrifugue.rotate(angle = 0.05, axis = vec(1201.350, 551.637, 5615.770))

button(text = "spin", bind = spin)
