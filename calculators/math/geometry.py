from decimal import Decimal

from system.utils.decimalhelpers import get_quadratic_equation_roots


#region Planimetry

class CircleAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, pi: Decimal, r: Decimal) -> Decimal:
        S: Decimal = pi * (r ** Decimal("2"))
        return S


    def get_r(self, *, S: Decimal, pi: Decimal) -> Decimal:
        r: Decimal = (S / pi).sqrt()
        return r


class CircumferenceTheorem:
    def __init__(self) -> None:
        pass


    def get_l(self, *, pi: Decimal, r: Decimal) -> Decimal:
        l: Decimal = Decimal("2") * pi * r
        return l


    def get_r(self, *, l: Decimal, pi: Decimal) -> Decimal:
        r: Decimal = l / (Decimal("2") * pi)
        return r


class ParallelogramAreaByBaseAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, h: Decimal) -> Decimal:
        S: Decimal = a * h
        return S


    def get_a(self, *, S: Decimal, h: Decimal) -> Decimal:
        a: Decimal = S / h
        return a


    def get_h(self, *, S: Decimal, a: Decimal) -> Decimal:
        h: Decimal = S / a
        return h
    

class TrapezoidMidlineTheorem:
    def __init__(self) -> None:
        pass


    def get_m(self, *, a: Decimal, b: Decimal) -> Decimal:
        m: Decimal = (a + b) / Decimal("2")
        return m


    def get_a(self, *, m: Decimal, b: Decimal) -> Decimal:
        a: Decimal = (Decimal("2") * m) - b
        return a


    def get_b(self, *, m: Decimal, a: Decimal) -> Decimal:
        b: Decimal = (Decimal("2") * m) - a
        return b


class TrapezoidAreaByMidlineAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, m: Decimal, h: Decimal) -> Decimal:
        S: Decimal = m * h
        return S


    def get_m(self, *, S: Decimal, h: Decimal) -> Decimal:
        m: Decimal = S / h
        return m


    def get_h(self, *, S: Decimal, m: Decimal) -> Decimal:
        h: Decimal = S / m
        return h


class TriangleAreaByBaseAndHeightTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, h: Decimal) -> Decimal:
        S: Decimal = (a * h) / Decimal("2")
        return S


    def get_a(self, *, S: Decimal, h: Decimal) -> Decimal:
        a: Decimal = (Decimal("2") * S) / h
        return a


    def get_h(self, *, S: Decimal, a: Decimal) -> Decimal:
        h: Decimal = (Decimal("2") * S) / a
        return h


class HeronTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, b: Decimal, c: Decimal) -> Decimal:
        p: Decimal = (a + b + c) / Decimal("2")

        S: Decimal = (p * (p - a) * (p - b) * (p - c)).sqrt()
        return S


class CosineTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, b: Decimal, c: Decimal, cosa: Decimal) -> list[Decimal]:
        a: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * b * cosa), c=((b ** Decimal("2")) - (c ** Decimal("2"))), mode="POSITIVE")
        return a


    def get_b(self, *, a: Decimal, c: Decimal, cosa: Decimal) -> list[Decimal]:
        b: list[Decimal] = get_quadratic_equation_roots(a=Decimal("1"), b=(Decimal("-2") * a * cosa), c=((a ** Decimal("2")) - (c ** Decimal("2"))), mode="POSITIVE")
        return b


    def get_c(self, *, a: Decimal, b: Decimal, cosa: Decimal) -> Decimal:
        c: Decimal = ((a ** Decimal("2")) + (b ** Decimal("2")) - (Decimal("2") * a * b * cosa)).sqrt()
        return c


    def get_cosa(self, *, a: Decimal, b: Decimal, c: Decimal) -> Decimal:
        cosa: Decimal = -((c - (a ** Decimal("2")) - (b ** Decimal("2"))) / (Decimal("2") * a * b))
        return cosa


class SineTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, sina: Decimal, R: Decimal) -> Decimal:
        a: Decimal = Decimal("2") * R * sina
        return a


    def get_sina(self, *, a: Decimal, R: Decimal) -> Decimal:
        sina: Decimal = a / (Decimal("2") * R)
        return sina


    def get_R(self, *, a: Decimal, sina: Decimal) -> Decimal:
        R: Decimal = a / (Decimal("2") * sina)
        return R


class PythagoreanTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, c: Decimal, b: Decimal) -> Decimal:
        a: Decimal = (c ** Decimal("2") - b ** Decimal("2")).sqrt()
        return a


    def get_b(self, *, c: Decimal, a: Decimal) -> Decimal:
        b: Decimal = (c ** Decimal("2") - a ** Decimal("2")).sqrt()
        return b


    def get_c(self, *, a: Decimal, b: Decimal) -> Decimal:
        c: Decimal = (a ** Decimal("2") + b ** Decimal("2")).sqrt()
        return c


class TriangleAreaByInscribedCircleTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, p: Decimal, r: Decimal) -> Decimal:
        S: Decimal = p * r
        return S


    def get_p(self, *, S: Decimal, r: Decimal) -> Decimal:
        p: Decimal = S / r
        return p


    def get_r(self, *, S: Decimal, p: Decimal) -> Decimal:
        r: Decimal = S / p
        return r


class TriangleAreaByCircumscripedCircleTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, a: Decimal, b: Decimal, c: Decimal, R: Decimal) -> Decimal:
        S: Decimal = (a * b * c) / (Decimal("4") * R)
        return S


    def get_a(self, *, S: Decimal, b: Decimal, c: Decimal, R: Decimal) -> Decimal:
        a: Decimal = (S * Decimal("4") * R) / (b * c)
        return a


    def get_b(self, *, S: Decimal, R: Decimal, a: Decimal, c: Decimal) -> Decimal:
        b: Decimal = (S * Decimal("4") * R) / (a * c)
        return b


    def get_c(self, *, S: Decimal, R: Decimal, a: Decimal, b: Decimal) -> Decimal:
        c: Decimal = (S * Decimal("4") * R) / (a * b)
        return c


    def get_R(self, *, a: Decimal, b: Decimal, c: Decimal, S: Decimal) -> Decimal:
        R: Decimal = (a * b * c) / (Decimal("4") * S)
        return R


class TriangleSideProjectionTheorem:
    def __init__(self) -> None:
        pass


    def get_h(self, *, a: Decimal, cossina: Decimal) -> Decimal:
        h: Decimal = a * cossina
        return h


    def get_a(self, *, h: Decimal, cossina: Decimal) -> Decimal:
        a: Decimal = h / cossina
        return a


    def get_cossina(self, *, h: Decimal, a: Decimal) -> Decimal:
        cossina: Decimal = h / a
        return cossina


class FigureAreaBySimilarityCoefficientTheorem:
    def __init__(self) -> None:
        pass


    def get_S2(self, *, S1: Decimal, k: Decimal) -> Decimal:
        S2: Decimal = S1 * k ** Decimal("2")
        return S2


    def get_S1(self, *, S2: Decimal, k: Decimal) -> Decimal:
        S1: Decimal = S2 / k ** Decimal("2")
        return S1
    
    
    def get_k(self, *, S1: Decimal, S2: Decimal) -> Decimal:
        k: Decimal = (S2 / S1).sqrt()
        return k


class PolygonAnglesSumTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, n: Decimal) -> Decimal:
        S: Decimal = (n - Decimal("2")) * Decimal("180")
        return S


    def get_n(self, *, S: Decimal) -> Decimal:
        n: Decimal = (S / Decimal("180")) + Decimal("2")
        return n


class RegularPolygonAngleTheorem:
    def __init__(self) -> None:
        pass


    def get_a(self, *, n: Decimal) -> Decimal:
        a: Decimal = Decimal("180") - (Decimal("360") / n)
        return a


    def get_n(self, *, a: Decimal) -> Decimal:
        n: Decimal = Decimal("360") / (Decimal("180") - a)
        return n


class RegularPolygonAreaByCircumscripedCircleTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, n: Decimal, a: Decimal, R: Decimal) -> Decimal:
        S: Decimal = n * a * (R ** Decimal("2") - Decimal("0.25") * (a ** Decimal("2") / Decimal("4"))).sqrt()
        return S


    def get_n(self, *, S: Decimal, a: Decimal, R: Decimal) -> Decimal:
        n: Decimal = S / (a * (R ** Decimal("2") - Decimal("0.25") * (a ** Decimal("2") / Decimal("4"))).sqrt())
        return n


    def get_a(self, *, S: Decimal, n: Decimal, R: Decimal) -> list[Decimal]:
        a: list[Decimal] = get_quadratic_equation_roots(a=-(n ** Decimal("2")), b=((n * R) ** Decimal("2")), c=(Decimal("4") * S ** Decimal("2")), mode="POSITIVE")
        return a

    def get_R(self, *, S: Decimal, n: Decimal, a: Decimal) -> Decimal:
        R: Decimal = ((Decimal("4") * S ** Decimal("2") - n ** Decimal("2") * a ** Decimal("4")) / ((n * a) * Decimal("2"))).sqrt()
        return R

    
