import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Day3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = new String[140];
        for (int i = 0; i < 140; i++) {
            String str = br.readLine() + ".";
            strs[i] = str;
        }
        System.out.println(sumParts(strs));
        System.out.println(sumGearRatio(strs));
    }

    private static int sumParts(String[] strs) {
        int sum = 0;
        int startCol, endCol;
        for (int i = 0; i < strs.length; i++) {
            startCol = -1;
            for (int j = 0; j < strs[0].length(); j++) {
                if (strs[i].substring(j, j + 1).matches("[0-9]")) {
                    if (startCol == -1) {
                        startCol = j;
                    }
                } else {
                    if (startCol != -1) {
                        int num = Integer.parseInt(strs[i].substring(startCol, j));
                        endCol = j;
                        boolean flag = false;
                        for (int r = i - 1; r <= i + 1; r++) {
                            for (int c = startCol - 1; c <= endCol; c++) {
                                if (r < 0 || r >= strs.length || c < 0 || c >= strs[r].length()) {
                                    continue;
                                }
                                char ch = strs[r].charAt(c);
                                if (!((ch >= '0' && ch <= '9') || ch == '.')) {
                                    flag = true;
                                    break;
                                }
                            }
                        }
                        if (flag) {
                            sum += num;
                            System.out.println(num);
                        }
                    }
                    startCol = -1;
                }
            }
        }
        return sum;
    }

    private static int sumGearRatio(String[] strs) {
        int sum = 0;
        int startCol, endCol;
        HashMap<List<Integer>, Set<Integer>> map;
        map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            startCol = -1;
            for (int j = 0; j < strs[0].length(); j++) {
                if (strs[i].substring(j, j + 1).matches("[0-9]")) {
                    if (startCol == -1) {
                        startCol = j;
                    }
                } else {
                    if (startCol != -1) {
                        int num = Integer.parseInt(strs[i].substring(startCol, j));
                        endCol = j;
                        for (int r = i - 1; r <= i + 1; r++) {
                            for (int c = startCol - 1; c <= endCol; c++) {
                                if (r < 0 || r >= strs.length || c < 0 || c >= strs[r].length()) {
                                    continue;
                                }
                                char ch = strs[r].charAt(c);
                                if (ch == '*') {
                                    List<Integer> coord = new ArrayList<>();
                                    coord.add(r);
                                    coord.add(c);
                                    Set<Integer> set = map.getOrDefault(coord, new HashSet<>());
                                    set.add(num);
                                    map.put(coord, set);
                                }
                            }
                        }
                    }
                    startCol = -1;
                }
            }
        }
        System.out.println(map);
        for (List<Integer> key : map.keySet()) {
            if (map.get(key).size() == 2) {
                int prod = 1;
                for (int factor : map.get(key)) {
                    prod *= factor;
                }
                sum += prod;
            }
        }
        return sum;
    }
}
