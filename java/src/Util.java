import java.util.ArrayList;
import java.util.List;

/**
 * I implemented this class after Day 3 since extracting numbers and digits seem to be
 * useful functionalities for Advent of Code
 */
public class Util {

    public static void main(String[] args) {
        System.out.println(getNumbers("abc123abc"));
        System.out.println(getNumbers("ab0qqq987"));
        System.out.println(getNumbers("12345"));
    }

    /**
     * Returns a list of (number, startIdx, endIdx) tuple, ordered increasingly by startIdx.
     * endIdx is the idx right after the last digit of the number,
     * so s.substring(startIdx, endIdx) is the number.
     */
    public static List<List<Integer>> getNumbers(String s) {
        List<List<Integer>> numbers = new ArrayList<>();
        int start = -1;  // -1 denotes not currently in a number, >= 0 denotes currently in a number
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                if (start == -1) {
                    start = i;
                }
            } else {
                if (start != -1) {
                    int end = i;
                    int num = Integer.parseInt(s.substring(start, end));
                    List<Integer> lst = new ArrayList<>();
                    lst.add(num);
                    lst.add(start);
                    lst.add(end);
                    numbers.add(lst);
                }
                start = -1;
            }
        }
        if (start != -1) {
            int end = s.length();
            int num = Integer.parseInt(s.substring(start, end));
            List<Integer> lst = new ArrayList<>();
            lst.add(num);
            lst.add(start);
            lst.add(end);
            numbers.add(lst);
        }
        return numbers;
    }

    /**
     * Returns a list of (digit, idx) tuple, ordered increasingly by idx.
     */
    public static List<List<Integer>> getDigits(String s) {
        List<List<Integer>> digits = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                List<Integer> lst = new ArrayList<>();
                lst.add(s.charAt(i) - '0');
                lst.add(i);
                digits.add(lst);
            }
        }
        return digits;
    }
}
