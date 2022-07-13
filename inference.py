class Inference():

    def __init__(self , age, blood_pressure, blood_sugar,
                 cholestrol, heart_rate, ecg, old_peak, chest_pain,
                 exercise, thallium, sex):

        self.age = age
        self.blood_pressure = blood_pressure
        self.blood_sugar = blood_sugar
        self.cholestrol = cholestrol
        self.heart_rate = heart_rate
        self.ecg = ecg
        self.old_peak = old_peak
        self.chest_pain = chest_pain
        self.exercise = exercise
        self.thallium = thallium
        self.sex = sex

        self.sick_1 = 0
        self.sick_2 = 0
        self.sick_3 = 0
        self.sick_4 = 0
        self.healthy = 0

    def infer(self):

        # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, min(self.age['very_old'], self.chest_pain['atypical_anginal']))

        # RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, min(self.heart_rate['high'], self.age['old']))

        # RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, min(self.sex['male'], self.heart_rate['medium']))

        # RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, min(self.sex['female'], self.heart_rate['medium']))

        # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, min(self.chest_pain['non_anginal_pain'], self.blood_pressure['high']))

        # RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, min(self.chest_pain['typical_anginal'], self.heart_rate['medium']))

        # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, min(self.blood_sugar['true'], self.age['mild']))

        # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, min(self.blood_sugar['false'], self.blood_pressure['very_high']))

        # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, max(self.chest_pain['asymptomatic'], self.age['very_old']))

        # RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, max(self.blood_pressure['high'], self.heart_rate['low']))

        # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
        self.healthy = max(self.healthy, self.chest_pain['typical_anginal'])

        # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.chest_pain['atypical_anginal'])

        # RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.chest_pain['non_anginal_pain'])

        # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.chest_pain['asymptomatic'])

        # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.chest_pain['asymptomatic'])

        # RULE 16: IF (sex IS female) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.sex['female'])

        # RULE 17: IF (sex IS male) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.sex['male'])

        # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
        self.healthy = max(self.healthy, self.blood_pressure['low'])

        # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.blood_pressure['medium'])

        # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.blood_pressure['high'])

        # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.blood_pressure['high'])

        # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.blood_pressure['very_high'])

        # RULE 23: IF (cholesterol IS low) THEN health IS healthy;
        self.healthy = max(self.healthy, self.cholestrol['low'])

        # RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.cholestrol['medium'])

        # RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.cholestrol['high'])

        # RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.cholestrol['high'])

        # RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.cholestrol['very_high'])

        # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.blood_sugar['true'])

        # RULE 29: IF (ECG IS normal) THEN health IS healthy;
        self.healthy = max(self.healthy, self.ecg['normal'])

        # RULE 30: IF (ECG IS normal) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.ecg['normal'])

        # RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.ecg['abnormal'])

        # RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.ecg['hypertrophy'])
        
        # RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.ecg['hypertrophy'])

        # RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;
        self.healthy = max(self.healthy, self.heart_rate['low'])

        # RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.heart_rate['medium'])

        # RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.heart_rate['medium'])

        # RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.heart_rate['high'])

        # RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.heart_rate['high'])

        # RULE 39: IF (exercise IS true) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.exercise['true'])

        # RULE 40: IF (old_peak IS low) THEN health IS healthy;
        self.healthy = max(self.healthy, self.old_peak['low'])

        # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.old_peak['low'])

        # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.old_peak['terrible'])

        # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.old_peak['terrible'])

        # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.old_peak['risk'])

        # RULE 45: IF (thallium IS normal) THEN health IS healthy;
        self.healthy = max(self.healthy, self.thallium['normal'])

        # RULE 46: IF (thallium IS normal) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.thallium['normal'])

        # RULE 47: IF (thallium IS medium) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.thallium['medium'])

        # RULE 48: IF (thallium IS high) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.thallium['high'])

        # RULE 49: IF (thallium IS high) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.thallium['high'])

        # RULE 50: IF (age IS young) THEN health IS healthy;
        self.healthy = max(self.healthy, self.age['young'])

        # RULE 51: IF (age IS mild) THEN health IS sick_1;
        self.sick_1 = max(self.sick_1, self.age['mild'])

        # RULE 52: IF (age IS old) THEN health IS sick_2;
        self.sick_2 = max(self.sick_2, self.age['old'])

        # RULE 53: IF (age IS old) THEN health IS sick_3;
        self.sick_3 = max(self.sick_3, self.age['old'])

        # RULE 54: IF (age IS very_old) THEN health IS sick_4;
        self.sick_4 = max(self.sick_4, self.age['very_old'])

        return self.healthy, self.sick_1, self.sick_2, self.sick_3, self.sick_4
        
        
        