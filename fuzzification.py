class Fuzzification:
    def __init__(self , input_dict):

        self.input_dict = input_dict

    def fuzzificate(self):
        return (
            self.age_fuzzificate(),
            self.blood_pressure_fuzzificate(),
            self.blood_sugar_fuzzificate(),
            self.cholestrol_fuzzificate(),
            self.heart_rate_fuzzificate(),
            self.ecg_fuzzificate(),
            self.old_peak_fuzzificate(),
            self.chest_pain_fuzzificate(),
            self.exercise_fuzzificate(),
            self.thallium_scan_fuzzificate(),
            self.sex_fuzzificate()
            )        


    def calc_membership(self, crisp_val, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        a = (y2 - y1) / (x2 - x1)
        fuzzy_value = y1 + a * (crisp_val - x1)
        return fuzzy_value


    def age_fuzzificate(self):
        return {
            'young': self.age_young(),
            'mild': self.age_mild(),
            'old': self.age_old(),
            'very_old': self.age_veryold()
            }

    def age_young(self):
        crisp_input = int(self.input_dict['age'])
        if crisp_input <= 29:
            return 1
        elif 29 < crisp_input < 38:
            return self.calc_membership(crisp_input, (29, 1), (38, 0))
        else:
            return 0


    def age_mild(self):
        crisp_input = int(self.input_dict['age'])
        if crisp_input <= 33 or crisp_input >= 45:
            return 0
        elif 33 < crisp_input <= 38:
            return self.calc_membership(crisp_input, (33, 0), (38, 1))
        else:
            return self.calc_membership(crisp_input, (45, 0), (38, 1))


    def age_old(self):
        crisp_input = int(self.input_dict['age'])
        if crisp_input <= 40 or crisp_input >= 58:
            return 0
        elif 40 < crisp_input <= 48:
            return self.calc_membership(crisp_input, (40, 0), (48, 1))
        else:
            return self.calc_membership(crisp_input, (58, 0), (48, 1))


    def age_veryold(self):
        crisp_input = int(self.input_dict['age'])
        if crisp_input <= 52:
            return 0
        elif 40 < crisp_input <= 48:
            return self.calc_membership(crisp_input, (52, 0), (60, 1))
        else:
            return 1


    def blood_pressure_fuzzificate(self):
        return {
            'low': self.bp_low(),
            'medium': self.bp_medium(),
            'high': self.bp_high(),
            'very_high': self.bp_veryhigh()
            }

    def bp_low(self):
        crisp_input = int(self.input_dict['blood_pressure'])
        if crisp_input <= 111:
            return 1
        elif 111 < crisp_input < 134:
            return self.calc_membership(crisp_input, (111, 1), (134, 0))
        else:
            return 0


    def bp_medium(self):
        crisp_input = int(self.input_dict['blood_pressure'])
        if crisp_input <= 127 or crisp_input >= 153:
            return 0
        elif 127 < crisp_input <= 139:
            return self.calc_membership(crisp_input, (127, 0), (139, 1))
        else:
            return self.calc_membership(crisp_input, (153, 0), (139, 1))


    def bp_high(self):
        crisp_input = int(self.input_dict['blood_pressure'])
        if crisp_input <= 142 or crisp_input >= 172:
            return 0
        elif 142 < crisp_input <= 157:
            return self.calc_membership(crisp_input, (142, 0), (157, 1))
        else:
            return self.calc_membership(crisp_input, (172, 0), (157, 1))


    def bp_veryhigh(self):
        crisp_input = int(self.input_dict['blood_pressure'])
        if crisp_input <= 154:
            return 0
        elif 154 < crisp_input <= 171:
            return self.calc_membership(crisp_input, (154, 0), (171, 1))
        else:
            return 1
    
    def blood_sugar_fuzzificate(self):
        crisp_input = int(self.input_dict['blood_sugar'])
        if crisp_input > 120:
            return {'true': 1, 'false': 0}

        else:
            return {'true': 0, 'false': 1}
        
    
    def cholestrol_fuzzificate(self):
        return {
            'low': self.cholesterol_low(),
            'medium': self.cholesterol_medium(),
            'high': self.cholesterol_high(),
            'very_high': self.cholesterol_veryhigh()
            }
    
    def cholesterol_low(self):
        crisp_input = int(self.input_dict['cholestrol'])
        if crisp_input <= 151:
            return 1
        elif 151 < crisp_input < 197:
            return self.calc_membership(crisp_input, (151, 1), (197, 0))
        else:
            return 0


    def cholesterol_medium(self):
        crisp_input = int(self.input_dict['cholestrol'])
        if crisp_input <= 188 or crisp_input >= 250:
            return 0
        elif 188 < crisp_input <= 215:
            return self.calc_membership(crisp_input, (188, 0), (215, 1))
        else:
            return self.calc_membership(crisp_input, (250, 0), (215, 1))


    def cholesterol_high(self):
        crisp_input = int(self.input_dict['cholestrol'])
        if crisp_input <= 217 or crisp_input >= 307:
            return 0
        elif 217 < crisp_input <= 263:
            return self.calc_membership(crisp_input, (217, 0), (263, 1))
        else:
            return self.calc_membership(crisp_input, (307, 0), (263, 1))


    def cholesterol_veryhigh(self):
        crisp_input = int(self.input_dict['cholestrol'])
        if crisp_input <= 281:
            return 0
        elif 281 < crisp_input <= 347:
            return self.calc_membership(crisp_input, (281, 0), (347, 1))
        else:
            return 1


    def heart_rate_fuzzificate(self):
        return {
            'low': self.heart_rate_low(),
            'medium': self.heart_rate_medium(),
            'high': self.heart_rate_high()
            }

    def heart_rate_low(self):
        crisp_input = int(self.input_dict['heart_rate'])
        if crisp_input <= 100:
            return 1
        elif 100 < crisp_input < 141:
            return self.calc_membership(crisp_input, (100, 1), (141, 0))
        else:
            return 0


    def heart_rate_medium(self):
        crisp_input = int(self.input_dict['heart_rate'])
        if crisp_input <= 111 or crisp_input >= 194:
            return 0
        elif 111 < crisp_input <= 152:
            return self.calc_membership(crisp_input, (111, 0), (152, 1))
        else:
            return self.calc_membership(crisp_input, (194, 0), (152, 1))


    def heart_rate_high(self):
        crisp_input = int(self.input_dict['heart_rate'])
        if crisp_input <= 152:
            return 0
        elif 152 < crisp_input <= 210:
            return self.calc_membership(crisp_input, (152, 0), (210, 1))
        else:
            return 1

    def ecg_fuzzificate(self):
        return {
            'normal': self.ecg_normal(),
            'abnormal': self.ecg_abnormal(),
            'hypertrophy': self.ecg_hypertrophy()
            }

    def ecg_normal(self):
        crisp_input = float(self.input_dict['ecg'])
        if crisp_input <= 0:
            return 1
        elif 0 < crisp_input < 0.4:
            return self.calc_membership(crisp_input, (0, 1), (0.4, 0))
        else:
            return 0


    def ecg_abnormal(self):
        crisp_input = float(self.input_dict['ecg'])
        if crisp_input <= 0.2 or crisp_input >= 1.8:
            return 0
        elif 0.2 < crisp_input <= 1:
            return self.calc_membership(crisp_input, (0.2, 0), (1, 1))
        else:
            return self.calc_membership(crisp_input, (1.8, 0), (1, 1))


    def ecg_hypertrophy(self):
        crisp_input = float(self.input_dict['ecg'])
        if crisp_input <= 1.4:
            return 0
        elif 1.4 < crisp_input <= 1.9:
            return self.calc_membership(crisp_input, (1.4, 0), (1.9, 1))
        else:
            return 1
    
    def old_peak_fuzzificate(self):
        return {
            'low': self.old_peak_low(),
            'risk': self.old_peak_risk(),
            'terrible': self.old_peak_terrible()
            }

    def old_peak_low(self):
        crisp_input = float(self.input_dict['old_peak'])
        if crisp_input <= 1:
            return 1
        elif 1 < crisp_input < 2:
            return self.calc_membership(crisp_input, (1, 1), (2, 0))
        else:
            return 0


    def old_peak_risk(self):
        crisp_input = float(self.input_dict['old_peak'])
        if crisp_input <= 1.5 or crisp_input >= 4.2:
            return 0
        elif 1.5 < crisp_input <= 2.8:
            return self.calc_membership(crisp_input, (1.5, 0), (2.8, 1))
        else:
            return self.calc_membership(crisp_input, (4.2, 0), (2.8, 1))


    def old_peak_terrible(self):
        crisp_input = float(self.input_dict['old_peak'])
        if crisp_input <= 2.5:
            return 0
        elif 2.5 < crisp_input <= 4:
            return self.calc_membership(crisp_input, (2.5, 0), (4, 1))
        else:
            return 1

    def chest_pain_fuzzificate(self):
        crisp_input = int(self.input_dict["chest_pain"])
        return {
            'typical_anginal': 1 if crisp_input == 1 else 0,
            'atypical_anginal': 1 if crisp_input == 2 else 0,
            'non_anginal_pain': 1 if crisp_input == 3 else 0,
            'asymptomatic': 1 if crisp_input == 4 else 0
            }

    def exercise_fuzzificate(self):
        crisp_input = int(self.input_dict['exercise'])
        return {
            'true': 1 if crisp_input == 1 else 0,
            'false': 1 if crisp_input == 0 else 0
            }

    def thallium_scan_fuzzificate(self):
        crisp_input = int(self.input_dict['thallium_scan'])
        return {
            'normal': 1 if crisp_input == 3 else 0,
            'medium': 1 if crisp_input == 6 else 0,
            'high': 1 if crisp_input == 7 else 0
            }

    def sex_fuzzificate(self):

        crisp_input = int(self.input_dict['sex'])
        return {
            'female': 1 if crisp_input == 1 else 0,
            'male': 1 if crisp_input == 0 else 0
            }

            