/**
 * Created by cory1 on 6/29/2015.
 */
import java.util.Random;

public class PercolationStats {
    private double[] results;
    private int[] nodeOrder;
    private int myN;
    private double mean, std;

    public PercolationStats(int N, int T) {
        results = new double[T];
        myN = N;
        for (int i = 0; i < T; i++) {
            results[i] = startSim(N);
        }
        makeStats();
        String mean = "mean\t\t\t= " + Double.toString(mean());
        String std = "stddev\t\t\t= " + Double.toString(stddev());
        String conf = "95% confidence interval = " + Double.toString(confidenceLo())+ ", "
                        + Double.toString(confidenceHi());
        System.out.println(mean);
        System.out.println(std);
        System.out.println(conf);
    }

    private void makeStats() {
        double total = 0;
        for (int i = 0; i < results.length; i++) {
            total += results[i];
        }
        mean = total/results.length;
        total = 0;
        for (int i = 0; i < results.length; i++) {
            total += (results[i] - mean)*(results[i] - mean);
        }
        std = Math.sqrt(total/(results.length-1));
    }

    public double mean() {
        return mean;
    }

    public double stddev() {
        return std;
    }

    public double confidenceLo() {
        return mean() - (1.96 * stddev())/(Math.sqrt(results.length));
    }

    public double confidenceHi() {
        return mean() + (1.96 * stddev())/(Math.sqrt(results.length));
    }

    //my stuff
    private double startSim(int N) {
        nodeOrder = new int[N*N];
        for (int i = 0; i < nodeOrder.length; i++) {
            nodeOrder[i] = i + 1;
        }
        shuffleArray();
        Percolation p = new Percolation(myN);
        for (int i = 0; i < nodeOrder.length; i++) {
            int[] node = fromArrayToMatrix(nodeOrder[i]);
            p.open(node[0], node[1]);
            if (p.percolates()) {
                return (double) i/(myN*myN);
            }
        }

        return 0.0;
    }

    private void shuffleArray() {
        int max = nodeOrder.length - 1;
        for (int i = 0; i < nodeOrder.length - 1; i++) {
            int swap = randInt(i, max);
            if (i != swap) {
                int first = nodeOrder[i];
                int second = nodeOrder[swap];
                nodeOrder[i] = second;
                nodeOrder[swap] = first;
            }
        }
    }

    private int randInt(int min, int max) {
        Random rand = new Random();
        return rand.nextInt((max-min) + 1) + min;
    }

    private int[] fromArrayToMatrix(int node) {
        int i = (node - 1) / myN + 1;
        int j = (node - 1) % myN + 1;
        return new int[] {i, j};
    }

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int T = Integer.parseInt(args[1]);
        if (N <= 0) {
            throw new IllegalArgumentException();
        }
        if (T <= 0) {
            throw new IllegalArgumentException();
        }
        new PercolationStats(N, T);
    }
}
