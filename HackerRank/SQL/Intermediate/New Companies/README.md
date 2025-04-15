
# Title
New Companies

# Problem
Amber's conglomerate corporation just acquired some new companies.
Each of the companies follows this hierarchy:
Founder -> Lead Manager -> Senior Manager -> Manager -> Employee
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees.
Order your output by ascending company_code.
Note:
* The tables may contain duplicate records.
* The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2 and C_10, then the ascending company_codes will be C_1, C_10, and C_2. 

**Input Format**
The following tables contain company data:
* Company: The company_code is the code of the company and founder is the founder of the company.

|Column|Type|
|---|---|
|company_code|String|
|founder|String|

* Lead_manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.

|Column|Type|
|---|---|
|lead_manager_code|String|
|company_code|String|

* Senior_manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of ites lead manager, and the company_code is the code of the working company.

|Column|Type|
|---|---|
|senior_manager_code|String|
|lead_manager_code|String|
|company_code|String|

* Employee: The employee_code is the code of the employee, the manage_code is the code of ites manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

|Column|Type|
|---|---|
|employee_code|String|
|manager_code|String|
|senior_manger_code|String|
|lead_manager_code|String|
|company_code|String|

**Explanation**

In company  _C1_, the only lead manager is  _LM1_. There are two senior managers,  _SM1_  and  _SM2_, under  _LM1_. There is one manager,  _M1_, under senior manager  _SM1_. There are two employees,  _E1_  and  _E2_, under manager  _M1_.

In company  _C2_, the only lead manager is  _LM2_. There is one senior manager,  _SM3_, under  _LM2_. There are two managers,  _M2_  and  _M3_, under senior manager  _SM3_. There is one employee,  _E3_, under manager  _M2_, and another employee,  _E4_, under manager,  _M3_.
