class Cube:             #큐브 윗면 5번째 앞면 1, 그 오른쪽 2 그 오른쪽 3 그 오른쪽 4 밑면 6
    def __init__(self):
        self.mid_list = list()
        self.cube = list()
        self.ar = list()
        self.stage = 0 # 초기값 만들어놈 그냥ㅎ
        for i in range(6):
            self.cube.append([str(i) + "A", str(i) + "B", str(i) + "C", str(i) + "D", str(i) + "E", str(i) +"F", str(i) + "G", str(i) + "H", str(i) + "I"])
        #print(self.cube)
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
        self.cube.clear()
        for i in range(6):
            self.cube.append([str(i) + "A", str(i) + "B", str(i) + "C", str(i) + "D", str(i) + "E", str(i) +"F", str(i) + "G", str(i) + "H", str(i) + "I"])

    def vertical_switch_up(self):
        # 가운데 열을 위로 올리는 수직 회전
        faces = [0, 4, 2, 5]  # 앞, 위, 뒤, 아래
        idxs = [1, 4, 7]      # 가운데 열 인덱스

        # ① 값 수집
        mid_list = []
        for face in faces:
            for idx in idxs:
                mid_list.append(self.cube[face][idx])

        # ② 위로 올리는 회전 (3칸 오른쪽 시프트)
        mid_list = mid_list[-3:] + mid_list[:-3]

        # ③ 다시 각 면에 할당
        for i, face in enumerate(faces):
            for j, idx in enumerate(idxs):
                self.cube[face][idx] = mid_list[i * 3 + j]

        # ④ 가운데면은 존재하지 않으니 별도 면 회전 없음

    def vertical_switch_up_left(self):
        # 왼쪽 열을 위로 올리는 수직 회전
        faces = [0, 4, 2, 5]  # 앞, 위, 뒤, 아래

        # 각 면에 해당하는 인덱스 정의
        idx_map = {
            0: [0, 3, 6],       # 앞면: 정방향
            4: [6, 3, 0],       # 윗면: 반대로
            2: [8, 5, 2],       # 뒷면: 반대로
            5: [0, 3, 6],       # 아랫면: 반대로 넣기
        }

        # ① 값 수집
        mid_list = []
        for face in faces:
            for idx in idx_map[face]:
                mid_list.append(self.cube[face][idx])

        # ② 위로 올리는 회전 (3칸 오른쪽 시프트)
        mid_list = mid_list[-3:] + mid_list[:-3]

        # ③ 다시 입력
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]

        # ④ 왼쪽면(3번) 반시계 회전
        self.cube[3] = rotate_90_counterclockwise(self.cube[3])


    """def vertical_switch_up_left(self):
        print("ㅇㄴ마ㅣ;ㄴㄹㅇ")
        self.ar = []
        for a in [0, 4, 2, 5]:
            i_list = [2, 5, 8] if a == 2 else [0, 3, 6]
            for i in i_list:
                self.mid_list.append(self.cube[a][i])

        for i in range(3):
            self.first_value = self.mid_list.pop(11)
            self.mid_list.insert(0, self.first_value)
        for i in range(4):
            self.ar.append([self.mid_list[i * 3], self.mid_list[i*3 + 1], self.mid_list[i * 3 + 2]])

        for i in range(4):
            idx_map = [0, 3, 6] if i != 2 else [2, 5, 8]
            for a in range(3):
                self.cube[[0, 4, 2, 5][i]][idx_map[a]] = self.ar[i][a]

        self.cube[3] = rotate_90_counterclockwise(self.cube[3])
        self.mid_list.clear()"""
    """    def vertical_switch_up_right(self):
        self.ar = []
        self.mid_list.clear()

        faces = [0, 4, 2, 5]
        idx_map = {
            0: [2, 5, 8],  # 앞면
            4: [2, 5, 8],  # 윗면
            2: [2, 5, 8],  # 뒷면
            5: [0, 3, 6],  # 아랫면
        }

        # 값 수집
        for face in faces:
            for idx in idx_map[face]:
                self.mid_list.append(self.cube[face][idx])

        # 위로 올리기 (rotate left 3)
        self.mid_list = self.mid_list[-3:] + self.mid_list[:-3]

        # 다시 배치
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = self.mid_list[i * 3 + j]

        # 오른쪽 면을 시계 방향으로 회전
        self.cube[1] = rotate_90(self.cube[1])
        self.mid_list.clear()
"""
    def vertical_switch_up_right(self):
        # 오른쪽 열을 위로 올리는 수직 회전
        faces = [0, 4, 2, 5]  # 앞, 위, 뒤, 아래
        idx_map = {
            0: [2, 5, 8],       # 앞면: 오른쪽 열
            4: [8, 5, 2],       # 윗면: 반대로 수집
            2: [6, 3, 0],       # 뒷면: 반대로 수집
            5: [2, 5, 8],       # 아랫면: 오른쪽 열
        }

        mid_list = []

        # ① 값 수집
        for face in faces:
            for idx in idx_map[face]:
                mid_list.append(self.cube[face][idx])

        # ② 위로 올리기 (3칸 오른쪽 shift)
        mid_list = mid_list[-3:] + mid_list[:-3]

        # ③ 다시 배치
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]
        self.cube[1] = rotate_90(self.cube[1])









    def vertical_switch_down_left(self):
        # 왼쪽 열을 아래로 내리는 수직 회전
        faces = [0, 4, 2, 5]  # 앞, 위, 뒤, 아래

        # 각 면에 해당하는 인덱스 정의
        idx_map = {
            0: [0, 3, 6],       # 앞면: 정방향
            4: [6, 3, 0],       # 윗면: 반대로
            2: [8, 5, 2],       # 뒷면: 반대로
            5: [0, 3, 6],       # 아랫면: 정방향
        }

        # ① 값 수집
        mid_list = []
        for face in faces:
            for idx in idx_map[face]:
                mid_list.append(self.cube[face][idx])

        # ② 아래로 내리는 회전 (3칸 왼쪽 시프트)
        mid_list = mid_list[3:] + mid_list[:3]

        # ③ 다시 입력
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = mid_list[i * 3 + j]

        # ④ 왼쪽면(3번) 시계 방향 회전
        self.cube[3] = rotate_90(self.cube[3])

    def vertical_switch_down_right(self):
        self.mid_list.clear()

        # 면 번호 순서: 앞, 위, 뒤, 아래
        faces = [0, 4, 2, 5]
        idx_map = {
            0: [2, 5, 8],       # 앞면: 오른쪽 열
            4: [8, 5, 2],       # 윗면: 오른쪽 열 (거꾸로)
            2: [6, 3, 0],       # 뒷면: 오른쪽 열 (거꾸로)
            5: [2, 5, 8],       # 아랫면: 오른쪽 열
        }

        # ① 값 수집
        for face in faces:
            for idx in idx_map[face]:
                self.mid_list.append(self.cube[face][idx])

        # ② 아래로 내리기 (3칸 왼쪽 시프트)
        self.mid_list = self.mid_list[3:] + self.mid_list[:3]

        # ③ 다시 넣기
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = self.mid_list[i * 3 + j]

        # ④ 오른쪽 면(1번) 시계 방향 회전
        self.cube[1] = rotate_90_counterclockwise(self.cube[1])



    """def vertical_switch_down_right(self):
        self.ar.clear()
        self.mid_list.clear()

        # 면 인덱스 정의
        face_order = [0, 4, 2, 5]

        # 각 면의 인덱스를 조건에 따라 지정
        for idx in face_order:
            if idx == 2:  # 뒷면은 인덱스 반대
                for i in [2, 5, 8]:
                    self.mid_list.append(self.cube[idx][i])
            else:
                for i in [0, 3, 6]:
                    self.mid_list.append(self.cube[idx][i])

        # 오른쪽 회전 (뒤로 보내기)
        self.mid_list = self.mid_list[-3:] + self.mid_list[:-3]

        # 다시 4면으로 쪼개기
        for i in range(4):
            self.ar.append(self.mid_list[i*3 : (i+1)*3])

        # 각 면에 다시 넣기
        for i in range(4):
            face = face_order[i]
            if face == 2:  # 뒷면은 [2,5,8]
                for a, idx in enumerate([2, 5, 8]):
                    self.cube[face][idx] = self.ar[i][a]
            else:          # 나머지는 [0,3,6]
                for a, idx in enumerate([0, 3, 6]):
                    self.cube[face][idx] = self.ar[i][a]

        # 오른쪽 면 자체를 반시계 방향 회전
        self.cube[1] = rotate_90_counterclockwise(self.cube[1])
"""

    def vertical_switch_down(self):
        self.ar = []
        self.mid_list.clear()

        faces = [0, 4, 2, 5]
        idx_map = {
            0: [1, 4, 7],       # 앞면
            4: [7, 4, 1],       # 윗면 (반대)
            2: [7, 4, 1],       # 뒷면 (반대)
            5: [1, 4, 7],       # 아랫면
        }

        # 값 수집
        for face in faces:
            for idx in idx_map[face]:
                self.mid_list.append(self.cube[face][idx])

        # 첫 번째 값을 꺼내서 뒤로 돌리기 (rotate left 3)
        self.mid_list = self.mid_list[-3:] + self.mid_list[:-3]

        # 다시 배치
        for i, face in enumerate(faces):
            for j, idx in enumerate(idx_map[face]):
                self.cube[face][idx] = self.mid_list[i * 3 + j]

        # mid_list 초기화
        self.mid_list.clear()


















 # 옆 돌기
    def mid_switch_left(self):
        self.ar = []
        self.mid_list.clear()

        # 각 면의 가운데 3개 값 수집
        for a in range(4):
            for i in range(3, 6):  # 3, 4, 5 번째 값을 다룬다
                self.mid_list.append(self.cube[a][i])

        #print(str(self.mid_list) + " 미드 리스트 from mid switch left")

        # 왼쪽으로 회전 (첫 번째 값 pop 후 뒤로 추가)
        for i in range(3):
            self.first_value = self.mid_list.pop(0)  # 첫 번째 값을 꺼냄
            self.mid_list.append(self.first_value)  # 꺼낸 값을 뒤로 추가

        #print(str(self.mid_list) + " 삭제 전 미드 리스트 from mid switch left")

        # 회전된 값을 각 면에 배치
        for i in range(4):
            self.ar.append([self.mid_list[i * 3], self.mid_list[i * 3 + 1], self.mid_list[i * 3 + 2]])

        # 수정된 값을 큐브에 다시 넣기
        for i in range(4):
            for a in range(3):  # 0, 1, 2 번째로 대입
                self.cube[i][a + 3] = self.ar[i][a]

        self.mid_list.clear()


    """    def mid_switch_down_left(self):
        print("테스트트트트트")
        for a in [0,1,2,3]:
            for i in [0,1,2]:
                self.mid_list.append(self.cube[a][i+6])
        for i in range(3):
            self.first_value = self.mid_list.pop(0)
            self.mid_list.append(self.first_value)
        for i in range(4):
            self.ar.append([self.mid_list[i*3], self.mid_list[i*3 + 1], self.mid_list[i*3+2]])
        for i in range(4):
            for a in range(3):
                self.cube[i][a+6] = self.ar[i][a]"""
    def mid_switch_down_left(self):
        #print("테스트트트트트")

        self.mid_list.clear()
        self.ar.clear()

        # 각 면의 하단 줄 (index 6~8) 모으기
        for a in [0, 1, 2, 3]:
            for i in [6, 7, 8]:
                self.mid_list.append(self.cube[a][i])

        # 왼쪽으로 한 칸 회전 (첫 블록을 맨 뒤로)
        self.mid_list = self.mid_list[3:] + self.mid_list[:3]

        # 다시 4면으로 분할
        for i in range(4):
            self.ar.append(self.mid_list[i*3 : (i+1)*3])

        # 적용
        for i in range(4):
            for a in range(3):
                self.cube[i][a+6] = self.ar[i][a]

                
        self.cube[5] = rotate_90_counterclockwise(self.cube[5])
        self.mid_list.clear()





    def mid_switch_upper_left(self):
        self.mid_list = []
        self.ar = []

        # 앞(0), 왼(1), 뒤(2), 오른(3) 면의 윗줄 수집
        for face in [0, 1, 2, 3]:
            for idx in [0, 1, 2]:
                self.mid_list.append(self.cube[face][idx])

        # 왼쪽으로 한 칸 회전 (왼쪽 shift 3칸)
        self.mid_list = self.mid_list[3:] + self.mid_list[:3]

        # 다시 나눠서 각 면에 배치
        for i in range(4):
            self.ar.append(self.mid_list[i*3:i*3+3])

        for i in range(4):
            for j in range(3):
                self.cube[i][j] = self.ar[i][j]

        # 윗면 반시계 방향 회전
        self.cube[4] = rotate_90_counterclockwise(self.cube[4])

        self.mid_list.clear()

    """def mid_switch_upper_left(self):
        faces = [0, 3, 2, 1]  # 앞, 왼, 뒤, 오른 (큐브 기준 좌측 회전 방향)
        idxs = [0, 1, 2]      # 윗줄

        self.mid_list = []
        self.ar = []

        # ① 윗줄 수집
        for face in faces:
            for idx in idxs:
                self.mid_list.append(self.cube[face][idx])

        # ② 왼쪽 회전 (왼쪽으로 3칸 shift)
        self.mid_list = self.mid_list[3:] + self.mid_list[:3]

        # ③ 다시 배치
        for i, face in enumerate(faces):
            for j, idx in enumerate(idxs):
                self.cube[face][idx] = self.mid_list[i * 3 + j]

        # ④ 윗면 시계 방향 회전
        self.cube[4] = rotate_90(self.cube[4])

        # ⑤ 클리어
        self.mid_list.clear()"""


