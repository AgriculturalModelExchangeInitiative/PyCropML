
int temp, b=1; 
result=0;  
for(int i=0;i<n;i++)  
{    
    temp = result;   
    result=b;    
    b=temp+b;    
}
 