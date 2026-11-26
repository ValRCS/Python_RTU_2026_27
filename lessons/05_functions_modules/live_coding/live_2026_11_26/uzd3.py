def basket_total(basket, prices, precision=2):
    """Aprēķina kopējo cenu iepirkumu grozam, pamatojoties uz dotajām cenām.
    Args:
        basket (list): Saraksts ar iepirkumu groza priekšmetiem.
        prices (dict): Vārdnīca, kurā atslēgas ir priekšmetu nosaukumi un vērtības ir to cenas.
        precision (int, optional): Cik zīmju aiz komata saglabāt gala cenu. Noklusējuma vērtība ir 2.
    Returns:
        float: Kopējā cena, noapaļota līdz norādītajai precizitātei.
    """
    total = 0
    for item in basket:
        if item in prices:
            total += prices[item]
        else:
            print(f"Brīdinājums: {item} nav cenas sarakstā!")
    return round(total, precision)

iepirkumu_saraksts = ["ābols", "banāns", "apelsīns", "ābols"]
cenas = {
    "ābols": 0.5,
    "banāns": 0.3,
    "apelsīns": 0.7,
    "kivi": 1.2,
    "kartupelis": 0.2
}

total_price = basket_total(iepirkumu_saraksts, cenas)
print(f"Kopējā cena ir: {total_price} EUR")