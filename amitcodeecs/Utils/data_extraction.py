class UserManager:
    _user_data = None

    @staticmethod
    def set_user_data(data):
        UserManager._user_data = data
    
    @staticmethod
    def first_name():
        return UserManager._user_data.get("personal").get("firstName")

    @staticmethod
    def last_name():
        return UserManager._user_data.get("personal").get("lastName")
    
    @staticmethod
    def email():
        return UserManager._user_data.get("email")
    
    @staticmethod
    def phone():
        return UserManager._user_data.get("personal").get("mobileNumber")
    
    @staticmethod
    def funding_type():
        return UserManager._user_data.get("preApproval").get("fundingType")
    
    @staticmethod
    def income_source():
        return UserManager._user_data.get("preApproval").get("incomeSource")
    
    @staticmethod
    def education():
        return UserManager._user_data.get("preApproval").get("education")
    
    @staticmethod
    def monthly_income():
        return UserManager._user_data.get("preApproval").get("monthlyIncome")
    
    @staticmethod
    def funding_amount_personal():
        return UserManager._user_data.get("preApproval").get("fundingAmountPersonal")
    
    @staticmethod
    def funding_amount():
        return UserManager._user_data.get("preApproval").get("fundingAmount")
    
    @staticmethod
    def time_in_business():
        return UserManager._user_data.get("preApproval").get("timeInBusiness")
    
    @staticmethod
    def type_of_business():
        return UserManager._user_data.get("preApproval").get("typeOfBusiness")
    
    @staticmethod
    def revenue():
        return UserManager._user_data.get("preApproval").get("revenue")
    
    @staticmethod
    def funding_use():
        return UserManager._user_data.get("preApproval").get("fundingUse")
    
    @staticmethod
    def fico_score():
        return UserManager._user_data.get("preApproval").get("ficoScore")
    
    @staticmethod
    def credit_cards():
        return UserManager._user_data.get("preApproval").get("creditCards")
    
    @staticmethod
    def debts():
        return UserManager._user_data.get("preApproval").get("debts")
    
    @staticmethod
    def credit_limit():
        return UserManager._user_data.get("preApproval").get("creditLimit")
    
    @staticmethod
    def credit_card_utilization():
        return UserManager._user_data.get("preApproval").get("creditCardUtilization")
    
    @staticmethod
    def credit_history():
        return UserManager._user_data.get("preApproval").get("creditHistory")
    
    @staticmethod
    def derogatory_accounts():
        return UserManager._user_data.get("preApproval").get("derogatoryAccounts")
    
    @staticmethod
    def bankruptcy():
        return UserManager._user_data.get("preApproval").get("bankruptcy")
    
    @staticmethod
    def information_is_true():
        return UserManager._user_data.get("preApproval").get("informationIsTrue")
    
    @staticmethod
    def business_title():
        return UserManager._user_data.get("business").get("title")
    
    @staticmethod
    def business_name():
        return UserManager._user_data.get("business").get("businessName")
    
    @staticmethod
    def business_phone():
        return UserManager._user_data.get("business").get("businessPhone")
    
    @staticmethod
    def business_percent():
        return UserManager._user_data.get("business").get("businessPercent")
    
    @staticmethod
    def sole_owner():
        return UserManager._user_data.get("business").get("soleOwner")
    
    @staticmethod
    def anyone_25():
        return UserManager._user_data.get("business").get("anyone25")
    
    @staticmethod
    def monthly_spend():
        return UserManager._user_data.get("business").get("monthlySpend")
    
    @staticmethod
    def outstanding_invoices_amount():
        return UserManager._user_data.get("business").get("outstandingInvoicesAmount")
    
    @staticmethod
    def is_b2b():
        return UserManager._user_data.get("business").get("isB2B")
    
    @staticmethod
    def max_negative_days_per_month():
        return UserManager._user_data.get("business").get("maxNegativeDaysPerMonth")
    
    @staticmethod
    def max_nsf_per_month():
        return UserManager._user_data.get("business").get("maxNFSPerMonth")
    
    @staticmethod
    def min_avg_daily_balance():
        return UserManager._user_data.get("business").get("minAvgDailyBalance")
    
    @staticmethod
    def min_net_income_percentage():
        return UserManager._user_data.get("business").get("minNetIncomePercentage")
    
    @staticmethod
    def min_number_of_deposit_months():
        return UserManager._user_data.get("business").get("minNumberOfDepositMonths")
    
    @staticmethod
    def min_monthly_deposit_amount():
        return UserManager._user_data.get("business").get("minMonthlyDepositAmount")
    
    @staticmethod
    def has_deposit_account():
        return UserManager._user_data.get("business").get("hasDepositAccount")
    
    @staticmethod
    def days_worth_of_deposit():
        return UserManager._user_data.get("business").get("daysWorthOfDeposit")
    
    @staticmethod
    def annual_growth_rate_percentage():
        return UserManager._user_data.get("business").get("annualGrowthRatePercentage")
    
    @staticmethod
    def min_runways_months():
        return UserManager._user_data.get("business").get("minRunwaysMonths")
    
    @staticmethod
    def revenue_start_date():
        return UserManager._user_data.get("business").get("revenueStartDate")
    
    @staticmethod
    def business_dti_percentage():
        return UserManager._user_data.get("business").get("dtiPercentage")
    
    @staticmethod
    def business_address():
        return UserManager._user_data.get("business").get("businessAddress")
    
    @staticmethod
    def business_city():
        return UserManager._user_data.get("business").get("businessCity")
    
    @staticmethod
    def business_zipcode():
        return UserManager._user_data.get("business").get("businessZipcode")
    
    @staticmethod
    def business_state():
        return UserManager._user_data.get("business").get("businessState")
    
    @staticmethod
    def business_suite_no():
        return UserManager._user_data.get("business").get("businessSuiteNo")
    
    @staticmethod
    def business_email():
        return UserManager._user_data.get("business").get("businessEmail")
    
    @staticmethod
    def date_business_commenced():
        return UserManager._user_data.get("business").get("dateBusinessCommenced")
    
    @staticmethod
    def year_business_started():
        return UserManager.date_business_commenced().split("-")[0]
    
    @staticmethod
    def month_business_started():
        return UserManager.date_business_commenced().split("-")[1]

    
    @staticmethod
    def business_website():
        return UserManager._user_data.get("business").get("website")
    
    @staticmethod
    def industry_type():
        return UserManager._user_data.get("business").get("industryType")
    
    @staticmethod
    def incorporation_state():
        return UserManager._user_data.get("business").get("incorporationState")
    
    @staticmethod
    def business_entity():
        return UserManager._user_data.get("business").get("entity")
    
    @staticmethod
    def number_of_employees():
        return UserManager._user_data.get("business").get("numberOfEmployees")
    
    @staticmethod
    def ein_number():
        return UserManager._user_data.get("business").get("einNumber")
    
    @staticmethod
    def gross_sales():
        return UserManager._user_data.get("business").get("grossSales")
    
    @staticmethod
    def projected_gross_sales():
        return UserManager._user_data.get("business").get("projectedGrossSales")
    
    @staticmethod
    def exclude_cards():
        return UserManager._user_data.get("business").get("excludeCards")
    
    @staticmethod
    def middle_name():
        return UserManager._user_data.get("personal").get("middleName")
    
    @staticmethod
    def mother_maiden_name():
        return UserManager._user_data.get("personal").get("motherMaidenName")
    
    @staticmethod
    def birth_city():
        return UserManager._user_data.get("personal").get("birthCity")
    
    @staticmethod
    def household_income():
        return UserManager._user_data.get("personal").get("householdIncome")
    
    @staticmethod
    def personal_dti_percentage():
        return UserManager._user_data.get("personal").get("dtiPercentage")
    
    @staticmethod
    def personal_has_deposit_account():
        return UserManager._user_data.get("personal").get("hasDepositAccount")
    
    @staticmethod
    def housing_status():
        return UserManager._user_data.get("personal").get("housingStatus")
    
    @staticmethod
    def monthly_payment():
        return UserManager._user_data.get("personal").get("monthlyPayment")
    
    @staticmethod
    def years_at_address():
        return UserManager._user_data.get("personal").get("yearsAtAddress")
    
    @staticmethod
    def drivers_license_number():
        return UserManager._user_data.get("personal").get("driversLicenseNumber")
    
    @staticmethod
    def dl_state():
        return UserManager._user_data.get("personal").get("dlState")
    
    @staticmethod
    def dl_expiration_date():
        return UserManager._user_data.get("personal").get("dlExpirationDate")
    
    @staticmethod
    def dl_issue_date():
        return UserManager._user_data.get("personal").get("dlIssueDate")
    
    @staticmethod
    def current_employer():
        return UserManager._user_data.get("personal").get("currentEmployer")
    
    @staticmethod
    def years_at_current_employer():
        return UserManager._user_data.get("personal").get("yearsAtCurrentEmployer")
    
    @staticmethod
    def position():
        return UserManager._user_data.get("personal").get("position")
    
    @staticmethod
    def employment_type():
        return UserManager._user_data.get("personal").get("employmentType")
    
    @staticmethod
    def bank_accounts():
        return UserManager._user_data.get("personal").get("bankAccounts")
    
    @staticmethod
    def personal_income_source():
        return UserManager._user_data.get("personal").get("incomeSource")
    
    @staticmethod
    def ssn():
        return UserManager._user_data.get("personal").get("ssn")
    
    @staticmethod
    def dob():
        return UserManager._user_data.get("personal").get("dob")
    
    @staticmethod
    def home_address():
        return UserManager._user_data.get("personal").get("homeAddress")
    
    @staticmethod
    def city():
        return UserManager._user_data.get("personal").get("city")
    
    @staticmethod
    def zipcode():
        return UserManager._user_data.get("personal").get("zipcode")
    
    @staticmethod
    def state():
        return UserManager._user_data.get("personal").get("state")
    
    @staticmethod
    def suite_no():
        return UserManager._user_data.get("personal").get("suiteNo")
    
    @staticmethod
    def masked_ssn():
        return UserManager._user_data.get("personal").get("maskedSSN")
