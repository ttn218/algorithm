function solution(babbling) {
  var answer = 0;

  for(babble of babbling){
      var bab = '';
      if(babble.includes('aya')){
          bab += 'aya'
      }
      if(babble.includes('ye')){
          bab += 'ye'
      }
      if(babble.includes('woo')){
          bab += 'woo'
      }
      if(babble.includes('ma')){
          bab += 'ma'
      }
      if(babble.length === bab.length){
          answer ++;
      }
  }    
  
  

  
  return answer;
}