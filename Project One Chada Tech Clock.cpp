// CS-210-R1790 Programming Languages 23EW1
// Project One
// Chada Tech Clock
// Hiroshi Thomas

#include <iostream>
#include <sstream>
#include <string.h>
#include <iomanip>
#include <vector>
using namespace std;


// variables
int timeLength;
string userTime;
int num24 = 0; 
int menuSelect = 0;
auto asteriskRow = std::string(26, '*');
vector<int> numTimes(4);
vector<string> userAMPM(1);

// Display menu, and based on menu selection operate AM/PM and 60/0 rollover
int menu() {
	// Display menu
	cout << asteriskRow << endl
		<< "* 1-Add One Hour         *" << endl
		<< "* 2-Add One Minute       *" << endl
		<< "* 3-Add One Second       *" << endl
		<< "* 4-Exit Program         *" << endl
		<< asteriskRow << endl;

	// Take menu input
	cin >> menuSelect;
	while (!menuSelect >= 1 && !menuSelect <= 4) {
		cin.clear();
		cin.ignore(100, '\n');
		cout << "Select a valid option 1-4" << endl;
		cin >> menuSelect;
		if (menuSelect < 1 && menuSelect < 4) {
			cin.clear();
			cin.ignore(100, '\n');
			cout << "Select a valid option 1-4" << endl;
		}
	}



	// make selected mene changes
	if (menuSelect == 1) {
		numTimes.at(0) = numTimes.at(0) + 1;
		numTimes.at(3) = numTimes.at(3) + 1;
		if (numTimes.at(0) > 12) {
			numTimes.at(0) = 1;
		}
		if (numTimes.at(0) == 12) {

			if (userAMPM.at(0) == "AM") {
				userAMPM.at(0) = "PM";
			}
			else if (userAMPM.at(0) == "PM") {
				userAMPM.at(0) = "AM";
			}
		}
		if (numTimes.at(3) > 23) {
			numTimes.at(3) = 0;
		}
	}
	if (menuSelect == 2) {
		numTimes.at(1) = numTimes.at(1) + 1;
		if (numTimes.at(1) == 60) {
			numTimes.at(1) = 0;
		}
	}
	if (menuSelect == 3) {
		numTimes.at(2) = numTimes.at(2) + 1;
		if (numTimes.at(2) == 60) {
			numTimes.at(2) = 0;
		}
	}
	if (menuSelect == 4) {
		menuSelect = 4;
	}

	return menuSelect;
}


void getTimeandlegth() {
	// get time from user
	cout << "Enter time as Hours:Minutes:Seconds AM/PM " << endl;
	std::getline(std::cin, userTime);
	timeLength = userTime.length(); 

	// check length to partially check format
	while (timeLength != 11) {
		cout << "Improper format" << endl;
		cout << endl;
		cout << "Use correct format 01:23:45 PM ";
		std::getline(std::cin, userTime);
		timeLength = userTime.length();
	}
}


// split user input time to vector
vector<int> splitTimeandStoi() {
	// split out to sub strings
	string userSeconds = userTime.substr(6, 2);
	string userMinutes = userTime.substr(3, 2);
	string userHours = userTime.substr(0, 2);
	userAMPM.at(0) = userTime.substr(9, 2);

	// change strings to integers
	int numSeconds = stoi(userSeconds, 0, 10);
	int numMinutes = stoi(userMinutes, 0, 10);
	int numHours = stoi(userHours, 0, 10);

	// assign to vectors
	numTimes.at(0) = numHours;
	numTimes.at(1) = numMinutes;
	numTimes.at(2) = numSeconds;

	// add for military time
	if (userAMPM.at(0) == "PM") {
		numTimes.at(3) = numTimes.at(0) + 12;
	}
	return numTimes;
}

// display time
void display() {

	cout << endl << asteriskRow << "      " << asteriskRow << endl;
	cout << "*      12-Hour Clock     *      *      24-Hour Clock     *" << endl;
	cout << "*       "
		
		<< setw(2) << setfill('0') << numTimes.at(0) << ":" << 
		setw(2) << setfill('0') << numTimes.at(1) << ":" <<
		setw(2) << setfill('0') << numTimes.at(2) << " " <<
		setw(2) << setfill('0') << userAMPM.at(0)
		<< "      *      *         "
		<< 
		setw(2) << setfill('0') << numTimes.at(3) << ":" <<
		setw(2) << setfill('0') << numTimes.at(1) << ":" <<
		setw(2) << setfill('0') << numTimes.at(2)
		<< "        *" << endl;
	cout << asteriskRow << "      " << asteriskRow << endl << endl << endl << endl;
}


// main
int main()
{
	getTimeandlegth();
	splitTimeandStoi();
	while (menuSelect != 4) {
		display();
		menu();
	}
	return 0;
}