function solution(date1, date2) {
  let newDate1 = date1[0]*100000 + date1[1]*100 + date1[2];
  let newDate2 = date2[0]*100000 + date2[1]*100 + date2[2];
  if( newDate1 < newDate2){
      return 1
  }
  return 0
}