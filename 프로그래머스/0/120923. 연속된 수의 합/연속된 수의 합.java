import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int num, int total) {
        // int[] answer = {};
        ArrayList<Integer> answer = new ArrayList<>();
        int middle = total / num;
        
        if (total % num != 0) {
            num--;
            for(int i=middle - (num/2); i<middle + (num/2) + 2; i++) {
                answer.add(i);
            }
        } else {
            num--;
            for(int i=middle - (num/2); i<middle + (num/2) + 1; i++) {
                answer.add(i);
            }
        }
        
        
        
        return answer;
    }
}