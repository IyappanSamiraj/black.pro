#include<stdio.h>
unsigned reduce(unsigned num, unsigned k) 
  {
  if (k <= 0) {
    return num;  
  }
  if (num == 0) {
    return 10;  
  }
  unsigned path1 = reduce(num/10, k)*10 + num%10;
  unsigned path2 = reduce(num/10, k-1);
  return path1 < path2 ? path1 : path2;
  }
int main() 
{
long long n;
int num;
scanf("%lld %d",&n,&num);
if(num==0)
  {
   printf("%lld",n);
  }
else
  {
   printf("%lld", reduce(n,num));
  }
}
