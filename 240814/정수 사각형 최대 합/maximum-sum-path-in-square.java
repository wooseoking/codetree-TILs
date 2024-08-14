import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();

        int[][] a = new int[n + 1][n + 1];
        int[][] dp = new int[n+ 1][n + 1];
        for(int i = 1 ;i<n + 1 ;i++){
            for(int j = 1;j<n + 1;j++){
                a[i][j] = sc.nextInt();
            }
        }
        dp[1][1] = a[1][1];

        for(int i = 1;i<n + 1;i++){
            for(int j = 1;j<n + 1;j++){
                dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]) + a[i][j];
            }
        }
        System.out.print(dp[n][n]);
    }
}