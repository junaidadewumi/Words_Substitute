# REGULAR EXPRESSION ASSIGNMENT
import re
employ = """                    EMPLOYMENT LETTER
Applicant,
05, Paradise Street,
United Arab Emirates,
20th June, 2023,
Dear Applicant,
Ref-Application No.4664/Dated 01/06/2023

With reference to your application for the post of ARMY Members Manager (AMM), we hereby employ
you for the same post. We have gone though your profile provided in the application and we found
that you are the right candidate for the post.
                                                                                    sincerely,
                                                                                    BTS LEADER
                                                                                    KIM NAMJOON
                                                                                    Seoul, Korea.
"""

emp = re.sub("Applicant", "JUNAID, S. O.", employ)
hire = re.sub("employ", "hire", emp)
supplied = re.sub("provided", "supplied", hire)
Rap_Monster = re.sub("KIM NAMJOON", "Rap Monster", supplied)
employee = re.sub("candidate", "employee", Rap_Monster)
print(employee)