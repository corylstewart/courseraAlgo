import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.Set;

/**
 * Created by cory1 on 7/24/2015.
 */
public class PointSET {
    private SET<Point2D> points = new SET<Point2D>();

    public PointSET() {
    }

    public boolean isEmpty() {
        return this.points.isEmpty();
    }

    public int size() {
        return this.points.size();
    }

    public void insert(Point2D p) {
        if (p != null) this.points.add(p);
    }

    public boolean contains(Point2D p) {
        return points.contains(p);
    }

    public void draw() {
        for (Point2D p : this.points) {
            StdDraw.point(p.x(), p.y());
        }
    }

    public Iterable<Point2D> range(RectHV rect) {
        ArrayList<Point2D> pointsWithin = new ArrayList<Point2D>();
        for (Point2D p : this.points) {
            if (p.x() <= rect.xmax() && p.x() >= rect.xmin() &&
                    p.y() <= rect.ymax() && p.y() >= rect.ymin()) {
                pointsWithin.add(p);
            }
        }
        return pointsWithin;
    }

    public Point2D nearest(Point2D p) {
        if (this.size() == 0) return null;
        double minSoFar = Double.POSITIVE_INFINITY;
        Point2D pointSoFar = null;
        double dist;
        for (Point2D point : this.points) {
            if (point.equals(p)) {
                return point;
            }
            dist = point.distanceTo(p);
            if (dist < minSoFar) {
                minSoFar = dist;
                pointSoFar = point;
            }
        }
        return pointSoFar;
    }

    public static void main(String[] args) {
        PointSET pointSET = new PointSET();
        double x, y;
        In in = new In(args[0]);
        double[] thesePoints = in.readAllDoubles();
        for (int i = 0; i < thesePoints.length; i+=2) {
            x = thesePoints[i];
            y = thesePoints[i + 1];
            Point2D p = new Point2D(x, y);
            pointSET.insert(p);
        }
    }
}
