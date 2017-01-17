import math


class CDPC:


    def cal_ppc(self, dose, ba, vd, weight, k):
        t=0.00000001
        e = math.exp((-1)*k*t)
        cp = (ba * dose) / (vd * weight) * e
        return cp