###########################################
# 오른쪽 메소드 3개
    def mid_switch_right(self):
        #print("외애오애애ㅗㅙㅇㅇㅇ")
        #print(self.cube)
        for a in range(4):
            for i in range(3,6):
                #print(self.cube[a][i])
                self.mid_list.append(self.cube[a][i])
        #print(str(self.mid_list) + "미드 리스트 from mid switch right")
        for i in range(3):
            self.first_value = self.mid_list.pop(11)  # 첫 번째 값 1을 꺼냄
            self.mid_list.insert(0, self.first_value)  # 꺼낸
        for i in range(4):
            self.ar.append([self.mid_list[i*3], self.mid_list[i*3+1], self.mid_list[i*3+2]])
        for i in range(4):
            for a in range(3):
                self.cube[i][a+3] = self.mid_list[i*3+a]
        #print(str(self.mid_list) + "삭제전 미드 리스트 from mid switch_right")
        self.mid_list = []
    def upper_switch_right(self):
        self.cube[4] = rotate_90(self.cube[4])
        self.ar = []
        for a in range(4):
            for i in range(3):
                self.mid_list.append(self.cube[a][i])
        #print(str(self.mid_list)+"미드 리스트 from upper switch right")
        for i in range(3):
            self.first_value = self.mid_list.pop(11)
            self.mid_list.insert(0, self.first_value)
        for i in range(4):
            self.ar.append([self.mid_list[i*3], self.mid_list[i*3 + 1], self.mid_list[i*3 + 2]])
        for i in range(4):
            for a in range(3):
                self.cube[i][a] = self.mid_list[i*3+a]
        #print(str(self.mid_list) + "삭제전 미드 리스트 from dupper switch right")
        self.mid_list = [] 

    """def dupper_switch_left(self):
        self.cube[5] = rotate_90(self.cube[5])
        self.ar = []
        for a in range(4):
            for i in range(6,9):
                self.mid_list.append(self.cube[a][i])
        print(str(self.mid_list)+"미드 리스트 from dupper switch right")
        for i in range(3):
            self.first_value = self.mid_list.pop(0)
            self.mid_list.append(self.first_value)
        for i in range(4):
            self.ar.append([self.mid_list[i*3], self.mid_list[i*3 + 1], self.mid_list[i*3 + 2]])
        for i in range(4):
            for a in range(3):
                self.cube[i][a+6] = self.mid_list[i*3+a]
        print(str(self.mid_list) + "삭제전 미드 리스트 from upper switch right")
        self.mid_list = []
                    """
    def down_switch_right(self):
        self.cube[5] = rotate_90(self.cube[5])
        #print(self.cube[5])
        #print("slkdj;fjdajlsdjjsdjfkl;sjsdjfkl;jflsjlfsdfjlsdfjsl;jflkj;f")
        self.ar = []
        for a in range(4):
            for i in range(6,9):
                self.mid_list.append(self.cube[a][i])
        #print(str(self.mid_list)+"미드 리스트 from dupper switch right")
        for i in range(3):
            self.first_value = self.mid_list.pop(11)
            self.mid_list.insert(0, self.first_value)
        for i in range(4):
            self.ar.append([self.mid_list[i*3], self.mid_list[i*3 + 1], self.mid_list[i*3 + 2]])
        for i in range(4):
            for a in range(3):
                self.cube[i][a+6] = self.mid_list[i*3+a]
        #print(str(self.mid_list) + "삭제전 미드 리스트 from upper switch right")
        self.mid_list = []














