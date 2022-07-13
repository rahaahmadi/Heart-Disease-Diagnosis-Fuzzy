class Defuzzification():

    def __init__(self):
        self.step = 0.005

    def defuzzificate(self, healthy, sick_1, sick_2, sick_3, sick_4):
        temp, sumy, sumx = (0, 0, 0)
        while temp <= 4:
            y = self.output_fuzzificate(temp)
            y =  max(min(healthy, y['healthy']), min(sick_1, y['sick_1']),
                   min(sick_2, y['sick_2']), min(sick_3, y['sick_3']),
                   min(sick_4, y['sick_4']))
            sumx += y
            sumy += y * temp
            temp += self.step
        output = sumy / sumx
        return self.get_results(output)
    
    def get_results(self, value):

        result_list = []
        res = ''

        if value < 1.78 :
            result_list.append('healthy ')
        if 1 <= value <= 2.51:
            result_list.append('sick1 ')
        if 1.78 <= value <= 3.25:
            result_list.append('sick2 ')
        if 1.5 <= value <= 4.5:
            result_list.append('sick3 ')
        if value > 3.25 :
            result_list.append('sick4 ')

        for i in range(len(result_list)):
            if i != 0:
                res += 'and '
            res += result_list[i]

        res += ': ' + str(value)

        return res
    
    def calc_membership(self, crisp_val, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        a = (y2 - y1) / (x2 - x1)
        fuzzy_value = y1 + a * (crisp_val - x1)
        return fuzzy_value
    
    def output_fuzzificate(self, x):
        return {
            'healthy': self.output_healthy(x),
            'sick_1': self.output_sick1(x),
            'sick_2': self.output_sick2(x),
            'sick_3': self.output_sick3(x),
            'sick_4': self.output_sick4(x)
            }

    def output_healthy(self, x):
        if x <= 0.25:
            return 1
        elif 0.25 < x < 1:
            return self.calc_membership(x, (0.25, 1), (1, 0))
        else:
            return 0


    def output_sick1(self, x):
        if x <= 0 or x >= 2:
            return 0
        elif 0 < x <= 1:
            return self.calc_membership(x, (0, 0), (1, 1))
        else:
            return self.calc_membership(x, (2, 0), (1, 1))


    def output_sick2(self, x):
        if x <= 1 or x >= 3:
            return 0
        elif 1 < x <= 2:
            return self.calc_membership(x, (1, 0), (2, 1))
        else:
            return self.calc_membership(x, (3, 0), (2, 1))


    def output_sick3(self, x):
        if x <= 2 or x >= 4:
            return 0
        elif 2 < x <= 3:
            return self.calc_membership(x, (2, 0), (3, 1))
        else:
            return self.calc_membership(x, (4, 0), (3, 1))


    def output_sick4(self, x):
        if x <= 3:
            return 0
        elif 3 < x <= 3.75:
            return self.calc_membership(x, (3, 0), (3.75, 1))
        else:
            return 1

