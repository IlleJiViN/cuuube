import rubikcube as r_b
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
width = 1
class TreePlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.axis('off')
        self.levels = {}

    def plot_tree(self, data, x=0, y=0, dx=4, level=0):
        label = "list" if isinstance(data, list) else str(data)
        self.ax.text(x, y, label, ha='center', va='center',
                     bbox=dict(boxstyle="round", facecolor='lightblue', edgecolor='gray'))

        if isinstance(data, list):
            count = len(data)
            for i, item in enumerate(data):
                x_child = x + dx * (i - (count - 1) / 2)
                y_child = y - 1.5
                # Draw line
                self.ax.plot([x, x_child], [y - 0.2, y_child + 0.2], 'k-')
                self.plot_tree(item, x_child, y_child, dx / 2, level + 1)
def visualize_nested_list(data):
    tree = TreePlotter()
    tree.plot_tree(data)
    plt.show()

# 테스트용 리스트

def count_leaf_elements(data):
    if isinstance(data, list):
        return sum(count_leaf_elements(item) for item in data)
    else:
        return 1  # 리스트가 아니면 최소 단위니까 1

# 예시
"""nested_list = [[1, 2], [3, [4, 5, [6]]], 7]
print(count_leaf_elements(nested_list))  # 출력: 7 """
#import visual
cl_list = []
for i in range(40):
    cl_list.append([])
class Tree:
    the_best = 1
    def __init__(self, cube_data, depth = 1, parent = None, move = None, phase = 1):
        self.cube_class = cube_data # 큐브 상태 rubikcube의 cube 객체 위치 저장
        self.depth = depth # 깊이
        self.parent = parent # 트리 객체 넣으면 될듯 ㅎㅎ
        self.move = move
        self.cost = depth
        self.estimated_cost = self.cost #+ self.heuristic()
        self.score = self.huristic()
        self.phase = phase
        #print(self.score)
    def huristic(self):
        score = 0
        cube = self.cube_class.cube
        
        for face in cube:
            center = face[4][0]
            score += sum(1 for s in face if s[0] == center)
        
        if is_corner_orientation_valid(cube):
            self.phase = 2
        if is_edge_orientation_valid(cube):
            self.phase = 2
        
        # 십자가 완성 여부에 따라 보너스 점수 추가
        if is_cross_formed(cube):
            self.phase = 2  # 보너스 점수 값은 조절 가능
        
        # Phase 2 조건 (임의 점수 35 이상 & phase2 조건)
        if score >= 35 and is_phase2_condition(cube):
            score += 10
        
        return score


    def huristic_organiztion(self):
        score = 0
        cube = self.cube_class.cube
        for face in cube:
            center = face[4][0]
            score += sum(1 for s in face if s[0] == center)

    # Phase1 성향 판단 보너스
        if is_corner_orientation_valid(cube):
            score += 20  # 코너 방향 다 맞음
        if is_edge_orientation_valid(cube):
            score += 20  # 엣지 방향 다 맞음

        return score

    def generate_offspring(self):
        children = []
        for a in range(12):
            if self.phase == 1 and blablablablabla:
                break
            new_state = copy.deepcopy(self.cube_class)  # 부모 복사본
            #print(new_state)
            new_state.turn(a)  # turn() 메서드 호출 시 move 값을 전달
            child_node = Tree(new_state, depth=self.depth + 1, parent = self, move= a, phase = self.phase)
            children.append(child_node)
        return children
    def backtracking(self):
        return("my parent is  " + str(self.parent))

    """def huristic(self):
        mapped = get_mapped_cube(self.cube_class.cube)
        score = 0
        for face in mapped:
            for i, sticker in enumerate(face):
                if sticker == chr(ord('A') + i):
                    score += 1
        return score
        for i in self.cube_class.cube:
            print(i)"""
def is_cross_formed(cube):
    # 윗면은 4번 면
    face = cube[4]
    center = face[4][0]  # 윗면 중앙 색 (ex: '4')
    
    # 십자가는 윗면의 1,3,5,7 위치 엣지 조각이 중심과 같은 면방향이어야 함
    cross_positions = [1, 3, 5, 7]
    
    for pos in cross_positions:
        sticker = face[pos]
        # 스티커 면 번호가 윗면 번호(4)여야 십자가 조각이 제대로 방향 맞음
        if sticker[0] != center:
            return False
    
    return True