def rotate_90_counterclockwise(matrix): #반시계 방향
    thing = [matrix[i:i+3] for i in range(0, 9, 3)]
    # 1. 전치 (행과 열을 바꿈)
    transposed = list(map(list, zip(*thing)))
    
    # 2. 열을 뒤집음 (리스트 전체를 뒤집음)
    rotated = transposed[::-1]
    ret = list()
    for i in range(3):
        for a in range(3):
            ret.append(rotated[i][a])
    return ret
def rotate_90(matrix): #시계 방향으로 돌리기
    thing = [matrix[i:i+3] for i in range(0, 9, 3)]
    # 1. 전치 (행과 열을 바꿈)
    transposed = list(map(list, zip(*thing)))
    
    # 2. 각 행을 뒤집음
    rotated = [row[::-1] for row in transposed]
    ret = list()
    for i in range(3):
        for a in range(3):
            ret.append(rotated[i][a])
    return ret
a = Cube()
if __name__ == "__main__":
    print("sadlkjfslkjl;sdjfksjfsdlkjfsdasdfsdafsdasdafsd")
    #a = Cube()
    print(" let's go debugging")
#a.vertical_switch_up()
#print(a.cube)
#a#.vertical_switch_up_left()
#print(a.cube)
#a.vertical_switch_up_left()
#p#rint(a.cube)
#a.vertical_switch_up_left()
#print(a.cube)
#a.vertical_switch_down()

