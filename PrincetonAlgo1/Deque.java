import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by cory1 on 7/14/2015.
 */
public class Deque<Item> implements Iterable<Item> {

    private Node head;
    private Node tail;
    private int itemCount;

    public Deque() {
        head = null;
        tail = null;
        itemCount = 0;
    }

    public boolean isEmpty() { return itemCount == 0; }

    public int size() { return itemCount; }

    public void addFirst(Item item) {
        Node newNode = new Node();
        if (size() == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.setNext(head);
            head.setPrev(newNode);
            head = newNode;
        }
        newNode.setData(item);
        itemCount++;
    }

    public void addLast(Item item) {
        Node newNode = new Node();
        if (size() == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.setPrev(tail);
            tail.setNext(newNode);
            tail = newNode;
        }
        newNode.setData(item);
        itemCount++;
    }

    public Item removeFirst() {
        emptyError();
        Item item = head.getData();
        if (size() == 1) {
            head = null;
            tail = null;
        } else {
            head = head.getNext();
            head.setPrev(null);
        }
        itemCount--;
        return item;
    }

    public Item removeLast() {
        emptyError();
        Item item = tail.getData();
        if (size() == 1) {
            head = null;
            tail = null;
        } else {
            tail = tail.getPrev();
            tail.setNext(null);
        }
        itemCount--;
        return item;
    }

    private void emptyError() {
        if (size() == 0) {
            throw new NoSuchElementException();
        }
    }

    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    public static void main(String[] args) {
        Deque deque = new Deque();
        deque.addFirst(1);
        deque.addLast(2);
        deque.addFirst(3);
        deque.removeLast();
        Iterator iterator = deque.iterator();
        System.out.println(iterator.hasNext());
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        //System.out.println(deque.removeFirst());
        //System.out.println("hi");

    }

    private class Node {
        private Node next;
        private Node prev;
        private Item data;

        public Node() {
            next = null;
            prev = null;
            data = null;
        }

        public Item getData() { return data; }

        public void setData(Item payload) {
            checkNull(payload);
            data = payload;
        }

        public Node getNext() { return next; }

        public void setNext(Node _next) { next = _next; }

        public Node getPrev() { return prev; }

        public void setPrev(Node _prev) { prev = _prev; }

        private void checkNull(Item payload) {
            if (payload == null) { throw new NullPointerException(); }
        }
    }

    private class DequeIterator implements Iterator<Item>{
        private Node current = head;

        public boolean hasNext() { return current != null;}

        public void remove() { throw new UnsupportedOperationException(); }

        public Item next() {
            if (!hasNext()) { throw new NoSuchElementException(); }
            Item item = current.getData();
            current = current.getNext();
            return item;
        }
    }
}
