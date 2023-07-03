package_weight = 20
elements = []
packages = [0]

print("Ile elementów chcesz wysłać?: ")
elements_count = int(input())

for element in range(1, elements_count + 1):
    print(f"Podaj wagę elementu {element}")
    element_weight = int(input())
    if element_weight > 10 or element_weight < 1:
        break
    elements.append(element_weight)

for element in range(0, len(elements)):
    element_weight = elements[element]
    weigth = packages[len(packages) - 1]
    if element_weight + weigth > package_weight:
        packages.append(element_weight)
    else:
        packages[len(packages) - 1] += element_weight

min_weigth = min(packages)
max_empty_index = packages.index(
    min_weigth) + 1
max_empty_weight = package_weight - min_weigth

sum_empty_kgs = len(packages) * package_weight - sum(packages)

print(f'1. Ilosc wyslanych paczek to: {len(packages)} o kilogramach {packages}')
print(f'2. Ilość wysłanych kilogramów: {sum(packages)}')
print(f'3. Ilość wysłanych pustych kilogramów: {sum_empty_kgs}')
print(f'4. Paczka z największą ilością pustych kilogramów: '
      f'{max_empty_index} z {max_empty_weight} pustymi kilogramami')
