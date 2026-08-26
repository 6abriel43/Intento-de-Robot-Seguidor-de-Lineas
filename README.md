Simulación de un robot seguidor de líneas utilizando el modelo e-puck en Webots. Implementa un controlador reactivo en Python basado en lectura de sensores infrarrojos para la corrección de trayectorias del seguimiento.

Características Principales

.**Entorno Simulado:** Mundo 3D físico de WeBots
.**Módulo de Sensado:** Integración `E-puckGroundSensors`, que proporciona 3 sensores infrarrojos (izquierdo, central y derecho) "simulados" dirigidos hacia el suelo.
.**Controlador Reactivo (Hecho con Python):** lee los niveles de reflexión de luz y calcula para corregir la trayectoria y abrazar el borde del circuito (linea negra).
.**Lógica de Recuperación:** detecta si el robot ha perdido completamente la pista (los 3 sensores leen blanco) e inicia una rotación sobre su propio eje para buscarla nuevamente (falta configurar el spawn para que no se quede dando vueltas).

Para ejecutar o modificar esta simulación de manera local, se requiere:
1. Instalar [Webots](https://cyberbotics.com/) (Probado en la versión R2025a).
2. Tener [Python](https://www.python.org/) configurado en las variables de entorno (PATH) del sistema operativo.
3. y cargar toda la info del repo
