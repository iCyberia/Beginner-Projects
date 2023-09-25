#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    
    ifstream theFile("FahrenheitTemperature.txt"); // open file into object

    string name; // Declare variables
    int temp;

    ofstream outFile("CelciusTemperature.txt"); // out file object

    while (theFile >> name >> temp) {
        temp = (temp - 32) * 5 / 9; // convert temp
        outFile << name << " " << temp << endl; // write each line
    }

    return 0;
}
