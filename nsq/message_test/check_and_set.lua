local money = tonumber(redis.call('get', KEYS[1]));
print(money);
if money <=0 then  
   return nil
else  
   money=money-tonumber(KEYS[2]);  
   if money<0 then  
     return nil 
   else  
     redis.call('set', KEYS[1],money);
     return money; 
   end 
end 
 return nil;  