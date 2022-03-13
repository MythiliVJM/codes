#include <stdio.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n,i,j,sum=0,p=1;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        sum+=a[i];
        p=p*a[i];
    }
    if(sum%2 == 0){
        printf("%d",sum);
    }
    else
        printf("%d",p);
    return 0;
}