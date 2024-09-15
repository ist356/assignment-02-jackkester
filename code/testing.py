











def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    string_nums = ("0","1","2","3","4","5","6","7","8","9")
    new_dict = []
    new_list = packaging_data.split(" ")

    for i, strings in enumerate(new_list):
        if new_list[i][0] in string_nums:
            if i+2 < len(new_list):
                if new_list[i+2] != "/":
                    new_dict.append({new_list[i+1]: int(new_list[i])})
            elif i + 2 == len(new_list):
                new_dict.append({new_list[i+1]: int(new_list[i])})
        
    return new_dict

text = "2 foo in 1 bar / 3 bars in 1 baz / 4 baz in 1 qux / 2 qux in 1 biz"
parsed = parse_packaging(text)
print(parsed)


print("[{'foo': 2}, {'bars': 3}, {'baz': 4}, {'qux': 2}, {'biz': 1}]")


def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)

    '''
    total = 1
    for i in parsed:
        for j in i.values():
            total = total * j
    return total

print(calc_total_units(parsed))

def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    return list(package[0])[0]

print(get_unit(parsed))