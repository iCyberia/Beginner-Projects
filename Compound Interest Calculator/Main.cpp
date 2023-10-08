// Hiroshi Thomas
// CS-210-R1790 Programming Languages 23EW1
// Project Two Airgead Banking

#include <iostream>
#include "userData.h"
#include "SystemDisplay.h"
using namespace std;

int main() {

	UserData data;  // Creating UserData class as object

	int iYears; // Declaring variables
	double initInvestment, monDeposit, annInterest, earInterest, yearEndBalance;

	// Declaring variables for while loop
	char useInput = NULL;
	bool runApp = true;

	while (runApp) {
		displayBanner(); // Aigead Banking Header

		cout << "Initial Investment Amount: $"; // Get user input
		cin >> initInvestment;
		if (cin.fail()) { // Make sure it's the correct input type
			cin.clear();
			cin.ignore();
			cout << "[-] Error: Decimal numbers only" << endl;
			cout << "Initial Investment Amount: $";
			cin >> initInvestment;
		}

		cout << "Monthly Deposit: $"; // Get user input
		cin >> monDeposit;
		if (cin.fail()) { // Make sure it's the correct input type
			cin.clear();
			cin.ignore();
			cout << "[-] Error: Decimal numbers only" << endl;
			cout << "Monthly Deposit: $";
			cin >> monDeposit;
		}

		cout << "Annual Interest: %"; // Get user input
		cin >> annInterest;
		if (cin.fail()) { // Make sure it's the correct input type
			cin.clear();
			cin.ignore();
			cout << "[-] Error: Decimal or Whole numbers only" << endl;
			cout << "Monthly Deposit: $";
			cin >> annInterest;
		}

		cout << "Number of years: "; // Get user input
		cin >> iYears;
		if (cin.fail()) { // Make sure it's the correct input type
			cin.clear();
			cin.ignore();
			cout << "[-] Error: Whole numbers only" << endl;
			cout << "Monthly Deposit: $";
			cin >> iYears;
		}
		cout << endl;
		system("cls"); // Clear Screen

		// Set UserData class object
		data.setInitInvestment(initInvestment);
		data.setMonDeposit(monDeposit);
		data.setAnnInterest(annInterest);
		data.setYears(iYears);

		displayTableWODeposit(data.getYears(), data);  // Print Graph with no deposit
		displayTableWDeposit(data.getYears(), data); // Print Graph with deposit
		cout << endl;

		cout << "Type 'Q' to Quit or 'R' to retry: ";  // Quit or restart
		cin >> useInput;

		if (useInput == 'Q' || useInput == 'q') { // end loop
			runApp = false;
		}
		system("cls"); // Clear Screen
	}
	return 0;
}