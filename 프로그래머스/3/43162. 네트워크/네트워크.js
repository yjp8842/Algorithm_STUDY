function solution(n, computers) {
    var answer = 0;
    var visited = Array(n).fill(0);
    
    function bfs(a, computers, visited) {
        var queue = [a];
        visited[a] = 1;

        while (queue.length > 0) {
            x = queue.pop();
            
            for (let i=0; i < n; i++) {
                if (visited[i] == 0 && computers[x][i] == 1) {
                    queue.push(i);
                    visited[i] = 1;
                }
            }
        }
    }
    
    for (let i=0; i < n; i++) {
        if (visited[i] == 0) {
            bfs(i, computers, visited);
            answer += 1;   
        }
    }
    
    return answer;
}