import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Day2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum1 = 0;
        int sum2 = 0;
        for (int i = 1; i <= 100; i++) {
            String game = br.readLine();
            if (possible(game)) {
                sum1 += i;
            }
            sum2 += power(game);
        }
        System.out.println(sum1);
        System.out.println(sum2);
    }

    private static int getMax(String game, String color) {
        int max = 0;
        int idx = game.indexOf(color);
        while (idx != -1) {
            max = Math.max(max, Integer.parseInt(game.substring(idx - 3, idx).strip()));
            idx = game.indexOf(color, idx + 1);
        }
        return max;
    }

    private static boolean possible(String game) {
        int colon = game.indexOf(":");
        game = game.substring(colon + 1);
        return getMax(game, "red") <= 12
                && getMax(game, "green") <= 13
                && getMax(game, "blue") <= 14;
    }

    private static int power(String game) {
        int colon = game.indexOf(":");
        game = game.substring(colon + 1);
        return getMax(game, "red") * getMax(game, "green") * getMax(game, "blue");
    }
}
