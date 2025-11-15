function getKNum(n, k, nums) {
    // 나머지를 push
    nums.push(n % k);

    // 몫이 0이면 종료
    if (Math.floor(n / k) === 0) {
        return nums;
    } else {
        return getKNum(Math.floor(n / k), k, nums);
    }
}

function isPrime(n) {
    if (n < 2) return false;

    let i = 2;
    while (i * i <= n) {
        if (n % i === 0) return false;
        i++;
    }
    return true;
}

function solution(n, k) {
    var answer = 0;
    var lists = [];
    var primes = [];
    
    getKNum(n, k, lists);
    
    var sortLists = lists.reverse().join('').split(0);
    
    for (let i=0; i < sortLists.length; i++) {
        if (isPrime(sortLists[i]) == true) {
            answer += 1;
        }
    }
    
    return answer;
}