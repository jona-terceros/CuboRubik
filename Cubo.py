import heapq
from copy import deepcopy

class RubiksCube:
    def __init__(self):

        self.up = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
        self.down = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
        self.left = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        self.right = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
        self.back = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
        self.front = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]

    def _get_color_name(self, color):
        if color == 1:
            return 'White'
        elif color == 2:
            return 'Yellow'
        elif color == 3:
            return 'Orange'
        elif color == 4:
            return 'Red'
        elif color == 5:
            return 'Blue'
        elif color == 6:
            return 'Green'
        else:
            return 'Desconocida'   
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) != 6:
                    print("El archivo debe contener exactamente 6 líneas.")
                    return

                faces = [self.up, self.down, self.left, self.right, self.back, self.front]
                center_count = {'W': 0, 'Y': 0, 'O': 0, 'R': 0, 'B': 0, 'G': 0}  
                for i, line in enumerate(lines):
                    colors = line.strip().split(',')
                    if len(colors) != 9:
                        print(f"La Cara {self._get_color_name(i+1)} no contiene 9 colores.")
                        return
                    for j, color in enumerate(colors):
                        if j in [4]: 
                            center_count[color] += 1  

                    for j in range(3):
                        faces[i][j] = colors[j*3:(j+1)*3]

                for color, count in center_count.items():
                    if count > 1:  
                        print(f"Error: Hay {count} centros de color {color}, por favor no utilices un color más de una vez como centro.")

                print("Cubo cargado correctamente desde el archivo.")

        except FileNotFoundError:
            print("Archivo no encontrado.")

    def copy(self):
        return deepcopy(self)

    def apply_move(self, move):
        if move == 'U':
            self.rotate_face_clockwise(self.up)
            self.rotate_adjacent_edges_clockwise_U([self.left, self.front, self.right, self.back])
        elif move == "U'":
            self.rotate_face_counterclockwise(self.up)
            self.rotate_adjacent_edges_counterclockwise_U([self.left, self.front, self.right, self.back])
        elif move == 'D':
            self.rotate_face_clockwise(self.down)
            self.rotate_adjacent_edges_clockwise_D([self.left, self.front, self.right, self.back])
        elif move == "D'":
            self.rotate_face_counterclockwise(self.down)
            self.rotate_adjacent_edges_counterclockwise_D([self.left, self.front, self.right, self.back])
   
    def rotate_face_clockwise(self, face):
        face[:] = [list(row[::-1]) for row in zip(*face)]

#////////////////////////////////////////////////////////////////////////////////
    def rotate_adjacent_edges_clockwise_U(self, edge_faces):
        first_row = edge_faces[0][0]
        for i in range(len(edge_faces)-1):
            edge_faces[i][0] = edge_faces[i+1][0]
        edge_faces[-1][0] = first_row
#////////////////////////////////////////////////////////////////////////////////

    def rotate_adjacent_edges_clockwise_D(self, edge_faces):
        last_rows = [face[-1] for face in edge_faces]
        for i in range(len(edge_faces) - 1, 0, -1):
            edge_faces[i][-1] = edge_faces[i - 1][-1]
        edge_faces[0][-1] = last_rows[-1]
 
#////////////////////////////////////////////////////////////////////////////////
    def rotate_face_counterclockwise(self, face):
        face[:] = [list(row) for row in zip(*face)][::-1]

#////////////////////////////////////////////////////////////////////////////////

    def rotate_adjacent_edges_counterclockwise_U(self, edge_faces):
        last_row = edge_faces[-1][0]
        for i in range(len(edge_faces)-1, 0, -1):
            edge_faces[i][0] = edge_faces[i-1][0]
        edge_faces[0][0] = last_row

#////////////////////////////////////////////////////////////////////////////////       
    def rotate_adjacent_edges_counterclockwise_D(self, edge_faces):
        # Guarda la primera fila de las caras actuales
        first_rows = [face[0] for face in edge_faces]

        # Rotación de las últimas filas entre las caras en sentido antihorario
        for i in range(len(edge_faces) - 1):
            edge_faces[i][-1] = edge_faces[i + 1][-1]

        # La última fila toma la primera fila original
        edge_faces[-1][-1] = first_rows[0]

#////////////////////////////////////////////////////////////////////////////////
       
    def is_solved(self):
        for face in [self.up, self.down, self.left, self.right, self.back, self.front]:
            color = face[0][0]
            if any(color != cell for row in face for cell in row):
                return False
        return True

class Node:
    def __init__(self, cube, moves=[]):
        self.cube = cube
        self.moves = moves

    def __lt__(self, other):
        return len(self.moves) < len(other.moves)

def get_target_coords(cell):
    if cell == 'W':
        return (0, 0, 0) 
    elif cell == 'R':
        return (1, 1, 1)  
    elif cell == 'G':
        return (1, 0, 1)  
    elif cell == 'B':
        return (1, 1, 0)  
    elif cell == 'O':
        return (1, 0, 0)  
    elif cell == 'Y':
        return (2, 0, 1)  
    else:
        raise ValueError(f"Valor de celda desconocido: {cell}")

def heuristic(cube):
    total_distance = 0
    for face_index, face in enumerate(cube.state):
        for row_index, row in enumerate(face):
            for col_index, cell in enumerate(row):
                current_coords = (face_index, row_index, col_index)
                target_coords = get_target_coords(cell)  
                distance = sum(abs(current - target) for current, target in zip(current_coords, target_coords))
                total_distance += distance

    for face_index, face in enumerate(cube.state):
        current_orientation = tuple(face[0][0] for face in cube.state)
        target_orientation = ('W', 'Y', 'O', 'R', 'B', 'G') 
        orientation_distance = sum(current != target for current, target in zip(current_orientation, target_orientation))
        total_distance += orientation_distance

    return total_distance

def astar(cube):
    open_set = [Node(cube)]
    closed_set = set()
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.cube.is_solved():
            return current_node.moves
        cube_state_tuple = tuple(tuple(row) for face in [current_node.cube.up, current_node.cube.down,
                                                          current_node.cube.left, current_node.cube.right,
                                                          current_node.cube.back, current_node.cube.front] for row in face)
        closed_set.add(cube_state_tuple)
        for move in ['U', 'U\'','D', 'D\'']:
            new_cube = current_node.cube.copy()
            new_cube.apply_move(move)
            new_cube_state_tuple = tuple(tuple(row) for face in [new_cube.up, new_cube.down,
                                                                 new_cube.left, new_cube.right,
                                                                 new_cube.back, new_cube.front] for row in face)
            if new_cube_state_tuple not in closed_set:
                new_node = Node(new_cube, current_node.moves + [move])
                heapq.heappush(open_set, new_node)

    return None


def solve_cube():
    cube = RubiksCube()
    cube.load_from_file('state_cube.txt')   

    print("Estado inicial del cubo:")
    print_cube(cube)
    #///////////////////////////////////////
    solution = astar(cube)
    if solution:
        print("La solucion es:")
        print(solution)
    else:
        print("No se encontró solución.")

def print_cube(cube):
  
    print("      " + " ".join(cube.up[0]))
    print("      " + " ".join(cube.up[1]))
    print("      " + " ".join(cube.up[2]))
    for i in range(3):
        print(" ".join(cube.left[i]) + " " + " ".join(cube.front[i]) + " " + " ".join(cube.right[i]) + " " + " ".join(cube.back[i]))
    print("      " + " ".join(cube.down[0]))
    print("      " + " ".join(cube.down[1]))
    print("      " + " ".join(cube.down[2]))

if __name__ == "__main__":
    solve_cube()
