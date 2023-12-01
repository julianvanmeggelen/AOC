#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string line;
    ifstream MyReadFile("1.txt");
    while (getline (MyReadFile, line)) {
        cout << line;
    }
}