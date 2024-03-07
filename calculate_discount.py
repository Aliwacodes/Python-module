def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price
  return final_price

original_price = 100.00
discount_percent = 25

final_price = calculate_discount(original_price, discount_percent)
print(f"Final price: ${final_price:.2f}")
