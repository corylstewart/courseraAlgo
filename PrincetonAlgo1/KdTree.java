import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by cory1 on 7/24/2015.
 */
public class KdTree {
    private int size;
    private Node root;
    private ArrayList<Point2D> pointsWithin;

    private class Node {
        private Point2D p;
        private Node leftChild;
        private Node rightChild;
        private int orientation;

        public Node(Point2D p, int orientation) {
            this.p = p;
            this.leftChild = null;
            this.rightChild = null;
            this.orientation = orientation;
        }



        private boolean hasLeftChild() {
            return this.leftChild != null;
        }

        private boolean hasRightChild() {
            return this.rightChild != null;
        }

        public String toString() {
            StringBuilder s = new StringBuilder();
            s.append(this.p.x());
            s.append(" ");
            s.append(this.p.y());
            s.append(" ");
            s.append(this.orientation);
            return s.toString();
        }
    }

    public KdTree() {
        this.size = 0;
        this.root = null;
    }

    public boolean isEmpty() {
        return this.size() == 0;
    }

    public int size() {
        return this.size;
    }

    public void insert(Point2D p) {
        if (this.root == null) {
            this.root = new Node(p, 0);
            this.size++;
        } else {
            put(this.root, p, this.root.orientation);
        }
    }

    private Node put(Node currentNode, Point2D p, int orientation) {
        if (currentNode == null) {
            currentNode = new Node(p, (orientation)%2);
            this.size++;
        } else if (!currentNode.p.equals(p)) {
            int cmp = this.compare(currentNode, p);
            if (cmp <= 0) {
                //StdOut.println("left");
                currentNode.leftChild = put(currentNode.leftChild, p, orientation + 1);
            } else {
                //StdOut.println("right");
                currentNode.rightChild = put(currentNode.rightChild, p, orientation + 1);
            }
        }

        return currentNode;
    }

    private Node get(Point2D p) {
        if (this.root == null) {
            return null;
        }
        return getNode(this.root, p);
    }

    private Node getNode(Node currentNode, Point2D p) {
        if (currentNode == null) {
            return null;
        }
        if (currentNode.p.equals(p)) {
            return currentNode;
        }
        int cmp = this.compare(currentNode, p);
        if (cmp <= 0) {
            return getNode(currentNode.leftChild, p);
        } else {
            return getNode(currentNode.rightChild, p);
        }
    }

    private int compare(Node currentNode, Point2D p) {
        if (currentNode.orientation == 0) {
            return Double.compare(p.x(), currentNode.p.x());
        } else {
            return Double.compare(p.y(), currentNode.p.y());
        }
    }

    public boolean contains(Point2D p) {
        return get(p) != null;
    }


    public void draw() {
        if (this.root != null) drawNode(this.root);
    }

    private void drawNode(Node node) {
        if (node != null) {
            node.p.draw();
            drawNode(node.leftChild);
            drawNode(node.rightChild);
        }
    }

    private double oneDDistance(Node node, Point2D p) {
        if (node.orientation == 0) {
            return Math.abs(node.p.x() - p.x());
        } else {
            return Math.abs(node.p.y() - p.y());
        }
    }

    public Iterable<Point2D> range(RectHV rect) {
        if (this.isEmpty()) return null;
        pointsWithin = new ArrayList<Point2D>();
        withinRect(rect, this.root);
        ArrayList<Point2D> newPointsWithin = pointsWithin;
        pointsWithin = null;

        return newPointsWithin;
    }

