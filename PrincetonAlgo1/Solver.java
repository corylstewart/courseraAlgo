import java.util.ArrayList;

/**
 * Created by cory1 on 7/22/2015.
 */
public class Solver {
    private boolean solvable;
    private int moves;
    private BoardState solution;
    private ArrayList<Board> boards = new ArrayList<Board>();

    public Solver(Board initial) {
        Board original = initial;
        if (original.isGoal()) {
            this.solution = new BoardState(original, 0, null);
            this.moves = 0;
            this.solvable = true;
            convertSolution();
            return;
        }

        Board twin = initial.twin();
        MinPQ<BoardState> originalPQ = new MinPQ<BoardState>();
        MinPQ<BoardState> twinPQ = new MinPQ<BoardState>();
        BoardState originalBS = new BoardState(original, 0, null);
        BoardState twinBS = new BoardState(twin, 0, null);
        originalPQ.insert(originalBS);
        twinPQ.insert(twinBS);
        boolean solved = false;
        BoardState originalNU;
        BoardState twinNU;
        while (!solved) {
            originalNU = originalPQ.delMin();
            twinNU = twinPQ.delMin();
            original = originalNU.board;
            twin = twinNU.board;
            if (original.isGoal()) {
                solvable = true;
                this.solution = originalNU;
                this.moves = originalNU.moves;
                convertSolution();
                return;
            }
            if (twin.isGoal()) {
                //System.out.println("No solution possible");
                solvable = false;
                return;
            }
            originalNU.moves += 1;
            Iterable<Board> originalNeighbors = original.neighbors();
            for (Board neighbor : originalNeighbors) {
                if (originalNU.previousBoard != null && neighbor.equals(originalNU.previousBoard.board)) {
                    continue;
                }
                BoardState newBS = new BoardState(neighbor, originalNU.moves, originalNU);
                originalPQ.insert(newBS);
            }

            twinNU.moves += 1;
            Iterable<Board> twinNeighbors = twin.neighbors();
            for (Board neighbor : twinNeighbors) {
                if (twinNU.previousBoard != null && neighbor.equals(twinNU.previousBoard.board)) {
                    continue;
                }
                BoardState newBS = new BoardState(neighbor, twinNU.moves, twinNU);
                twinPQ.insert(newBS);
            }
        }
    }

    private void convertSolution() {
        System.out.println(this.moves);
        if (!solvable) {
            return;
        }
        BoardState current = this.solution;
        int totalMoves = this.moves;
        for (int i = 0; i <= totalMoves; i++) {
            boards.add(current.board);
        }
        for (int i = totalMoves; i >= 0; i--) {
            boards.set(i, current.board);
            if (current.previousBoard != null) {
                current = current.previousBoard;
            }
        }
    }

    private class BoardState implements Comparable<BoardState> {
        private Board board;
        private int moves;
        private BoardState previousBoard;
        private int cachedPriority = -1;

        public BoardState(Board board, int moves, BoardState previousBoard) {
            this.board = board;
            this.moves = moves;
            this.previousBoard = previousBoard;
        }

        private int getCachedPriority() {
            if (this.cachedPriority == -1) {
                this.cachedPriority = this.moves + board.manhattan();
            }
            return this.cachedPriority;
        }

        @Override
        public int compareTo(BoardState that) {
            if (this.getCachedPriority() < that.getCachedPriority()) {
                return -1;
            }
            if (this.getCachedPriority() > that.getCachedPriority()) {
                return 1;
            }
            return 0;
        }
    }


    public boolean isSolvable() { return this.solvable;}

    public int moves() {
        if (this.solvable) {
            return boards.size() - 1;
        } else {
            return -1;
        }
    }

    public Iterable<Board> solution() {
        if (solvable) {
            return boards;
        } else {
            return null;
        }
    }

    public static void main(String[] args) {

        // create initial board from file
        In in = new In(args[0]);
        int N = in.readInt();
        int[][] blocks = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}
