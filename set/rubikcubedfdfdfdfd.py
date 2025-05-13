
class Cube:
    def __init__(self, mix=None):
        self.cube = [[f"{i}{c}" for c in "ABCDEFGHI"] for i in range(6)]
        if mix is not None:
            import random
            for _ in range(random.randint(1, 1000)):
                self.turn(random.randint(0, 11))

    def turn(self, ving):
        method = [
            self.vertical_switch_up_left,
            self.vertical_switch_up_right,
            self.vertical_switch_up,
            self.vertical_switch_down_left,
            self.vertical_switch_down_right,
            self.vertical_switch_down,
            self.down_switch_right,
            self.mid_switch_right,
            self.upper_switch_right,
            self.mid_switch_down_left,
            self.mid_switch_upper_left,
            self.mid_switch_left
        ]
        method[ving]()

    def reset(self):
        self.cube = [[f"{i}{c}" for c in "ABCDEFGHI"] for i in range(6)]

    def vertical_switch_up(self):
        faces = [0, 4, 2, 5]
        idxs = [1, 4, 7]
        mid_list = [self.cube[face][idx] for face in faces for idx in idxs]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idxs):
                self.cube[face][idx] = mid_list[i * 3 + j]

    def vertical_switch_up_left(self):
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [0, 3, 6],
            4: [6, 3, 0],
            2: [8, 5, 2],
            5: [0, 3, 6],
        }
        mid_list = [self.cube[face][idx] for face in faces for idx in idx_map[face]]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]
        self.cube[3] = rotate_90_counterclockwise(self.cube[3])

    def vertical_switch_up_right(self):
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [2, 5, 8],
            4: [8, 5, 2],
            2: [6, 3, 0],
            5: [2, 5, 8],
        }
        mid_list = [self.cube[face][idx] for face in faces for idx in idx_map[face]]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]
        self.cube[1] = rotate_90(self.cube[1])

    def vertical_switch_down_left(self):
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [0, 3, 6],
            4: [6, 3, 0],
            2: [8, 5, 2],
            5: [0, 3, 6],
        }
        mid_list = [self.cube[face][idx] for face in faces for idx in idx_map[face]]
        mid_list = mid_list[3:] + mid_list[:3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]
        self.cube[3] = rotate_90(self.cube[3])

    def vertical_switch_down_right(self):
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [2, 5, 8],
            4: [8, 5, 2],
            2: [6, 3, 0],
            5: [2, 5, 8],
        }
        mid_list = [self.cube[face][idx] for face in faces for idx in idx_map[face]]
        mid_list = mid_list[3:] + mid_list[:3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]
        self.cube[1] = rotate_90_counterclockwise(self.cube[1])

    def vertical_switch_down(self):
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [1, 4, 7],
            4: [7, 4, 1],
            2: [7, 4, 1],
            5: [1, 4, 7],
        }
        mid_list = [self.cube[face][idx] for face in faces for idx in idx_map[face]]
        mid_list = mid_list[3:] + mid_list[:3]
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]

    def mid_switch_left(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(3, 6)]
        mid_list = mid_list[3:] + mid_list[:3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j + 3] = mid_list[i * 3 + j]

    def mid_switch_right(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(3, 6)]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j + 3] = mid_list[i * 3 + j]

    def mid_switch_down_left(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(6, 9)]
        mid_list = mid_list[3:] + mid_list[:3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j + 6] = mid_list[i * 3 + j]
        self.cube[5] = rotate_90_counterclockwise(self.cube[5])

    def mid_switch_upper_left(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(3)]
        mid_list = mid_list[3:] + mid_list[:3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j] = mid_list[i * 3 + j]
        self.cube[4] = rotate_90_counterclockwise(self.cube[4])

    def upper_switch_right(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(3)]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j] = mid_list[i * 3 + j]
        self.cube[4] = rotate_90(self.cube[4])

    def down_switch_right(self):
        mid_list = [self.cube[i][j] for i in range(4) for j in range(6, 9)]
        mid_list = mid_list[-3:] + mid_list[:-3]
        for i in range(4):
            for j in range(3):
                self.cube[i][j + 6] = mid_list[i * 3 + j]
        self.cube[5] = rotate_90(self.cube[5])


def rotate_90(matrix):
    grid = [matrix[i:i+3] for i in range(0, 9, 3)]
    return [grid[j][i] for i in range(3) for j in reversed(range(3))]

def rotate_90_counterclockwise(matrix):
    grid = [matrix[i:i+3] for i in range(0, 9, 3)]
    return [grid[j][i] for i in reversed(range(3)) for j in range(3)]
