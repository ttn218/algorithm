function solution(chicken) {
  var answer = 0;
  var cuppon = chicken;
  while(cuppon>=10){
      answer += Math.floor(cuppon/10);
      cuppon = Math.floor(cuppon/10) + cuppon%10;
  }
  return answer;
}