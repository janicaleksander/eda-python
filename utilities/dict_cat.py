def get_dict(name):
    if name == "Marital status":
        return {
            1: "Single",
            2: "Married",
            3: "Widower",
            4: "Divorced",
            5: "Facto union",
            6: "Legally separated"
        }
    elif name == "Nationality":
        return {
            1: "Portuguese",
            2: "German",
            3: "Spanish",
            4: "Italian",
            5: "Dutch",
            6: "English",
            7: "Lithuanian",
            8: "Angolan",
            9: "Cape Verdean",
            10: "Guinean",
            11: "Mozambican",
            12: "Santomean",
            13: "Turkish",
            14: "Brazilian",
            15: "Romanian",
            16: "Moldova (Republic of)",
            17: "Mexican",
            18: "Ukrainian",
            19: "Russian",
            20: "Cuban",
            21: "Colombian"
        }
    elif name == "Application mode":
        return {
            1: "1st phase general contingent",
            2: "Ordinance No. 612/93",
            3: "1st phase special contingent (Azores Island)",
            4: "Holders of other higher courses",
            5: "Ordinance No. 854-B/99",
            6: "International student (bachelor)",
            7: "1st phase special contingent (Madeira Island)",
            8: "2nd phase general contingent",
            9: "3rd phase general contingent",
            10: "Ordinance No. 533-A/99, item b2) (Different Plan)",
            11: "Ordinance No. 533-A/99, item b3 (Other Institution)",
            12: "Over 23 years old",
            13: "Transfer",
            14: "Change in course",
            15: "Technological specialization diploma holders",
            16: "Change in institution/course",
            17: "Short cycle diploma holders",
            18: "Change in institution/course (International)"
        }
    elif name == "Course":
        return {
            1: "Biofuel Production Technologies",
            2: "Animation and Multimedia Design",
            3: "Social Service (evening attendance)",
            4: "Agronomy",
            5: "Communication Design",
            6: "Veterinary Nursing",
            7: "Informatics Engineering",
            8: "Equiniculture",
            9: "Management",
            10: "Social Service",
            11: "Tourism",
            12: "Nursing",
            13: "Oral Hygiene",
            14: "Advertising and Marketing Management",
            15: "Journalism and Communication",
            16: "Basic Education",
            17: "Management (evening attendance)"
        }
    elif name in ["Mother's qualification", "Father's qualification"]:
        return {
            1: "Secondary Education—12th Year of Schooling or Equivalent",
            2: "Higher Education bachelor's degree",
            3: "Higher Education degree",
            4: "Higher Education master's degree",
            5: "Higher Education doctorate",
            6: "Frequency of Higher Education",
            7: "12th Year of Schooling not completed",
            8: "11th Year of Schooling not completed",
            9: "7th Year (Old)",
            10: "Other—11th Year of Schooling",
            11: "2nd year complementary high school course",
            12: "10th Year of Schooling",
            13: "General commerce course",
            14: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
            15: "Complementary High School Course",
            16: "Technical-professional course",
            17: "Complementary High School Course—not concluded",
            18: "7th year of schooling",
            19: "2nd cycle of the general high school course",
            20: "9th Year of Schooling—not completed",
            21: "8th year of schooling",
            22: "General Course of Administration and Commerce",
            23: "Supplementary Accounting and Administration",
            24: "Unknown",
            25: "Cannot read or write",
            26: "Can read without having a 4th year of schooling",
            27: "Basic education 1st cycle (4th/5th year) or equivalent",
            28: "Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent",
            29: "Technological specialization course",
            30: "Higher education—degree (1st cycle)",
            31: "Specialized higher studies course",
            32: "Professional higher technical course",
            33: "Higher Education—master's degree (2nd cycle)",
            34: "Higher Education—doctorate (3rd cycle)"
        }
    elif name == "Previous qualification":
        return {
            1: "Secondary education",
            2: "Higher education bachelor's degree",
            3: "Higher education degree",
            4: "Higher education master's degree",
            5: "Higher education doctorate",
            6: "Frequency of higher education",
            7: "12th year of schooling not completed",
            8: "11th year of schooling not completed",
            9: "Other 11th year of schooling",
            10: "10th year of schooling",
            11: "10th year of schooling not completed",
            12: "Basic education 3rd cycle (9th/10th/11th year) or equivalent",
            13: "Basic education 2nd cycle (6th/7th/8th year) or equivalent",
            14: "Technological specialization course",
            15: "Higher education degree (1st cycle)",
            16: "Professional higher technical course",
            17: "Higher education master's degree (2nd cycle)"
        }
    elif name in ["Mother's occupation", "Father's occupation"]:
        return {
            1: "Student",
            2: "Legislative and Executive Representatives, Directors, and Managers",
            3: "Intellectual and Scientific Professionals",
            4: "Intermediate Level Technicians and Professions",
            5: "Administrative Staff",
            6: "Personal Services, Security, and Sales Workers",
            7: "Farmers and Skilled Agricultural Workers",
            8: "Industry, Construction, and Craft Workers",
            9: "Machine Operators and Assemblers",
            10: "Unskilled Workers",
            11: "Armed Forces",
            12: "Other",
            13: "(blank)",
            14: "Armed Forces Officers",
            15: "Armed Forces Sergeants",
            16: "Other Armed Forces Personnel",
            17: "Administrative and Commercial Service Directors",
            18: "Hotel, Catering, Trade, and Other Service Directors",
            19: "Science, Engineering, and Mathematics Professionals",
            20: "Health Professionals",
            21: "Teachers",
            22: "Finance, Accounting, and Administrative Specialists",
            23: "Intermediate Level Science and Engineering Technicians",
            24: "Health Technicians",
            25: "Legal, Social, Cultural, and Sports Technicians",
            26: "ICT Technicians",
            27: "Office Workers and Data Entry Staff",
            28: "Accounting and Registry-related Operators",
            29: "Administrative Support Staff",
            30: "Personal Service Workers",
            31: "Sales Workers",
            32: "Personal Care Workers",
            33: "Security and Protection Services Personnel",
            34: "Market-oriented Farmers",
            35: "Subsistence Farmers, Fishermen, and Hunters",
            36: "Construction Workers",
            37: "Metalworkers",
            38: "Electricians",
            39: "Food, Wood, and Clothing Industry Workers",
            40: "Fixed Plant Operators",
            41: "Assembly Workers",
            42: "Vehicle Operators",
            43: "Unskilled Agricultural Workers",
            44: "Unskilled Construction and Factory Workers",
            45: "Meal Preparation Assistants",
            46: "Street Vendors and Service Providers"
        }
    elif name == "Gender":
        return {1: "Male", 0: "Female"}
    elif name == "Daytime/evening attendance":
        return {1: "Daytime", 0: "Evening"}
    elif name in ["Displaced", "Educational special needs", "Debtor", "Tuition fees up to date", "Scholarship holder", "International"]:
        return {1: "Yes", 0: "No"}
    elif name in "Target":
        return {"Graduate": "Graduate", "Dropout": "Dropout", "Enrolled":"Enrolled"}
    else:
        return None