class RegularPolygonPerimeterTheorem:
    def __init__(self) -> None:
        pass


    def get_P(self, *, a: Decimal, n: Decimal) -> Decimal:
        P: Decimal = a * n
        return P


    def get_a(self, *, P: Decimal, n: Decimal) -> Decimal:
        a: Decimal = P / n
        return a


    def get_n(self, *, P: Decimal, a: Decimal) -> Decimal:
        n: Decimal = P / a
        return n

#endregion


#region Stereometry

class PrismAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, Sb: Decimal, Ss: Decimal) -> Decimal:
        S: Decimal = Decimal("2") * Sb + Ss
        return S


    def get_Sb(self, *, S: Decimal, Ss: Decimal) -> Decimal:
        Sb: Decimal = (S - Ss) / Decimal("2")
        return Sb


    def get_Ss(self, *, S: Decimal, Sb: Decimal) -> Decimal:
        Ss: Decimal = S - Decimal("2") * Sb
        return Ss


class PrismVolumeTheorem:
    def __init__(self) -> None:
        pass


    def get_V(self, *, Sb: Decimal, h: Decimal) -> Decimal:
        V: Decimal = Sb * h
        return V


    def get_Sb(self, *, V: Decimal, h: Decimal) -> Decimal:
        Sb: Decimal = V / h
        return Sb


    def get_h(self, *, V: Decimal, Sb: Decimal) -> Decimal:
        h: Decimal = V / Sb
        return h


class CylinderAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, pi: Decimal, R: Decimal, h: Decimal) -> Decimal:
        S: Decimal = Decimal("2") * pi * R * (R + h)
        return S


    def get_R(self, *, S: Decimal, pi: Decimal, h: Decimal) -> list[Decimal]:
        R: list[Decimal] = get_quadratic_equation_roots(a=(Decimal("2") * pi), b=(Decimal("2") * pi * h), c=-S, mode="POSITIVE")
        return R


    def get_h(self, *, S: Decimal, pi: Decimal, R: Decimal) -> Decimal:
        h: Decimal = S / (Decimal("2") * pi * R) - R
        return h


class CylinderVolumeTheorem:
    def __init__(self) -> None:
        pass


    def get_V(self, *, pi: Decimal, R: Decimal, h: Decimal) -> Decimal:
        V: Decimal = pi * R ** Decimal("2") * h
        return V


    def get_R(self, *, V: Decimal, pi: Decimal, h: Decimal) -> Decimal:
        R: Decimal = (V / (pi * h)).sqrt()
        return R


    def get_h(self, *, V: Decimal, pi: Decimal, R: Decimal) -> Decimal:
        h: Decimal = V / (pi * R ** Decimal("2"))
        return h


class ConeAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, pi: Decimal, R: Decimal, l: Decimal) -> Decimal:
        S: Decimal = pi * R * (R + l)
        return S
        

    def get_R(self, *, S: Decimal, pi: Decimal, l: Decimal) -> list[Decimal]:
        R: list[Decimal] = get_quadratic_equation_roots(a=pi, b=(pi * l), c=-S, mode="POSITIVE")
        return R


    def get_l(self, *, S: Decimal, pi: Decimal, R: Decimal) -> Decimal:
        l: Decimal = S / (pi * R) - R
        return l
    

class ConeVolumeTheorem:
    def __init__(self) -> None:
        pass


    def get_V(self, *, pi: Decimal, R: Decimal, h: Decimal) -> Decimal:
        V: Decimal = (pi * R ** Decimal("2") * h) / Decimal("3")
        return V
        

    def get_R(self, *, V: Decimal, pi: Decimal, h: Decimal) -> Decimal:
        R: Decimal = ((Decimal("3") * V) / (pi * h)).sqrt()
        return R


    def get_h(self, *, V: Decimal, pi: Decimal, R: Decimal) -> Decimal:
        h: Decimal = (Decimal("3") * V) / (pi * R ** Decimal("2"))
        return h
    

class SphereAreaTheorem:
    def __init__(self) -> None:
        pass


    def get_S(self, *, pi: Decimal, R: Decimal) -> Decimal:
        S: Decimal = Decimal("4") * pi * R ** Decimal("2")
        return S


    def get_R(self, *, S: Decimal, pi: Decimal) -> Decimal:
        R: Decimal = (S / (Decimal("4") * pi)).sqrt()
        return R

    
class SphereVolumeTheorem:
    def __init__(self) -> None:
        pass


    def get_V(self, *, pi: Decimal, R: Decimal) -> Decimal:
        V: Decimal = (Decimal("4") * pi * R ** Decimal("3")) / Decimal("3")
        return V


    def get_R(self, *, V: Decimal, pi: Decimal) -> Decimal:
        R: Decimal = pow(((Decimal("3") * V) / (Decimal("4") * pi)), Decimal("1") / Decimal("3")).quantize(Decimal("1"))
        return R

#endregion
