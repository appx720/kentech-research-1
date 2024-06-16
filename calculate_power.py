"""
code for calculating power or efficiency
"""

def wave_power(h, T, L):
    """
    h: 파도 높이(m)
    T: 파도 주기(s)
    L: 해변 길이(m)

    반환값의 단위는 kW(발전 에너지)
    """
    return 0.96 * (h ** 2) * T * L

def solar_power(x, y):
    """
    x: 1m^2에 입사한 빛에너지(J)
    y: 출력된 빛에너지(J)

    반환값 단위는 %(발전 효율)
    """
    return (y / x) * 100

def water_power(q, h, nt, ng):
    """
    q: 유량(m^3/s)
    h: 유효 낙차(m)
    nt: 수차 효율(%)
    ng: 발전기 효율(%)

    반환값 단위는 kW(발전 에너지)
    """
    return 9.8 * q * h * nt * ng

def wind_power(rho, A, v, Cp, t):
    """
    rho: 공기 밀도(kg/m^3)
    A: 단위 시간당 공기가 통과하는 면적(m^2)
    v: 풍속(m/s)
    Cp: 풍력터빈의 성능을 나타내는 계수(0<=Cp<=1)
    t: 발전 시간(s)

    반환값 단위는 %(발전 효율)
    """

    e = 0.5 * rho * A * (v ^ 3)
    p = e * Cp
    E = p * t
    return E / p


wave_power(0, 0, 0)
solar_power(0, 0)
water_power(0, 0, 0, 0)
wind_power(0, 0, 0, 0, 0)