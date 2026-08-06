#pragma GCC optimize("O3", "unroll-loops")
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        while(right>left){
            right&=(right-1);
        }
        return right;
    }
};