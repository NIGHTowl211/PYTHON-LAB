
item1 = float(input("Enter the price of item 1: ₹"))
item2 = float(input("Enter the price of item 2: ₹"))
item3 = float(input("Enter the price of item 3: ₹"))
item4 = float(input("Enter the price of item 4: ₹"))

subtotal = item1 + item2 + item3 + item4


if subtotal > 1000:
    discount = subtotal * 0.10
else:
    discount = 0.0
discounted_subtotal = subtotal - discount

gst = discounted_subtotal * 0.12


grand_total = discounted_subtotal + gst

print(f"\n--- Bill Details ---")
print(f"Original Subtotal: ₹{subtotal:.2f}")
print(f"Discounted Subtotal: ₹{discounted_subtotal:.2f}")
print(f"Tax Amount (GST 12%): ₹{gst:.2f}")
print(f"Grand Total: ₹{grand_total:.2f}")
