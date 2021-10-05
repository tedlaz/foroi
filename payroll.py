import requests
from taxes import ergazomenos_period_taxes as ptaxes


def get_kpk_from_api(kpk, period):
    url = f"https://vwf3fo.deta.dev/kpkper?kpk={kpk}&period={period}"
    response = requests.get(url).json()
    if not response['result'][0]['kpk']:
        raise ValueError
    penos = response['result'][0]['enos']
    pefkatotal = response['result'][0]['total']
    return penos, pefkatotal


def efka2dic(value: float, kpk: str, period: int) -> dict:
    penos, pefkatotal = get_kpk_from_api(kpk, period)
    enos, total, etis = calc_efka(value, penos, pefkatotal)
    return {
        'value': value,
        'kpk': kpk,
        'pososto_efka_ergazomenoy': penos,
        'pososto_efka_synolika': pefkatotal,
        'efka_ergazomenoy': enos,
        'efka_ergodoti': etis,
        'efka_total': total,
    }


def calc_efka(value, penos, pefkatotal) -> tuple[float, ...]:
    enos = round(value * penos / 100.0, 2)
    total = round(value * pefkatotal / 100.0, 2)
    etis = round(total - enos, 2)
    return enos, total, etis


def efka_total(period, kpk_list, apodoxes_gia_efka):
    efkalist = []
    total_efka_enoy = total_efka_eti = total_efka = 0
    for kpk in kpk_list:
        efka = efka2dic(apodoxes_gia_efka, kpk, period)
        total_efka_enoy = round(total_efka_enoy + efka['efka_ergazomenoy'], 2)
        total_efka_eti = round(total_efka_eti + efka['efka_ergodoti'], 2)
        total_efka = round(total_efka + efka['efka_total'], 2)
        efkalist.append(efka)
    return total_efka_enoy, total_efka_eti, total_efka, efkalist


def calcmis_misthotos(
    *,
    period: int,
    misthos: float,
    meres: float = 25,
    kpk_list: list = ['101'],
    paidia: int = 0
) -> dict:
    """Υπολογισμός μισθοδοσίας Μήνα για μισθωτούς"""
    apodoxes_gia_efka = round(misthos * meres / 25.0, 2)
    total_efka_enoy, total_efka_eti, total_efka, efkalist = efka_total(
        period, kpk_list, apodoxes_gia_efka)
    apodoxes_gia_foro = round(apodoxes_gia_efka - total_efka_enoy, 2)
    taxes = ptaxes(year_from_period(period), apodoxes_gia_foro, paidia, 14)
    return {
        'period': period,
        'misthos': misthos,
        'apodoxes_periodoy': apodoxes_gia_efka,
        'total_efka_ergazomenoy': total_efka_enoy,
        'total_efka_ergodoti': total_efka_eti,
        'total_efka': total_efka,
        'apodoxes_gia_foro': apodoxes_gia_foro,
        'barytis_periodoy': 14,
        'foros_eisodimatos': taxes['tax'],
        'foros_eea': taxes['eea'],
        'foroi_synolika': taxes['total_taxes'],
        'pliroteo': round(apodoxes_gia_foro - taxes['total_taxes'], 2),
        'efka': efkalist,
        'taxes': taxes,
    }


def year_from_period(period):
    return int(str(period)[:4])
