import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Day4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        String[] strs = new String[189];
        for (int i = 0; i < 189; i++) {
            String str = br.readLine();
            sum += getPoints(str);
            strs[i] = str;
        }
        System.out.println("Part 1: " + sum);
        System.out.println("Part 2: " + getNumCards(strs));
    }

    private static int getMatches(String str) {
        str = str.substring(str.indexOf(":") + 1);
        List<List<Integer>> numbers = Util.getNumbers(str);
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < 10; i++) {
            set.add(numbers.get(i).get(0));
        }
        int match = 0;
        for (int i = 10; i < numbers.size(); i++) {
            if (set.contains(numbers.get(i).get(0))) {
                match++;
            }
        }
        return match;
    }

    private static int getPoints(String str) {
        int match = getMatches(str);
        return match == 0 ? 0 : (int)(Math.pow(2, match - 1));
    }

    private static int getNumCards(String[] strs) {
        int n = strs.length;
        int[] total = new int[n];
        for (int i = 0; i < n; i++) {
            total[i] = 1;
        }
        for (int i = 0; i < n; i++) {
            int matches = getMatches(strs[i]);
            for (int j = 1; j <= matches; j++) {
                if (i + j >= n) {
                    continue;
                }
                total[i + j] += total[i];
            }
        }

        int sum = 0;
        for (int num : total) {
            sum += num;
        }
        return sum;
    }
}
