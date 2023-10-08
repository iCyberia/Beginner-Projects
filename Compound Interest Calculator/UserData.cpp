#include <iostream>
#include <math.h>
#include <iomanip>
#include "UserData.h"
using namespace std;


void UserData::setInitInvestment(double t_initial) {  // Set Initial Investment
	this->m_initInvestment = t_initial;
}
double UserData::getInitInvestment() {  // Get Initial Investment
	return m_initInvestment;
}

void UserData::setMonDeposit(double t_monthly) {  // Set Monthly Deposit
	this->m_monDeposit = t_monthly;
}
double UserData::getMonDeposit() {  // Get Monthly Deposit
	return m_monDeposit;
}

void UserData::setAnnInterest(double t_interest) {  // Set Annual Interest
	this->m_annInterest = t_interest;
}
double UserData::getAnnInterest() { // Get Annual Interest
	return m_annInterest;
}

void UserData::setYears(int t_years) {  // Set Years
	this->m_years = t_years;
}
int UserData::getYears() { // Get years
	return m_years;
}

double UserData::calcInterestWithOutDeposits(int t_year) {  // Calculate with out monthly deposit
	double interest = this->m_annInterest / 100;
	return this->m_initInvestment * pow(1 + (interest / 1), t_year) - 1;
}
double UserData::calcInterestWithDeposits(double t_initial) {  // Calculate with monthly deposit
	double interest = this->m_annInterest / 100;
	return (t_initial + this->m_monDeposit) * (interest / 12);
}