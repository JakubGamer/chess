from color import Color
from game_state.board import Board
from game_state.castling_permissions import GlobalCastlingPermissions


class GameState:

    def __init__(self):
        self.board = Board()
        self.color_to_move = Color.WHITE
        self.global_castling_permissions = GlobalCastlingPermissions()
        self.en_passant_target_square = None
        self.halfmove_clock = 0
        self.fullmove_count = 0