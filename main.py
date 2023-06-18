weight_count = 0
package_weight = 20
packages_count = 1
empty_kilograms = [[]]

print("Ile elementów chcesz wysłać?: ")
parcel_count = int(input())

for element in range(1, parcel_count + 1):
    print(f"Podaj wagę elementu {element}")
    element_weight = int(input())
    if element_weight > 10 or element_weight < 1:
        weight_count += element_weight
        packages_count += 1
        empty_kilograms.append([])
        empty_kilograms[packages_count - 1].append(package_weight -
                                                   weight_count)
        break
    while weight_count + element_weight > package_weight:
        packages_count += 1
        empty_kilograms.append([])
        empty_kilograms[packages_count - 1].append(
            package_weight - weight_count)
        break
    if weight_count + element_weight <= package_weight:
        weight_count += element_weight
        empty_kilograms[packages_count - 1].append(package_weight -
                                                   weight_count)
    else:
        weight_count += element_weight
    if element_weight == parcel_count:
        empty_kilograms[packages_count - 1].append(package_weight -
                                                   weight_count)

max_empty_kilograms = max([max(empty_kgs) for empty_kgs in empty_kilograms])
max_empty_package = [i+1 for i, empty_kgs in enumerate(empty_kilograms) if
                     max(empty_kgs) == max_empty_kilograms][0]
max_empty_weight = max_empty_kilograms if max_empty_kilograms > 0 else 0

print(f'1. Ilość wysłanych paczek to: {packages_count}')
print(f'2. Ilość wysłanych kilogramów: {weight_count}')
print(f'3. Ilość wysłanych pustych kilogramów: '
      f'{packages_count * 20 - weight_count}')
print(f'4. Paczka z największą ilością pustych kilogramów: '
      f'{max_empty_package} z {max_empty_weight} pustymi kilogramami')
# ostatnia komenda print - zawsze pokazuje paczkę 1 z 10 pustymi kg - niestety
# nie wiem jak to prawidłowo napisać. Poproszę o wskazówki
