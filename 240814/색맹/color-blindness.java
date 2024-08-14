import java.util.*;

public class Main {
    static boolean[][] v;
    static int n;
    static char[][] a;
    static char[][] b;
    static int ans1 = 0;
    static int ans2 = 0;
    static int[] dy = {-1,0,1,0};
    static int[] dx = {0,1,0,-1};

    public static boolean inside(int y,int x){
        return 0<=y && y<n && 0<= x && x <n;
    }

    public static void dfs(int y,int x,char c,char[][] map){
        v[y][x] = true;
        
        for(int k = 0 ;k<4;k++){
            int ny = y + dy[k];
            int nx = x + dx[k];
            if(!inside(ny,nx))continue;
            if(v[ny][nx])continue;
            if(map[y][x] != map[ny][nx])continue;
            dfs(ny,nx,c,map);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new char[n][n];
        b = new char[n][n];
        v = new boolean[n][n];

        for(int i = 0 ;i<n;i++){
            String str = sc.next();
            for(int j = 0;j<n;j++){
                a[i][j] = str.charAt(j);
                b[i][j] = a[i][j];
                if(b[i][j] == 'G'){
                    b[i][j] = 'R';
                }
            }
        }

        for(int i = 0 ;i<n;i++){
            for(int j = 0;j<n;j++){
                if(!v[i][j]){
                    ans1++;
                    dfs(i,j,a[i][j],a);
                }
            }
        }

        v = new boolean[n][n];
        for(int i = 0 ;i<n;i++){
            for(int j = 0;j<n;j++){
                if(!v[i][j]){
                    ans2++;
                    dfs(i,j,a[i][j],b);
                }
            }
        }

        System.out.print(ans1 + " " + ans2);
    }
}