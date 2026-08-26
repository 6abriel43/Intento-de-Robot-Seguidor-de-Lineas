from controller import Robot

robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28 

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

sensores = []
for i in range(3):
    sensor = robot.getDevice(f'gs{i}')
    sensor.enable(TIME_STEP)
    sensores.append(sensor)

while robot.step(TIME_STEP) != -1:
    val_izq = sensores[0].getValue()
    val_cen = sensores[1].getValue()
    val_der = sensores[2].getValue()
    
    print(f"I: {val_izq:.1f} | C: {val_cen:.1f} | D: {val_der:.1f}")

    # UMBRAL ajustado según tu lectura (Blanco = 860, Negro = ~300)
    UMBRAL = 600 
    
    # Evaluar qué está viendo cada sensor lateral
    negro_izq = val_izq < UMBRAL
    negro_der = val_der < UMBRAL
    
    # Velocidad crucero
    left_speed = MAX_SPEED * 0.5
    right_speed = MAX_SPEED * 0.5

    # Lógica de corrección en la pista ancha
    if negro_izq and not negro_der:
        # Se está saliendo por la derecha, doblar fuerte a la izquierda
        left_speed = MAX_SPEED * 0.1
        right_speed = MAX_SPEED * 0.6
    elif negro_der and not negro_izq:
        # Se está saliendo por la izquierda, doblar fuerte a la derecha
        left_speed = MAX_SPEED * 0.6
        right_speed = MAX_SPEED * 0.1
    elif not negro_izq and not negro_der and (val_cen > UMBRAL):
        # EMERGENCIA: Los 3 sensores ven blanco (se salió del mapa)
        # Frenar una rueda y dar marcha atrás con la otra para girar en el lugar
        left_speed = MAX_SPEED * 0.3
        right_speed = -MAX_SPEED * 0.3

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)