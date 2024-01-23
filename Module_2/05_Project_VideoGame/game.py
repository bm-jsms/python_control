games = ["Super Mario Bros", "Zelda Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]

top_sales = 500

genders = {
    "Super Mario Bros": "Adventure",
    "Zelda Breath of the Wild": "Adventure",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol",
}

sales_and_Stock = {
    "Super Mario Bros": (500, 200),
    "Zelda Breath of the Wild": (300, 20),
    "Cyberpunk 2077": (100, 50),
    "Final Fantasy VII": (824, 10),
}

clients = {
    "Super Mario Bros": {"Mario", "Juan", "Daniel"},
    "Zelda Breath of the Wild": {"Denis", "Lucia", "Fabian"},
    "Cyberpunk 2077": {"Daniel", "Lucia", "Raquel"},
    "Final Fantasy VII": {"Juan", "Daniel", "Lucia"},
}


def summary(game):
    print(f"\n[i] Game summary: {game}\n")
    print(f"\t[+] Game gender: {genders[game]}")
    print(f"\t[+] Game sales: {sales_and_Stock[game][0]}")
    print(f"\t[+] Game stock: {sales_and_Stock[game][1]}")
    print(f"\t[+] Game clients: {' - '.join(clients[game])}\n")


for game in games:
    if sales_and_Stock[game][0] >= top_sales:
        summary(game)

total_sales = lambda: sum(sales for my_game, (sales, _) in sales_and_Stock.items() if sales_and_Stock[my_game][0] >= top_sales)

print(f"\n[+] Total sales: {total_sales()}\n")