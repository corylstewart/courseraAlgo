import java.util.Arrays;

/**
 * Created by cory1 on 7/18/2015.
 */
public class Brute {
    public void Brute() {

    }

    public static void main(String[] args) {
        int arraySize = 6;
        Point[] points = new Point[arraySize];
        points[0] = new Point(19000, 10000);
        points[1] = new Point(18000, 10000);
        points[2] = new Point(32000, 10000);
        points[3] = new Point(21000, 10000);
        points[4] = new Point(1234, 5678);
        points[5] = new Point(14000, 10000);
        Arrays.sort(points);
        System.out.println(Arrays.toString(points));
        System.out.println(points[0].SLOPE_ORDER.compare(points[1], points[2]));
    }
}
