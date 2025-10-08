def get_order_details():
    dishes = []
    for i in range(1, 4):
        print(f"\nEnter details for Dish #{i}")
        name = input("Dish name: ")
        price = int(input("Dish price (in sums): "))
        qty = int(input("Quantity: "))
        dishes.append({
            'name': name,
            'price': price,
            'quantity': qty,
            'total': price * qty
        })
    return dishes

def get_customer_info():
    print("\nEnter Customer Information:")
    name = input("Customer name: ")
    has_student_id = input("Has student ID? (yes/no): ").strip().lower() == 'yes'
    order_time = int(input("Order time (24-hour format, e.g., 14): "))
    return name, has_student_id, order_time

def calculate_discounts(subtotal, has_student_id, order_time):
    # Determine discount eligibility
    student_eligible = has_student_id
    happy_hour_eligible = 14 <= order_time <= 17
    large_order_eligible = subtotal >= 150000

    # Calculate individual discounts
    student_discount = 0.15 * subtotal if student_eligible else 0
    happy_hour_discount = 0.20 * subtotal if happy_hour_eligible else 0

    # Apply the better discount between student and happy hour
    if student_discount >= happy_hour_discount:
        main_discount_name = "Student Discount"
        main_discount = student_discount
    else:
        main_discount_name = "Happy Hour Discount"
        main_discount = happy_hour_discount

    large_order_discount = 0.05 * subtotal if large_order_eligible else 0

    total_discounts = main_discount + large_order_discount
    subtotal_after_discounts = subtotal - total_discounts

    return {
        'student_eligible': student_eligible,
        'student_discount': student_discount,
        'happy_hour_eligible': happy_hour_eligible,
        'happy_hour_discount': happy_hour_discount,
        'main_discount_name': main_discount_name,
        'main_discount': main_discount,
        'large_order_eligible': large_order_eligible,
        'large_order_discount': large_order_discount,
        'total_discounts': total_discounts,
        'subtotal_after_discounts': subtotal_after_discounts
    }

def calculate_fees(subtotal_after_discounts):
    service_charge = 0.10 * subtotal_after_discounts
    free_delivery = subtotal_after_discounts < 100000
    delivery_fee = 0 if free_delivery else 15000
    return service_charge, delivery_fee, free_delivery

def print_summary(customer_name, has_student_id, order_time, dishes, subtotal, discounts, service_charge, delivery_fee, free_delivery):
    print("\n--- ORDER SUMMARY ---")
    print(f"Customer Name: {customer_name}")
    print(f"Student ID: {'Yes' if has_student_id else 'No'}")
    print(f"Order Time: {order_time}:00")

    print("\nItems Ordered:")
    for dish in dishes:
        print(f"- {dish['name']} | {dish['price']} x {dish['quantity']} = {dish['total']}")

    print(f"\nSubtotal before discounts: {subtotal} sum")
    
    print("\n--- DISCOUNTS ---")
    print(f"Student Discount Eligible: {discounts['student_eligible']} | Amount: {int(discounts['student_discount'])} sum")
    print(f"Happy Hour Discount Eligible: {discounts['happy_hour_eligible']} | Amount: {int(discounts['happy_hour_discount'])} sum")
    print(f"Applied Discount: {discounts['main_discount_name']} | Amount: {int(discounts['main_discount'])} sum")
    print(f"Large Order Discount Eligible: {discounts['large_order_eligible']} | Amount: {int(discounts['large_order_discount'])} sum")
    print(f"Total Discounts: {int(discounts['total_discounts'])} sum")

    print(f"\nSubtotal after discounts: {int(discounts['subtotal_after_discounts'])} sum")
    print(f"Service Charge (10%): {int(service_charge)} sum")
    print(f"Delivery Fee: {delivery_fee} sum | Free Delivery: {free_delivery}")

    final_total = int(discounts['subtotal_after_discounts'] + service_charge + delivery_fee)
    total_saved = int(discounts['total_discounts'])
    
    print(f"\n--- FINAL TOTAL ---")
    print(f"Final Total: {final_total} sum")
    print(f"Total Saved: {total_saved} sum")

def main():
    dishes = get_order_details()
    customer_name, has_student_id, order_time = get_customer_info()

    subtotal = sum(d['total'] for d in dishes)

    discounts = calculate_discounts(subtotal, has_student_id, order_time)
    service_charge, delivery_fee, free_delivery = calculate_fees(discounts['subtotal_after_discounts'])

    print_summary(
        customer_name,
        has_student_id,
        order_time,
        dishes,
        subtotal,
        discounts,
        service_charge,
        delivery_fee,
        free_delivery
    )

# Run the calculator
main()
