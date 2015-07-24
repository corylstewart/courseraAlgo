import java.util.Stack;

/**
 * Created by cory1 on 7/22/2015.
 */
public class Board {
    private int[][] board;
    private int size;

    public Board(int[][] board) {
        int N = board.length;
        this.board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                this.board[i][j] = board[i][j];
            }
        }
        this.size = board.length;
    }

    private boolean swap(int i, int j, int x, int y) {
        if (x < 0 || x >= this.size || y < 0 || y >= this.size) {
            return false;
        } else {
            int a = this.board[i][j];
            this.board[i][j] = this.board[x][y];
            this.board[x][y] = a;
            return true;
        }
    }

    public int dimension() {
        return this.size;
    }

    public int hamming() {
        int wrong = 0;
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size; j++)  {
                if (this.board[i][j] != (i*this.size + j + 1) && this.board[i][j] != 0) {
                    wrong += 1;
                }
            }
        }
        return wrong;
    }

    public int manhattan() {
        int wrong = 0;
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size; j++)  {
                if (this.board[i][j] != 0) {
                    wrong += distanceFromGoal(i, j, this.board[i][j]);
                }
            }
        }
        return wrong;
    }

    private int distanceFromGoal(int i, int j, int tile) {
        int x = (tile - 1) / this.size;
        int y = (tile - 1) % this.size;
        return Math.abs(i-x) + Math.abs(j-y);
    }

    public boolean isGoal() {
        return hamming() == 0;
    }

    public Board twin() {
        Board board = new Board(this.board);
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size - 1; j++) {
                if (this.board[i][j] != 0 && this.board[i][j + 1] != 0) {
                    board.swap(i, j, i, j + 1);
                    return board;
                }
            }
        }
        return board;
    }

    public boolean equals(Object y) {
        if (y == this) return true;
        if (y == null) return false;
        if (this.getClass() != y.getClass()) return false;
        return this.toString().equals(y.toString());
    }

    public Iterable<Board> neighbors() {
        int x = 0;
        int y = 0;
        boolean foundBlank = false;
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size; j++) {
                if (this.board[i][j] == 0) {
                    x = i;
                    y = j;
                    foundBlank = true;
                    break;
                }
            }
            if (foundBlank) {
                break;
            }
        }

        Stack<Board> boards =  new Stack<Board>();
        Board board;

        board = new Board(this.board);
        if (board.swap(x, y, x - 1, y)) boards.push(board);

        board = new Board(this.board);
        if (board.swap(x, y, x + 1, y)) boards.push(board);

        board = new Board(this.board);
        if (board.swap(x, y, x, y - 1)) boards.push(board);

        board = new Board(this.board);
        if (board.swap(x, y, x, y + 1)) boards.push(board);

        return boards;
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append(this.size + "\n");
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size; j++) {
                s.append(String.format("%2d ", this.board[i][j]));
            }
            s.append("\n");
        }
        return s.toString();
    }
}
