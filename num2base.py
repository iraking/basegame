def _n2base_(n_10, base, rev_result, symbols):
    a, b = divmod(n_10, base)
    rev_result.append(symbols[b])
    if a >= base:
        return _n2base_(a, base, rev_result, symbols)
    else:
        rev_result.append(symbols[a])
        return rev_result


def n2base(n_10, base):
    _symbols_ = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rev_result = []
    if base > 35:
        raise 'base bigger then 35 not supprted'
    _n2base_(n_10, base, rev_result, _symbols_)
    print rev_result
    
    result_str = ''.join(rev_result)[::-1]
    if result_str.startswith('0'): 
        result_str = result_str[1:]
    print result_str

# num_10 = raw_input('Number in base 10? ')
# new_base = raw_input('In what base to present? ')
# n2base(int(num_10), int(new_base))

