#include <iostream>
using namespace std;

int right_most_setbit_pos(int n){
    if (n==0){
        return 0;
    }
    else{
        int isolated = 0;
        isolated = n & -n;
        int pos = 0;
        while ((isolated >>=1)>0){
            pos++;
        }
        return pos;
    }
}

int main(){

    int n=18;
    count<<"the right most set bit in "<<n<<"is at:"<<right_most_setbit_pos(n)<<endl;
    return 0;
}

// out:the right most set bit in 18is at:1
