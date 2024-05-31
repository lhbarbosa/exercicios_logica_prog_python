
price = float(input('Digite o preço do produto: '))

discount = (price * 5) / 100
newPrice = price + discount
print(f'O produto com desconto de 5% custara: R$ {newPrice:.2f}')

