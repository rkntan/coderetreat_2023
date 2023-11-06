from app.main import *


def test_initialization():
    board = Board()
    assert board is not None
    assert len(board.game) == ROWS  # Adjust these values based on your implementation
    assert len(board.game[0]) == COLS


def test_count_neighbors():
    board = Board()
    # You may need to adapt this test based on your initial configuration
    # Here we assume that the center cell has 8 neighbors
    center_x = len(board.game) // 2
    center_y = len(board.game[0]) // 2

    # Assuming the initial configuration has all alive neighbors
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                board.game[center_x + i][center_y + j].set_status(True)

    neighbors = board.count_neighbors(center_x, center_y)
    print(f"Debug:  center_x value is {center_x}")
    print(f"Debug:  center_y value is {center_y}")
    assert neighbors == 8


def test_update():
    board = Board()
    board.set_all_cells_status(False)
    # Create a known pattern (blinker)
    board.game[1][0].set_status(True)
    board.game[1][1].set_status(True)
    board.game[1][2].set_status(True)

    # After one update, the pattern should change
    board.update()
    assert not board.game[0][0].is_alive()
    assert board.game[0][1].is_alive()
    assert not board.game[0][2].is_alive()
    assert not board.game[1][0].is_alive()
    assert board.game[1][1].is_alive()
    assert not board.game[1][2].is_alive()
    assert not board.game[2][0].is_alive()
    assert board.game[2][1].is_alive()
    assert not board.game[2][2].is_alive()
