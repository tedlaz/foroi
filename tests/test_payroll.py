from payroll import calcmis_misthotos


def test_calc_misthotos():
    # res = calc_misthotos(period=202109, misthos=1164.42, meres=25)
    res = calcmis_misthotos(period=202109, misthos=845, meres=25, paidia=1)
    assert res['pliroteo'] == 716.75
    re2 = calcmis_misthotos(period=202109, misthos=845,
                            meres=25, paidia=1, kpk_list=['101', '026'])
    print(re2)
