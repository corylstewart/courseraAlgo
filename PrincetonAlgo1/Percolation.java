import java.util.Arrays;

/**
 * Created by cory1 on 6/24/2015.
 */

//import java.util.Arrays;
import java.util.Random;


public class Percolation {
    private int N, totalSize, lastNode;
    private int[] parent;
    private int[][] nodes;


    public Percolation(int nMatrix) {
        N = nMatrix;
        if (N <= 0) {
            throw new IllegalArgumentException();
        }
        makeParents();
        initArray();
        //printGrid();
        //System.out.println(totalSize);
        //System.out.println(Arrays.toString(parent));
        //System.out.println(Arrays.toString(nodeOrder));
    }

    //stuff they need
    public boolean isFull(int i, int j) {
        if (nodes[i-1][j-1] == 0) {
            return false;
        } else {
            int node = fromMatrixToArray(i - 1, j - 1);
            return connected(0, node);
        }
    }

    public boolean isOpen(int i, int j) {
        return nodes[i-1][j-1] == 1;
    }

    public boolean percolates() {
        return connected(0, lastNode);
    }

    public void open(int i, int j) {
        insertNode(i - 1, j - 1);
    }



    //my stuff
    private void initArray() {
        nodes = new int[N][N];
        for (int i = 0; i < N; i++) {
            makeUnion(0, i + 1);
            makeUnion(lastNode, lastNode - 1 - i);
        }

    }

    private void insertNode(int i, int j) {
        nodes[i][j] = 1;
        int[][] neighbors = matrixNeighbors(i, j);
        for (int k = 0; k < neighbors.length; k++) {
            int x = neighbors[k][0];
            int y = neighbors[k][1];
            int arrayOne = fromMatrixToArray(i, j);
            int arrayTwo = fromMatrixToArray(x, y);

            if (openNode(x, y) && !connected(arrayOne, arrayTwo)) {
                makeUnion(arrayOne, arrayTwo);
            }
        }
    }


    private void printGrid() {
        for (int i = 0; i < nodes.length; i++) {
            System.out.println(Arrays.toString(nodes[i]));
        }
    }

    private int[][] matrixNeighbors(int i, int j) {
        int[][] neighbors;
        if (i == 0) { //handle if row is first row
            if (j == 0) {
                neighbors = new int[][] {{i, j + 1}, {i + 1, j}};
                return neighbors;
            } else if (j == nodes[0].length - 1) {
                neighbors = new int[][] {{i, j - 1},
                                        {i + 1, j}};
                return neighbors;
            } else {
                neighbors = new int[][] {{i, j - 1},
                                        {i, j + 1},
                                        {i + 1, j}};
                return neighbors;
            }

        } else if (i == nodes.length - 1) { //handle if row is last row
            if (j == 0) {
                neighbors = new int[][] {{i, j + 1}, {i - 1, j}};
            } else if (j == nodes[0].length - 1) {
                neighbors = new int[][] {{i, j - 1},
                                        {i - 1, j}};
            } else {
                neighbors = new int[][] {{i, j - 1},
                                        {i, j + 1},
                                        {i - 1, j}};
            }
        } else if (j == 0) { //handle if column is first
            neighbors = new int[][] {{i, j + 1},
                                    {i - 1, j},
                                    {i + 1, j}};

        } else if (j == nodes[i].length - 1) {
            neighbors = new int[][] {{i, j - 1},
                                    {i - 1, j},
                                    {i + 1, j}};
        } else {
            neighbors = new int[][] {{i, j - 1},
                                    {i, j + 1},
                                    {i - 1, j},
                                    {i + 1, j}};
        }
        return neighbors;
    }

    private int[] fromArrayToMatrix(int node) {
        int i = (node - 1) / N;
        int j = (node - 1) % N;
        int[] coordinate = new int[] {i, j};
        return coordinate;
    }

    private int fromMatrixToArray(int i , int j) {
        int node = (i * N) + j + 1;
        return node;
    }

    private int[][] arrayNeighbors(int node) {
        int[] coordinates = fromArrayToMatrix(node);
        int i = coordinates[0];
        int j = coordinates[1];
        int[][] mNeighbors = matrixNeighbors(i, j);

        return mNeighbors;

    }

    private boolean openNode(int i, int j) {
        return nodes[i][j] == 1;
    }


    //code for union find
    private void makeParents() {
        totalSize = (N * N) + 2;
        lastNode = totalSize - 1;
        parent = new int[totalSize];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }
    }



    private int find(int p) {
        while (p != parent[p]) {
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }

    private boolean connected(int p, int q) {
        if (N == 1) {
            return nodes[0][0] == 1;
        }
        return find(p) == find(q);
    }

    private void makeUnion(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;
        parent[rootQ] = rootP;
    }


    private int randInt(int min, int max) {
        Random rand = new Random();
        int randomNum = rand.nextInt((max-min) + 1) + min;
        return randomNum;
    }
}