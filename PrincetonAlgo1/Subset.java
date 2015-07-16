import java.util.*;

/**
 * Created by cory1 on 7/15/2015.
 */


public class Subset {

    public static void main(String[] args) {
        /*Scanner scanner = new Scanner(System.in);
        String a;
        int k;
        RandomizedQueue q = new RandomizedQueue();
        k = Integer.parseInt(args[0]);
        while (scanner.hasNext()) {
            a = scanner.next();
            q.enqueue(a);
        }
        q.printQueue();
        Iterator iterator = q.iterator();
        for (int i = 0; i < k; i++) {
            System.out.println(iterator.next());
        }*/
        int k = Integer.parseInt(args[0]);
        String a = StdIn.readLine();
        System.out.println(a);
        String[] s = a.split(" ");
        RandomizedQueue q = new RandomizedQueue();
        for (int i = 0; i < s.length; i ++) {
            q.enqueue(s[i]);
        }
        Iterator iterator = q.iterator();
        for (int i = 0; i < k; i++) {
            System.out.println(iterator.next());
        }

    }

}
