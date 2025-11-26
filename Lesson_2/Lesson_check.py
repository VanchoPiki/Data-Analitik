import numpy as np

product_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
prices = np.array([10.99, 20.99, 15.79, 16.56, 17.56, 13.23, 11.34, 19.14, 18.90, 14.56])
quantities = np.array([100, 56, 90, 34, 12, 45, 63, 98, 67, 101])

dates = np.array([
    '2025-01-01', '2025-02-02', '2025-03-03', '2025-04-04', '2025-05-05',
    '2025-06-06', '2025-07-07', '2025-08-08', '2025-09-09', '2025-10-10'
])

total_seles = prices * quantities
print(f"Total sales: {total_seles}")

#Total sales: [1099.   1175.44 1421.1   563.04  210.72  595.35  714.42 1875.72 1266.3 1470.56]

total_revenue = np.sum(total_seles)
print(f"Total revenue: {total_revenue}")

#Total revenue: 10391.65

average_check = np.mean(total_seles)
print(f"Average check: {average_check}")

#Average check: 1039.165

best_product_index = np.argmax(total_seles)
worst_product_index = np.argmin(total_seles)
print(f"Beat product (ID: {product_ids[best_product_index]}, sales amount: {total_seles[best_product_index]:.2f}$)")

#Beat product (ID: 108, sales amount: 1875.72$)

print(f"Worst product (ID: {product_ids[worst_product_index]}, sales amount: {total_seles[worst_product_index]:.2f}$)")

#Worst product (ID: 105, sales amount: 210.72$)