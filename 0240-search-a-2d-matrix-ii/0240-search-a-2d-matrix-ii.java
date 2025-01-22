/**

솔직히 그냥 늘여놓고 정렬하고 for문하나로만 찾아도 시간상 되긴 하는데,
문제 의도는 그냥 2차원 매트릭스 자체를 이용하라는 거겠지?

그냥 dfs나 bfs로 완전탐색 시키면 될 듯?
체크리스트 갖게 하고,

아래, 오른쪽 방향으로만 이동하게 하면 될 듯? target값보다 다음 값이 작으면 이동시키면 끝.
그냥 bfs로 하는게 제일 깔끔할 듯?

### 수도코드만들기
chklist로 matrix랑 동일한 크기로 만들어 두기
def bfs(target)
    q는 큐로 (0,0) 넣어두기
    while(q)
        curY,curX = q에서 popleft
        if 매트릭스[curY][curX]가 target이면 return true

        # 오른쪽
        if curX+1<len(matrix[0])라면 (내부이기만 하면) and chklist에 False라면 and matrix[curY][curX+1]<=target
            q.append((curY,curX+1))
            
        # 아래쪽 (오른쪽 아래쪽 둘다 넣을 수 있으니)
        if curY+1<len(matrix) and chklist에서 False라면 and matrix[curY+1][curX]<=target
            q.append((curY+1,curX))
        
    return False  (마지막까지 돌렸는데 못찾았다는거니.)


answer = bfs(target)
return answer

__ 알고 대충 10분
__ 수도 대충 17분
__ 엣지 대충.. 없어보임. 너무 간단함. 19분

 */

import java.util.*;
import java.io.*;

class Solution {
    static boolean[][] chklist;
    class Tuple{
        public int y;
        public int x;
        Tuple(int y, int x){
            this.y = y;
            this.x = x;
        }
    }
    public boolean bfs(int target,int[][] matrix){
        Queue<Tuple> q = new LinkedList<>();
        Tuple init = new Tuple(0,0);
        q.add(init);

        while(q.size()>0){
            Tuple curPos = q.poll();
            // // test
            // BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            // try{
                
            
            // String tmp = "curPos: "+Integer.toString(curPos.x)+ Integer.toString(curPos.y);
            // bw.write(tmp);
            // bw.newLine();
            // bw.flush();
            // }catch(IOException e){
            //     continue;
            // }
            

            if (matrix[curPos.y][curPos.x]==target) return true;

            if (curPos.x+1<matrix[0].length && matrix[curPos.y][curPos.x+1]<=target && !chklist[curPos.y][curPos.x+1]){
                chklist[curPos.y][curPos.x+1] = true;
                q.add(new Tuple(curPos.y, curPos.x+1));
            }

            if (curPos.y+1<matrix.length && matrix[curPos.y+1][curPos.x]<=target && !chklist[curPos.y+1][curPos.x]){
                chklist[curPos.y+1][curPos.x] = true;
                q.add(new Tuple(curPos.y+1, curPos.x));
            }
        }
        return false;
    }
    public boolean searchMatrix(int[][] matrix, int target) {
        chklist = new boolean[matrix.length][matrix[0].length]; // 초기화가 되네.
        boolean answer = bfs(target, matrix);
        return answer;
    }
}