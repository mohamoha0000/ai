import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
CELL_SIZE = WIDTH // 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game variables
board = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# Fonts
font = pygame.font.Font(None, 100)

def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), LINE_WIDTH)

def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                color = RED
            elif board[row][col] == "O":
                color = BLUE
            else:
                continue

            text = font.render(board[row][col], True, color)
            text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(text, text_rect)

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # Check for tie
    if all(cell is not None for row in board for cell in row):
        return "Tie"

    return None

def reset_game():
    global board, current_player, game_over
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

# Main loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            row, col = mouse_y // CELL_SIZE, mouse_x // CELL_SIZE

            if board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    game_over = True
                    if winner != "Tie":
                        print(f"{winner} wins!")
                    else:
                        print("It's a tie!")
                else:
                    current_player = "O" if current_player == "X" else "X"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    draw_grid()
    draw_marks()
    pygame.display.flip()
