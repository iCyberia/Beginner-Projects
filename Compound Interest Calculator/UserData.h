#pragma once
#ifndef AIRGEADBANKINGM4_USERDATA_H
#define AIRGEADBANKINGM4_USERDATA_H
#endif

class UserData { // Define user data class
public:
	void setInitInvestment(double t_initial);
	double getInitInvestment();
	void setMonDeposit(double t_monthly);
	double getMonDeposit();
	void setAnnInterest(double t_interest);
	double getAnnInterest();
	void setYears(int t_years);
	int getYears();

	double calcInterestWithOutDeposits(int t_year);
	double calcInterestWithDeposits(double t_initial);

private:
	double m_initInvestment;
	double m_monDeposit;
	double m_annInterest;
	int m_years;

};