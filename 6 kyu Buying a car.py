def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    i = 0
    saving = 0

    while start_price_old + saving < start_price_new:
        i += 1
        saving += saving_per_month
        if i % 2 == 0:
            percent_loss_by_month += 0.5
        start_price_old = start_price_old - (start_price_old * percent_loss_by_month) / 100
        start_price_new = start_price_new - (start_price_new * percent_loss_by_month) / 100

    return [i, round(start_price_old + saving - start_price_new)]


print(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
print(nbMonths(12000, 8000, 1000, 1.5), [0, 4000])
