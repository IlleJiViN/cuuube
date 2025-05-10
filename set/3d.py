import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import rubikcube as a
# 회전 메서드 리스트        q w r a s d f u b v l g 완성

method = [
    a.a.vertical_switch_up_left,
    a.a.vertical_switch_up_right,
    a.a.vertical_switch_up, 
    a.a.vertical_switch_down_left, 
    a.a.vertical_switch_down_right,
    a.a.vertical_switch_down, 
    a.a.down_switch_right,
    a.a.mid_switch_right, 
    a.a.upper_switch_right, 
    a.a.mid_switch_down_left, 
    a.a.mid_switch_upper_left, 
    a.a.mid_switch_left,
    a.a.reset
] #  f 문제 d 는 윗면만 잘못 나옴

# 색상 정의
colors = {
    '0': (1, 0, 0),     # 앞면 - 빨강
    '1': (0, 1, 0),     # 오른쪽 - 초록
    '2': (1, 1, 0),     # 뒷면 - 노랑
    '3': (0, 0, 1),     # 왼쪽 - 파랑
    '4': (1, 1, 1),     # 윗면 - 흰색
    '5': (1, 0.5, 0),   # 아랫면 - 주황
}

# 큐브 객체
cube = a.a

# 위치에 맞는 색상 찾기
def get_colors_for_position(x, y, z):
    face_color = {}

    if z == 1:
        idx = (1 - y) * 3 + (x + 1)
        face_color[0] = colors[cube.cube[0][idx][0]]
    if z == -1:
        idx = (1 - y) * 3 + (1 - x)
        face_color[2] = colors[cube.cube[2][idx][0]]
    if x == 1:
        idx = (1 - y) * 3 + (1 - z)
        face_color[1] = colors[cube.cube[1][idx][0]]
    if x == -1:
        idx = (1 - y) * 3 + (z + 1)
        face_color[3] = colors[cube.cube[3][idx][0]]
    if y == 1:
        idx = (1 - z) * 3 + (x + 1)
        face_color[4] = colors[cube.cube[4][idx][0]]
    if y == -1:
        idx = (1 - z) * 3 + (x + 1)  # ✅ 수정된 밑면 인덱싱
        face_color[5] = colors[cube.cube[5][idx][0]]

    return face_color

# 정육면체 그리기
def draw_cubelet(x, y, z, face_color):
    size = 0.98
    glPushMatrix()
    glTranslatef(x, y, z)

    glBegin(GL_QUADS)
    face_defs = [
        (0, (0,0,1), [(0,0,1), (1,0,1), (1,1,1), (0,1,1)]),
        (1, (1,0,0), [(1,0,1), (1,0,0), (1,1,0), (1,1,1)]),
        (2, (0,0,-1), [(1,0,0), (0,0,0), (0,1,0), (1,1,0)]),
        (3, (-1,0,0), [(0,0,0), (0,0,1), (0,1,1), (0,1,0)]),
        (4, (0,1,0), [(0,1,1), (1,1,1), (1,1,0), (0,1,0)]),
        (5, (0,-1,0), [(0,0,0), (1,0,0), (1,0,1), (0,0,1)]),
    ]

    for face_idx, normal, verts in face_defs:
        if face_idx in face_color:
            glColor3fv(face_color[face_idx])
            for vx, vy, vz in verts:
                glVertex3f((vx - 0.5) * size, (vy - 0.5) * size, (vz - 0.5) * size)
    glEnd()

    glColor3f(0, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINES)
    vertices = [
        (-0.5, -0.5, -0.5),
        ( 0.5, -0.5, -0.5),
        ( 0.5,  0.5, -0.5),
        (-0.5,  0.5, -0.5),
        (-0.5, -0.5,  0.5),
        ( 0.5, -0.5,  0.5),
        ( 0.5,  0.5,  0.5),
        (-0.5,  0.5,  0.5),
    ]
    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]
    for e in edges:
        for v in e:
            glVertex3f(vertices[v][0] * size, vertices[v][1] * size, vertices[v][2] * size)
    glEnd()

    glPopMatrix()

# 전체 큐브 렌더링
def draw_full_cube():
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                if abs(x) + abs(y) + abs(z) > 0:
                    face_color = get_colors_for_position(x, y, z)
                    draw_cubelet(x, y, z, face_color)

# 로그 저장 함수
def log_action(keyname):
    log_text = f"[LOG] Pressed: {keyname}\n[LOG] Cube Front: {cube.cube[0]}\n"
    print(log_text)
    with open("cube_log.txt", "a") as f:
        f.write(log_text)

# 메인 루프
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    rx, ry = 0, 0
    dragging = False
    last_pos = (0, 0)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                dragging = True
                last_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                dragging = False
            elif event.type == MOUSEMOTION and dragging:
                x, y = pygame.mouse.get_pos()
                dx, dy = x - last_pos[0], y - last_pos[1]
                rx += dy * 0.5
                ry += dx * 0.5
                last_pos = (x, y)
            elif event.type == KEYDOWN:
                keymap = {
                    K_r: "R", K_l: "L", K_u: "U",
                    K_d: "D", K_f: "F", K_b: "B",
                    K_q: "R'", K_a: "L'", K_w: "U'",
                    K_s: "D'", K_g: "F'", K_v: "B'",
                    K_z: "Z"
                }
                if event.key in keymap:
                    p = list(keymap).index(event.key)
                    print(p)
                    method[p]()  # 함수 실행
                    log_action(keymap[event.key])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glRotatef(rx, 1, 0, 0)
        glRotatef(ry, 0, 1, 0)
        draw_full_cube()
        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

main()