    private ArrayList<Point2D> withinRect(RectHV rectHV, Node currentNode) {
        if (currentNode == null) {
            return this.pointsWithin;
        }
        if (rectHV.contains(currentNode.p)) {
            this.pointsWithin.add(currentNode.p);
        }
        double x = currentNode.p.x();
        double y = currentNode.p.y();
        if (currentNode.orientation == 0) { //compare x axis
            if (x > rectHV.xmax()) {
                withinRect(rectHV,currentNode.leftChild);
            } else if (x < rectHV.xmin()) {
                withinRect(rectHV, currentNode.rightChild);
            } else {
                withinRect(rectHV, currentNode.leftChild);
                withinRect(rectHV,currentNode.rightChild);
            }
        } else { //compare y axis
            if (y > rectHV.ymax()) {
                withinRect(rectHV, currentNode.leftChild);
            } else if (y < rectHV.ymin()) {
                withinRect(rectHV, currentNode.rightChild);
            } else {
                withinRect(rectHV, currentNode.leftChild);
                withinRect(rectHV, currentNode.rightChild);
            }
        }
        return pointsWithin;
    }

    public Point2D nearest(Point2D p) {
        if (this.root == null) return null;
        return getNearest(this.root, p, this.root, this.root.p.distanceTo(p)).p;
    }

    private Node getNearest(Node currentNode, Point2D p, Node currBest, double currDist) {
        if (currentNode == null) {
            return currBest;
        }
        if (currentNode.p.equals(p)) {
            //thisDist = Double.POSITIVE_INFINITY;
            return currentNode;
        }
        double thisDist = currentNode.p.distanceTo(p);
        if (thisDist < currDist) {
            currBest = currentNode;
            currDist = thisDist;
        }
        int cmp = p.compareTo(currentNode.p);
        if (cmp <= 0) {
            if (currentNode.hasLeftChild()) {
                currBest = getNearest(currentNode.leftChild, p, currBest, currDist);
                currDist = currBest.p.distanceTo(p);
            }
            if (currentNode.hasRightChild() &&
                    currDist >= oneDDistance(currentNode, p)) {
                currBest = getNearest(currentNode.rightChild, p, currBest, currDist);
            }
        } else {
            if (currentNode.hasRightChild()) {
                currBest = getNearest(currentNode.rightChild, p, currBest, currDist);
                currDist = currBest.p.distanceTo(p);
            }
            if (currentNode.hasLeftChild() &&
                    currDist >= oneDDistance(currentNode, p)) {
                currBest = getNearest(currentNode.leftChild, p, currBest, currDist);
            }
        }
        return currBest;
    }

    public static void main(String[] args) {
        KdTree kd = new KdTree();
        double x, y;
        In in = new In(args[0]);
        double[] thesePoints = in.readAllDoubles();
        double[][] newPoints = new double[thesePoints.length/2][2];
        for (int i = 0; i < thesePoints.length; i+=2) {
            newPoints[i/2][0] = thesePoints[i];
            newPoints[i/2][1] = thesePoints[i + 1];
        }
        StdRandom.shuffle(newPoints);
        for (int i = 0; i < newPoints.length; i++) {
            Point2D p = new Point2D(newPoints[i][0], newPoints[i][1]);
            kd.insert(p);
        }

        StdDraw.clear();
        kd.draw();

        RectHV rect = new RectHV(0,0,.5,.5);
        while (true) {
            if (StdDraw.mousePressed()) {
                x = StdDraw.mouseX();
                y = StdDraw.mouseY();
                Point2D p = new Point2D(x, y);
                if (!kd.contains(p)) {
                    StdOut.println("New Node");
                    StdOut.printf("%8.6f %8.6f\n", x, y);
                    Point2D z= kd.nearest(p);
                    if (z != null) {
                        StdOut.println("nearest");
                        StdOut.printf("%8.6f %8.6f\n", z.x(), z.y());
                    } else {
                        StdOut.println("nope");
                    }
                    kd.insert(p);
                    StdDraw.clear();
                    kd.draw();
                    StdOut.println(kd.contains(p));
                    StdOut.println(kd.get(p).toString());
                    StdOut.println(kd.range(rect));
                    StdOut.println("size");
                    StdOut.println(kd.size());
                    StdOut.println("");
                }

            }
            StdDraw.show(50);
        }
    }
}


