def read_obj_file(file_path):
    vertices = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertex = line.strip().split()[1:]
                vertex = [float(coord) for coord in vertex]
                vertices.append(vertex)

    with open("site.mcfunction", 'w') as f:
        for vertex in vertices:
            s = 10
            x = round(vertex[0] * s, 4)
            y = round(vertex[1] * s, 4)
            z = round(vertex[2] * s, 4)

            cmd = "particle endRod ~{0} ~{1} ~{2} 0 0 0 0.1 0".format(x,y + 1,z)
            f.write(cmd + '\n')

obj_file_path = 'site_main.obj'
vertices = read_obj_file(obj_file_path)