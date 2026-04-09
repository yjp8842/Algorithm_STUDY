class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int num = 0;
        int type = 0; // 등차 = 0 / 등비 = 1
        
        int first = common[0];
        int second = common[1];
        int third = common[2];
        
        if (second - first == third - second) {
            answer = common[common.length - 1] + (second - first);
        } else {
            answer = common[common.length - 1] * (second / first);
        }
        
        return answer;
    }
}