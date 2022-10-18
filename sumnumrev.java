class Solution {
    public boolean sumOfNumberAndReverse(int num) {
        if(num == 0){
            return true;
            }
        int rem;
            int ans;
        for(int i=0;i<num;i++){
            int find; 
            find = num - i;
            ans = 0;
            while(find>0){
                rem = find % 10;
                ans = ans *10 + rem;
                find = find / 10;
                }
            if(ans == i){
                return true;
                }
        }
        return false;
            
   