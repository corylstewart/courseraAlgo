/**
 * Created by cory1 on 7/14/2015.
 */
import java.lang.NullPointerException;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Iterator;
import java.util.Random;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] queue;
    private int itemCount;
    private Random rand = new Random();

    public RandomizedQueue() {
        queue = (Item[])new Object[1];
        itemCount = 0;
    }

    public boolean isEmpty() { return itemCount == 0; }

    public int size() { return itemCount; }

    private boolean isFull() {return itemCount == queue.length; }

    private boolean isQuarterFull() {return itemCount < queue.length/4; }

    public void enqueue(Item item) {
        if (item == null) { throw new NullPointerException(); }
        //System.out.println(isFull());
        //System.out.println(isQuarterFull());
        if (isFull()) {
            resizeArray(queue.length*2);
        } else if (isQuarterFull()) {
            resizeArray(queue.length/2);
        }
        queue[itemCount] = item;
        itemCount++;
    }

    public Item dequeue() {
        if(isEmpty()){ throw new NoSuchElementException(); }
        int rI = nextRandomInt();
        Item payload = queue[rI];
        shiftArray(rI);
        itemCount--;
        return payload;
    }

    private void resizeArray(int newSize) {
        Item[] newQueue = (Item[])new Object[newSize];
        for (int i = 0; i < itemCount; i++) {
            newQueue[i] = queue[i];
        }
        queue = newQueue;
    }

    private void shiftArray(int startIndex) {
        for (int i = startIndex; i < itemCount - 1; i++) {
            queue[i] = queue[i+1];
        }
        if (queue.length == itemCount) {
            queue[itemCount-1] = null;
        } else {
            queue[itemCount-1] = queue[itemCount];
        }
    }

    public Item sample(){
        if(isEmpty()){
            throw new NoSuchElementException("Queue is empty");
        }
        return queue[nextRandomInt()];
    }

    public Iterator<Item> iterator(){
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        int n;
        int[] shuffledIndex;

        public RandomizedQueueIterator(){
            n = 0;
            shuffledIndex = makeShuffledIndex();
        }

        public boolean hasNext()  {
            return n < itemCount;

        }
        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            return queue[shuffledIndex[n++]];
        }
    }

    private void printQueue() {
        System.out.println(Arrays.toString(queue));
    }

    private int nextRandomInt() {
        return rand.nextInt(itemCount);
    }

    private int randomSwap(int min, int max) {
        return rand.nextInt((max - min)) + min;
    }

    private int[] makeShuffledIndex() {
        int swap;
        int oldValue;
        int[] myShuffle = new int[itemCount];
        for (int i = 0; i < itemCount; i++) {
            myShuffle[i] = i;
        }
        for (int i = 0; i < itemCount - 1; i++) {
            oldValue = myShuffle[i];
            swap = randomSwap(i, myShuffle.length);
            myShuffle[i] = myShuffle[swap];
            myShuffle[swap] = oldValue;
        }
        return myShuffle;
    }

    public static void main(String[] args) {
        RandomizedQueue q = new RandomizedQueue();
        Iterator iterator = q.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        q.sample();


    }

}