#a.vertical_switch_down() # 잘됨
#a.vertical_switch_down_left()          #아래로 돌리기
#print(a.cube)
#a.vertical_switch_down_right()
#print(a.cube)

#a.mid_switch_down_left() #  문제 해결
#print(a.cube)

#a.mid_switch_left()  #문제 해결        # 왼쪽 돌리기
#print(a.cube)
#a.mid_swtich_upper_left() #작동 됨
#print(a.cube)



#a.mid_switch_right() #작동 됨
#print(a.cube)
#a.upper_switch_right() #작동 됨          # 오른쪽 돌리기
#print(a.cube)
#a.down_switch_right() # 잘 작동 됨
#print(a.cube)

#a.vertical_switch_up() # 잘됨
#print(a.cube)
#a.vertical_switch_up_left() #잘됨  #위로 돌리기
#a.vertical_swtich_up_right() #잘됨
#print(a.cube)


#a.upper_switch_right()
##a.mid_switch_right()
#a.dupper_switch_right()
#a.upper_switch_right
#a.upper_switch_right()
#a.dupper_switch_right()
#a.mid_switch_right()
#print(a.cube)
#a.mid_switch_right()
#print("확인용요요ㅛ요요용용")

#a.mid_switch_left()
#print("옆돌기 확인")
#print(a.cube)
#print(len(a.cube))


# 현재 앞면 오른쪽 돌리기 완전 구현 가운데 오른쪽 돌리기 위 오른쪽 돌리기 아래 오른쪽 돌리기
# 다음에 할거 위 아래 움직임 구현 하하하하하
# + 왼쪽 움직임 구현