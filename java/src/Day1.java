import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Day1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum1 = 0;
        int sum2 = 0;
        for (int i = 0; i < 1000; i++) {
            String s = br.readLine();
            sum1 += extract(s);
            sum2 += extract2(s);
        }
        System.out.println(sum1);
        System.out.println(sum2);
    }

    private static int extract(String s) {
        int first = -1;
        int last = -1;
        for (int i = 0; i < s.length(); i++) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                first = s.charAt(i) - '0';
                break;
            }
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                last = s.charAt(i) - '0';
                break;
            }
        }
        return first * 10 + last;
    }

    private static int extract2(String s) {
        Map<String, Integer> dict = new HashMap<>();
        dict.put("one", 1);
        dict.put("two", 2);
        dict.put("three", 3);
        dict.put("four", 4);
        dict.put("five", 5);
        dict.put("six", 6);
        dict.put("seven", 7);
        dict.put("eight", 8);
        dict.put("nine", 9);
        int firstIdx = Integer.MAX_VALUE;
        int firstVal = -1;
        int lastIdx = -1;
        int lastVal = -1;
        for (String key : dict.keySet()) {
            int idx = s.indexOf(key);
            if (idx >= 0) {
                if (idx < firstIdx) {
                    firstIdx = idx;
                    firstVal = dict.get(key);
                }
                if (s.lastIndexOf(key) > lastIdx) {
                    lastIdx = s.lastIndexOf(key);
                    lastVal = dict.get(key);
                }
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9' && i < firstIdx) {
                firstVal = s.charAt(i) - '0';
                break;
            }
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9' && i > lastIdx) {
                lastVal = s.charAt(i) - '0';
                break;
            }
        }
        return firstVal * 10 + lastVal;
    }
}
