#include <iostream>
#include <fstream>
#include <cstdlib> 
using namespace std;

int main(){
    string line;
    ifstream MyReadFile("input.txt");
    int res = 0;
    while (getline(MyReadFile, line)) {
        vector<char> allNumeric;
        for(int i =0; i < line.length(); i++){
            if(isdigit(line[i]) != 0){
                allNumeric.push_back(line[i]);
            }
        }
        char first = allNumeric[0];
        char last = allNumeric.back();
        string conc = string(1,first) + last;
        int sum = stoi(conc);
        res += sum;
    }
    cout << res;
    return 0;
}