from PIL import Image, ImageDraw

#Crea una imagen blanca de 1024x1024 píxeles
img = Image.new('RGB', (1024, 1024), color='white')
draw = ImageDraw.Draw(img)

#Dibuja un circuito básico (una elipse gruesa)
# [x_inicial, y_inicial, x_final, y_final]
draw.ellipse([150, 150, 874, 874], outline='black', width=40)

draw.line([150, 512, 512, 150], fill='black', width=40) 

#Guarda la imagen lista para webots
img.save('pista_seguidor.png')
print("Imagen de pista generada con éxito")