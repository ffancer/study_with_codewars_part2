def pagination_text(page_number, page_size, total_products):
    a = page_size * (page_number - 1) + 1
    b = min(page_size * page_number, total_products)

    return f"Showing {a} to {b} of {total_products} Products."


print(pagination_text(1, 10, 30), "Showing 1 to 10 of 30 Products.")
print(pagination_text(3, 10, 26), "Showing 21 to 26 of 26 Products.")
print(pagination_text(1, 10, 8), "Showing 1 to 8 of 8 Products.")
print(pagination_text(2, 30, 350), "Showing 31 to 60 of 350 Products.")
print(pagination_text(1, 23, 30), "Showing 1 to 23 of 30 Products.")
print(pagination_text(2, 23, 30), "Showing 24 to 30 of 30 Products.")
print(pagination_text(43, 15, 3456), "Showing 631 to 645 of 3456 Products.")
