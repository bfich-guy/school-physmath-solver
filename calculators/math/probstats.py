from decimal import Decimal

from system.utils.decimalhelpers import decimal_factorial, decimal_back_factorial, decimal_expected_value, decimal_logarithm


class NumberFactorial:
    def __init__(self) -> None:
        pass


    def get_fn(self, *, n: Decimal) -> Decimal:
        fn: Decimal = decimal_factorial(n)
        return fn


    def get_n(self, *, fn: Decimal) -> Decimal:
        n: Decimal = decimal_back_factorial(fn)
        return n


class BinomialCoefficient:
    def __init__(self) -> None:
        pass


    def get_Ckn(self, *, nfct: Decimal, kfct: Decimal, nminuskfct: Decimal) -> Decimal:
        Ckn: Decimal = nfct / (kfct * nminuskfct)
        return Ckn


    def get_nfct(self, *, Ckn: Decimal, kfct: Decimal, nminuskfct: Decimal) -> Decimal:
        nfct: Decimal = Ckn  * kfct * nminuskfct
        return nfct


    def get_kfct(self, *, Ckn: Decimal, nfct: Decimal, nminuskfct: Decimal) -> Decimal:
        kfct: Decimal = nfct / (Ckn * nminuskfct)
        return kfct


    def get_nminuskfct(self, *, Ckn: Decimal, nfct: Decimal, kfct: Decimal) -> Decimal:
        nminuskfct: Decimal = nfct / (Ckn * kfct)
        return nminuskfct


class BernoulliProbabilityTheory:
    def __init__(self) -> None:
        pass


    def get_Pnk(self, *, Ckn: Decimal, p: Decimal, q: Decimal, k: Decimal, n: Decimal) -> Decimal:
        Pnk: Decimal = Ckn * p ** k * q ** (n - k)
        return Pnk


    def get_Ckn(self, *, Pnk: Decimal, p: Decimal, q: Decimal, k: Decimal, n: Decimal) -> Decimal:
        Ckn: Decimal = Pnk / (p ** k * q ** (n - k))
        return Ckn


    def get_p(self, *, Pnk: Decimal, Ckn: Decimal, q: Decimal, k: Decimal, n: Decimal) -> Decimal:
        p: Decimal = (Pnk / (Ckn * q ** (n - k))) ** (Decimal("1") / k)
        return p


    def get_q(self, *, Pnk: Decimal, Ckn: Decimal, p: Decimal, k: Decimal, n: Decimal) -> Decimal:
        q: Decimal = (Pnk / (Ckn * p ** k)) ** (Decimal("1") / (n - k))
        return q


    def get_k(self, *, Pnk: Decimal, Ckn: Decimal, p: Decimal, q: Decimal, n: Decimal) -> Decimal:
        k: Decimal = decimal_logarithm((Pnk / (Ckn * q ** n)), (p * q))
        return k


    def get_n(self, *, Pnk: Decimal, Ckn: Decimal, p: Decimal, q: Decimal, k: Decimal) -> Decimal:
        n: Decimal = decimal_logarithm((Pnk / (Ckn * p ** k)), q) + k
        return n


class ExpectedValue:
    def __init__(self) -> None:
        pass


    def get_MX(self, *, x: list[Decimal], p: list[Decimal]) -> Decimal:
        MX: Decimal = decimal_expected_value(x, p)
        return MX
