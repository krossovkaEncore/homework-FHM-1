import math

a = 1
b = math.sqrt(3)

r = math.sqrt(a ** 2 + b ** 2)

cos_phi = a / r
sin_phi = b / r

phi = math.atan2(b, a)

print("r =", r)
print("cos(phi) =", cos_phi)
print("sin(phi) =", sin_phi)
print("phi =", phi)
print("phi в градусах =", math.degrees(phi))
