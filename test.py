import main


def test_main():
    credit = main.CreditCalculator(300000, 12, 6)
    assert credit.calc_ann_credit(flag=False) == 310587.06, "должно быть 310587.06"
    assert credit.calc_diff_credit(flag=False) == 310500.0, "должно быть 310500.0"

    credit = main.CreditCalculator(3000000, 12, 6)
    assert credit.calc_ann_credit(flag=False) == 310587.06, "должно быть 310587.06"
    assert credit.calc_diff_credit(flag=False) == 310500.0, "должно быть 310500.0"

if __name__ == '__main__':
    test_main()
    print("tests passed")
