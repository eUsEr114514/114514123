import random
import math

def generate_sphere_points(radius, num_points):
    points = []
    for i in range(num_points):
        phi = random.uniform(0, 2 * math.pi)
        costheta = random.uniform(-1, 1)
        theta = math.acos(costheta)
        x = radius * math.sin(theta) * math.cos(phi)
        y = radius * math.sin(theta) * math.sin(phi)
        z = radius * math.cos(theta)
        points.append((x, y, z))
        command = f"particle endRod ~{x} ~{y} ~{z} 0 0 0 0.1 0"
        print(command)
    return points

radius = 5.0
num_points = 1000
sphere_points = generate_sphere_points(radius, num_points)

