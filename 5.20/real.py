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
    def __init__(self, cube_data, depth = 1, parent = None, move = None):
        self.cube_class = cube_data # 큐브 상태 rubikcube의 cube 객체 위치 저장
        self.depth = depth # 깊이
        self.parent = parent # 트리 객체 넣으면 될듯 ㅎㅎ
        self.move = move
        self.cost = depth
        self.estimated_cost = self.cost #+ self.heuristic()
        self.score = self.huristic()
        #print(self.score)
    def generate_offspring(self):
        children = []
        for a in range(12):
            new_state = copy.deepcopy(self.cube_class)  # 부모 복사본
            #print(new_state)
            new_state.turn(a)  # turn() 메서드 호출 시 move 값을 전달
            child_node = Tree(new_state, depth=self.depth + 1, parent = self, move= a)
            children.append(child_node)
        return children
    def backtracking(self):
        return("my parent is  " + str(self.parent))

    def huristic(self):
        mapped = get_mapped_cube(self.cube_class.cube)
        score = 0
        for face in mapped:
            for i, sticker in enumerate(face):
                if sticker == chr(ord('A') + i):
                    score += 1
        return score

        for i in self.cube_class.cube:
            print(i)
def spread(stage):
    my_precious_list = cl_list[stage-1]
    highest_score = 0

    # 점수 최댓값 찾기
    for i in range(len(my_precious_list)):
        for a in range(len(my_precious_list[i])):  # ✅ 여기 수정
            if my_precious_list[i][a].score > highest_score:
                highest_score = my_precious_list[i][a].score
                print("점수 갱신!", highest_score, stage)

    # 높은 점수에 해당하는 노드만 자식 생성
    for i in range(len(my_precious_list)):
        for a in range(len(my_precious_list[i])):  # ✅ 여기도 수정
            current_class = my_precious_list[i][a]
            if highest_score - width <= current_class.score:
                cl_list[stage].append(current_class.generate_offspring())

def get_mapped_cube(cube):
    mapped = []
    for face in cube:
        new_face = [s[1] for s in face]  # '0A' → 'A'
        mapped.append(new_face)
    return mapped
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
    for i in range(20):
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
    