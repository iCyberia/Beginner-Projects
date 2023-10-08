#pragma once
#ifndef AIRGEADBANKINGM4_SYSTEMDISPLAY_H
#define AIRGEADBANKINGM4_SYSTEMDISPLAY_H
#endif
#include <iostream>
#include <iomanip>
using namespace std;

void displayBanner() { // Aigead Banking Banner

	cout << "|==================================================|" << endl;
	cout << "                 Airgead Banking" << endl;
	cout << "|==================================================|" << endl;

}

void displayTableWODeposit(int years, UserData user) {  // Table with out monthly deposits

	double yearEndBal;
	double initTemp;
	double earnedInterest;

	displayBanner();
	cout << "               w/o Monthly Deposits" << endl;
	cout << "|==================================================|" << endl;
	cout << " Year   " << "Year End Balance   " << "Year End Earned Interest" << endl;
	cout << "---------------------------------------------------" << endl;

	for (int i = 1; i <= years; i++) {   // For loop line for each ear
		yearEndBal = user.calcInterestWithOutDeposits(i) + user.getInitInvestment();  // Year end balance
		initTemp = user.calcInterestWithOutDeposits(i - 1) + user.getInitInvestment(); // Prior year end balance 
		earnedInterest = yearEndBal - initTemp; // Calculates interest
		cout << right << fixed << setprecision(2) // Table lines
			<< setw(5) << i 
			<< setw(10) << "$" << setw(9) << yearEndBal
			<< setw(18) << "$" << setw(9) << earnedInterest << endl;
	}
	cout << endl;
}

void displayTableWDeposit(int years, UserData user) { // Table with out monthly deposits

	double yearEndBal;
	double earnedInterest;
	double interest;
	double annEarnedInterest;

	cout << "|==================================================|" << endl;
	cout << "                w/ Monthly Deposits" << endl;
	cout << "|==================================================|" << endl;
	cout << " Year   " << "Year End Balance   " << "Year End Earned Interest" << endl;
	cout << "---------------------------------------------------" << endl;

	yearEndBal = user.getInitInvestment();

	for (int i = 1; i <= years; i++) { // For loop line for each ear

		annEarnedInterest = 0;  // Resets annual interest

		for (int j = 0; j < 12; j++) {  // For loop line for each ear
			earnedInterest = user.calcInterestWithDeposits(yearEndBal);  // Monthly interest
			annEarnedInterest = annEarnedInterest + earnedInterest;  // Annual Interest
			yearEndBal = yearEndBal + user.getMonDeposit() + earnedInterest; // Year end balance
		}
		cout << right << fixed << setprecision(2) // Table lines
			<< setw(5) << i
			<< setw(10) << "$" << setw(9) << yearEndBal
			<< setw(18) << "$" << setw(9) << annEarnedInterest << endl;
	}
}