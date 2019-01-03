import math


class Measurement:
    def __init__(self, measure, error=None):
        self.measure = measure
        self.error = error

    def __str__(self):
        if self.error:
            return f'{self.measure} ± {self.error}'

        return f'{self.measure}'

    def __repr__(self):
        return f'Measurement({self})'

    def __add__(self, other):
        if type(other) == Measurement:
            if self.error is None:
                if other.error is None:
                    return Measurement(self.measure + other.measure)

                else:
                    return Measurement(self.measure + other.measure,
                                       error=other.error)
            else:
                if other.error is None:
                    return Measurement(self.measure + other.measure,
                                       error=self.error)

                else:
                    return Measurement(
                        self.measure + other.measure,
                        error=math.sqrt(self.error ** 2 +
                                        other.error ** 2))
        else:
            return Measurement(self.measure + other, error=self.error)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Measurement:
            return self + Measurement(-other.measure, error=other.error)
        else:
            return Measurement(self.measure - other, error=self.error)

    def __mul__(self, other):
        if type(other) == Measurement:
            res = self.measure * other.measure
            if self.error is None:
                if other.error is None:
                    return Measurement(res)

                else:
                    return Measurement(
                        res,
                        error=abs(res * (other.error / other.measure)))
            else:
                if other.error is None:
                    return Measurement(
                        res,
                        error=abs(res * (self.error / self.measure)))

                else:
                    return Measurement(
                        res,
                        error=abs(res * math.sqrt(
                            (self.error / self.measure) ** 2
                            + (other.error / other.measure) ** 2)))
        else:
            if self.error is not None:
                return Measurement(
                    self.measure * other,
                    error=abs(other * self.error))
            else:
                return Measurement(self.measure * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, denominator):
        if type(denominator) == Measurement:
            res = self.measure / denominator.measure
            if self.error is None:
                if denominator.error is None:
                    return Measurement(res)

                else:
                    return Measurement(
                        res,
                        error=abs(res
                                  * (denominator.error / denominator.measure)))
            else:
                if denominator.error is None:
                    return Measurement(
                        res,
                        error=abs(res * (self.error / self.measure)))

                else:
                    return Measurement(
                        res,
                        error=abs(res * math.sqrt(
                            (self.error / self.measure) ** 2
                            + (denominator.error / denominator.measure) ** 2)))
        else:
            if self.error is not None:
                return Measurement(
                    self.measure / denominator,
                    error=abs(self.error / denominator))
            else:
                return Measurement(self.measure / denominator)

    def __rtruediv__(self, numerator):
        return Measurement(numerator) / self

    def __pow__(self, exponent):
        if self.error is None:
            return Measurement(self.measure ** exponent)
        else:
            return Measurement(
                self.measure ** exponent,
                error=abs(exponent * (self.measure ** exponent)
                          * (self.error / self.measure)))
