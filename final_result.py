import fuzzification
import inference
import defuzzification
class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        f = fuzzification.Fuzzification(input_dict)
        age, blood_pressure, blood_sugar,cholestrol, heart_rate, ecg, old_peak, chest_pain, exercise, thallium, sex = f.fuzzificate()
        i = inference.Inference(age, blood_pressure, blood_sugar,cholestrol,
                                heart_rate, ecg, old_peak, chest_pain,
                                exercise, thallium, sex)
        healthy, sick_1, sick_2, sick_3, sick_4 = i.infer()
        d = defuzzification.Defuzzification()
        return d.defuzzificate(healthy, sick_1, sick_2, sick_3, sick_4)
