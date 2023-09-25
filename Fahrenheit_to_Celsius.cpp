#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // open file into object
    ifstream theFile("FahrenheitTemperature.txt");

    // Declare variables
    string name;
    int temp;

    // out file object
    ofstream outFile("CelciusTemperature.txt");

    // while loop to convert and then write file  
    while (theFile >> name >> temp) {
        temp = (temp - 32) * 5 / 9;
        outFile << name << " " << temp << endl;
    }

    return 0;
}
