#include <iostream>
using namespace std;
int main() {
    int n;
    int sum = 0;
    cout<<"Enter the number of terms you want to add: ";
    cin>>n;
    for(int i = 1;n<=i;i++){
        if (i%2 != 0){
            sum+=i;
        }
    cout<<"The sum of all the off numbers upto"<<n<<"is"<<sum;
    }
    return 0;
}