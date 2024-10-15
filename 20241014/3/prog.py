terrain = []
input_line = input()
line_count = 1
gas_count = 0
water_count = 0

while input_line := input():
    line_count += 1
    gas_count += input_line.count('.')
    water_count += input_line.count('~')
    if input_line[1] == '#':
        break

height = len(input_line)
width = line_count
water_rows = water_count // (width - 2) + (water_count % (width - 2) > 0)
gas_rows = height - 2 - water_rows

print('#' * width)
for _ in range(gas_rows):
    print('#' + '.' * (width - 2) + '#')
for _ in range(water_rows):
    print('#' + '~' * (width - 2) + '#')
print('#' * width)

volume = (height - 2) * (width - 2)

if gas_count > water_count:
    gas_display = '.' * 20 + f' {gas_count}/{volume}'
    gas_display_length = len(gas_display)
    water_line_length = round(water_count / gas_count * 20)
    print(gas_display)
    print(f"{'~' * water_line_length}{' ' * (gas_display_length - water_line_length - len(str(water_count)) - len(str(volume)) - 1)}{water_count}/{volume}")
else:
    water_display = '~' * 20 + f' {water_count}/{volume}'
    water_display_length = len(water_display)
    gas_line_length = round(gas_count / water_count * 20)
    print(f"{'.' * gas_line_length}{' ' * (water_display_length - gas_line_length - len(str(gas_count)) - len(str(volume)) - 1)}{gas_count}/{volume}")
    print(water_display)

