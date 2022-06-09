def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    i = 0
    saved_this_month = 0

    while (start_price_old + saved_this_month) <= start_price_new:
        i += 1
        if i % 2 == 0:
            percent_loss_by_month += 0.5
        start_price_old *= 1 - (percent_loss_by_month / 100)
        start_price_new *= 1 - (percent_loss_by_month / 100)
        saved_this_month += saving_per_month

    return [i, round(start_price_old + saved_this_month - start_price_new)]


print(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
print(nbMonths(12000, 8000, 1000, 1.5), [0, 4000])
