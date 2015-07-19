/**
 * Created by cory1 on 7/17/2015.
 */
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Point implements Comparable<Point> {

    // compare points by slope
    public final Comparator<Point> SLOPE_ORDER = new Comparator<Point>() {
        @Override
        public int compare(Point o1, Point o2) {
            return Double.compare(slopeTo(o1), slopeTo(o2));
        }
    };

    private final int x;                              // x coordinate
    private final int y;                              // y coordinate

    // create the point (x, y)
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
    }

    // plot this point to standard drawing
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    // draw line between this point and that point to standard drawing
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // slope between this point and that point
    public double slopeTo(Point that) {
        /* YOUR CODE HERE */
        if (this.compareTo(that) == 0) return Double.NEGATIVE_INFINITY;
        else if (this.x == that.x) return 0.0;
        else if (this.y == that.y) return Double.POSITIVE_INFINITY;
        else return ((double)that.y - this.y)/((double)that.x - this.x);
    }

    // is this point lexicographically smaller than that one?
    // comparing y-coordinates and breaking ties by x-coordinates
    public int compareTo(Point that) {
        /* YOUR CODE HERE */
        if (this.y < that.y) return -1;
        else if (this.y == that.y && this.x < that.x) return -1;
        else if (this.y == that.y && this.x == that.x) return 0;
        else return 1;
    }

    // return string representation of this point
    public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
    }

    // unit test
    public static void main(String[] args) {
        /* YOUR CODE HERE */
        Point[] a = {new Point(0,0), new Point(0,0), new Point(10,1), new Point(-1, -1)};
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));

    }
}