def spread(stage):
    my_precious_list = cl_list[stage-1]
    highest_score = 0

    # 점수 최댓값 찾기
    for i in range(len(my_precious_list)):
        for a in range(len(my_precious_list[i])):  # ✅ 여기 수정
            if my_precious_list[i][a].score > highest_score:
                highest_score = my_precious_list[i][a].score
                print("점수 갱신!", highest_score, stage)
                the_best = my_precious_list[i][a]

    # 높은 점수에 해당하는 노드만 자식 생성
    for i in range(len(my_precious_list)):
        for a in range(len(my_precious_list[i])):  # ✅ 여기도 수정
            current_class = my_precious_list[i][a]
            if highest_score - width <= current_class.score:
                cl_list[stage].append(current_class.generate_offspring())
def is_phase2_condition(cube):
    # 1. 코너, 엣지 방향 모두 맞아야 함
    if not (is_corner_orientation_valid(cube) and is_edge_orientation_valid(cube)):
        return False
    
    # 2. 윗면(4번 면) 스티커 중 중심과 같은 방향의 개수 체크
    upper_face = cube[4]
    center = upper_face[4][0]
    matching_upper = sum(1 for s in upper_face if s[0] == center)
    if matching_upper < 7:  # 예: 9개 중 7개 이상 맞아야 함
        return False
    
    # 3. 추가적으로 목표 위치 가까움 판단 (예: 앞면 0번 위치가 맞으면 True)
    # 간단히 앞면 0번 스티커가 맞으면 True (필요시 더 복잡하게)
    if cube[0][0][0] != '0':
        return False
    
    return True

def get_mapped_cube(cube):
    mapped = []
    for face in cube:
        new_face = [s[1] for s in face]  # '0A' → 'A'
        mapped.append(new_face)
    return mapped
def is_corner_orientation_valid(cube):
    # 코너 조각 인덱스들 (앞면, 윗면, 오른쪽 같은 3색 위치 조합)
    corner_indices = [
        (0, 0), (0, 2), (0, 6), (0, 8),
        (2, 0), (2, 2), (2, 6), (2, 8),
        (4, 0), (4, 2), (4, 6), (4, 8),
        (5, 0), (5, 2), (5, 6), (5, 8)
    ]
    for face_index, idx in corner_indices:
        sticker = cube[face_index][idx]
        if sticker[0] != str(face_index):
            return False
    return True

def is_edge_orientation_valid(cube):
    # 엣지 인덱스 (중앙 4방향에 위치한 조각)
    edge_indices = [
        (0, 1), (0, 3), (0, 5), (0, 7),
        (2, 1), (2, 3), (2, 5), (2, 7),
        (4, 1), (4, 3), (4, 5), (4, 7),
        (5, 1), (5, 3), (5, 5), (5, 7)
    ]
    for face_index, idx in edge_indices:
        sticker = cube[face_index][idx]
        if sticker[0] != str(face_index):
            return False
    return True

if __name__ == "__main__":               # 트리 3차원 구조임 유의할것  # extend 아니라 append 써서 한 집단의 부모 노드는 모두 같음 의도한건 아니고 extend 존재를 몰랐음

    #깊이 1
    cl_list[0].append(Tree(r_b.Cube("df")))
    #깊이 2
    cl_list[1].append(cl_list[0][0].generate_offspring())
    #print(cl_list[1])
    print(len(cl_list[1][0]))
    print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    #깊이 3
    for i in cl_list[1][0]:
        cl_list[2].append(i.generate_offspring())
    #print(cl_list)
    #print(len(cl_list))
    #print(len(cl_list[1]))
    #print(count_leaf_elements(cl_list))
    for i in range(30):
        spread(i+2)
        print(count_leaf_elements(cl_list))
    #spread(3)
    #spread(4)
    #spread(5)
    #spread(6)
    #spread(4)
    #spread(3)

    #print(cl_list)
    print(count_leaf_elements(cl_list))
    #visualize_nested_list(cl_list)
    














if True: # 시각 테스트용
    print("asdfjkhasdkjfads")
    import visual_test
    visual_test.cube_test_switch_activation(cl_list)
    